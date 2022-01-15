import numpy as np

from numpy import ndarray
from typing import Union

from src.equalpyzer.wavefile import WaveFile


class Equalizer:
    """Equalizer that can be used to manipulate frequency bands from a wave file."""

    def __init__(self, wave_file):
        self.wav: WaveFile = wave_file

        self.altered_signal: ndarray = self.wav.input_signal.copy()
        self.altered_amplitudes: ndarray = self.wav.amplitudes.copy()
        self.altered_amplitudes_db: ndarray = self.wav.amplitudes_db.copy()

    def boost(self, decibels: int, low_cut: int = 0, high_cut: Union[int, None] = None) -> None:
        if low_cut > high_cut:
            raise ValueError('Low-cut frequency cannot be higher than high-cut frequency!')

        # set high_cut to highest frequency in the signal if not given
        high_cut = self.wav.frequencies[-1] if high_cut is None else high_cut

        # apply boost on a simple rectangle window # TODO use different window function
        self.altered_amplitudes_db = self.wav.amplitudes_db.copy()
        self.altered_amplitudes_db[(self.wav.frequencies > low_cut) & (self.wav.frequencies < high_cut)] += decibels

        # reverse the dBFS conversion and apply boost to amplitudes
        scaled_amp_values = self.wav.max_sample_value * np.power(10, self.altered_amplitudes_db / 20)
        self.altered_amplitudes = scaled_amp_values * len(self.altered_amplitudes)

        # save altered signal
        self.altered_signal = np.fft.irfft(self.altered_amplitudes)
