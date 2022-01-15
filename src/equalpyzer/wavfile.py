import numpy as np

from numpy import ndarray
from scipy.io import wavfile as wf

from typing import Union


class Wavfile:
    """
    A container for specific properties from a single wav file.
    Contains properties which are important in order to apply FFT on the signal.
    """

    def __init__(self, path: str):
        self.input_signal: Union[ndarray, None] = None

        self.sample_rate: Union[int, None] = None
        self.max_sample_value: Union[int, None] = None  # value of loudest sample in the signal

        self.duration: float = Union[float, None]  # length of signal in seconds
        self.num_of_samples: int = Union[int, None]

        self.load_signal(path)

    def load_signal(self, path: str) -> None:
        self.sample_rate, self.input_signal = wf.read(path)

        self.max_sample_value = np.max(self.input_signal)

        self.num_of_samples: int = len(self.input_signal)
        self.duration: float = self.num_of_samples / self.sample_rate
