import numpy as np

from numpy import ndarray
from scipy.io import wavfile as wf
from typing import Union

from equalpyzer.wavfile import Wavfile


class Equalizer:
    """Equalizer that can be used to manipulate frequency bands of a signal read from a wavfile."""

    def __init__(self, wavfile):
        self._wav: Wavfile = wavfile

        self._amplitudes: Union[ndarray, None] = None
        self._frequencies: Union[ndarray, None] = None
        self._amplitudes_db: Union[ndarray, None] = None

    def save_wavfile(self, path: str) -> None:
        if self._amplitudes is None:  # if we did not fft the signal, just save it
            # this causes 24bit files to convert to 32bit files because numpy is missing 24bit data types
            wf.write(path, self._wav.sample_rate, self._wav.input_signal.astype(self._wav.input_signal.dtype))
        else:
            output_signal: ndarray = np.fft.irfft(self.amplitudes)

            if isinstance(self._wav.input_signal.dtype, np.integer):
                output_signal = np.round(output_signal)

            wf.write(path, self._wav.sample_rate, output_signal.astype(self._wav.input_signal.dtype))

    def amplify(self, gain: float, low_cut: int = 0, high_cut: Union[int, None] = None) -> None:
        if high_cut is None:
            high_cut = self.frequencies[-1]  # set to highest frequency in the signal
        if low_cut > high_cut:
            raise ValueError('Low-cut frequency cannot be higher than high-cut frequency!')

        self.amplitudes[(self.frequencies > low_cut) & (self.frequencies < high_cut)] *= gain
        self._amplitudes_db = None  # delete the old db scale

    @property
    def amplitudes(self) -> ndarray:
        """Amplitudes resulting from FFT"""
        if self._amplitudes is None:  # if we did not calculate the frequency domain yet
            self._amplitudes = np.fft.rfft(self._wav.input_signal)
        return self._amplitudes

    @property
    def frequencies(self) -> ndarray:
        """Frequencies resulting from FFT"""
        if self._frequencies is None:
            self._frequencies = np.fft.rfftfreq(self._wav.input_signal.size, 1 / self._wav.sample_rate)
        return self._frequencies

    @property
    def amplitudes_db(self) -> ndarray:
        """Amplitudes resulting from FFT but in dBFS scaling"""
        if self._amplitudes_db is None:
            # scale the amplitude of the fft by a factor of 2,
            # because we are using only half of the fft spectrum
            # (and normalize it by the number of amplitude samples)
            scaled_freq_values = self.amplitudes * 2 / len(self.amplitudes)
            # replace first self.amplitudes with abs(self.amplitudes) if wrong ^^

            # convert to dBFS (decibels full scale)
            self._amplitudes_db = 20 * np.log10(scaled_freq_values / self._wav.max_sample_value)

        return self._amplitudes_db
