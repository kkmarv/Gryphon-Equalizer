import numpy as np

from numpy import ndarray
from scipy.io import wavfile as wf

from typing import Union


class WaveFile:
    """
    A container for specific properties from a single wav file.
    Contains properties which are important in order to manipulate the signal.
    """

    def __init__(self, path: str):
        self.sample_rate: Union[int, None] = None
        self.input_signal: Union[ndarray, None] = None
        self.duration: float = Union[float, None]  # length of signal in seconds
        self.num_of_samples: int = Union[int, None]
        self.max_sample_value: Union[int, None] = None  # value of loudest sample in the signal

        self.amplitudes: Union[ndarray, None] = None  # Amplitudes resulting from FFT
        self.frequencies: Union[ndarray, None] = None  # Frequencies resulting from FFT
        self.amplitudes_db: Union[ndarray, None] = None  # Amplitudes resulting from FFT but in dBFS scaling

        self.load_signal(path)

    def load_signal(self, path: str) -> None:
        """Opens the wave file from path and reads all relevant data."""

        self.sample_rate, self.input_signal = wf.read(path)
        self.num_of_samples: int = len(self.input_signal)
        self.duration: float = self.num_of_samples / self.sample_rate

        max_sample_value = np.max(self.input_signal)
        min_sample_value = np.min(self.input_signal)
        self.max_sample_value = min_sample_value if np.abs(min_sample_value) > max_sample_value else max_sample_value

        self.amplitudes = np.fft.rfft(self.input_signal)
        self.frequencies = np.fft.rfftfreq(self.input_signal.size, 1 / self.sample_rate)

        # scale the amplitude of the fft by a factor of 2,
        # because we are using only half of the fft spectrum
        # and normalize it by the number of amplitude samples
        scaled_amp_values: ndarray = 2 * self.amplitudes / len(self.amplitudes)
        # convert to dBFS (decibels full scale)
        self.amplitudes_db = 20 * np.log10(scaled_amp_values / self.max_sample_value)

    def save_signal(self, path: str, output_signal: ndarray) -> None:
        output_signal: ndarray = self.input_signal if output_signal is None else output_signal

        if isinstance(self.input_signal.dtype, np.integer):
            output_signal = np.round(output_signal)

        # this causes 24bit files to convert to 32bit files because numpy is missing a 24bit data type
        wf.write(path, self.sample_rate, output_signal.astype(self.input_signal.dtype))
