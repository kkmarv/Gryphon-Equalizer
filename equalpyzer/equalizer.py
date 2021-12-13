import numpy as np

from numpy import ndarray
from scipy.io import wavfile as wf
from matplotlib import pyplot as plt

from typing import Tuple, Union


class Equalizer:
    def __init__(self):
        self.__sample_rate: Union[int, None] = None
        self.__time_domain: Union[ndarray, None] = None
        self.__freq_domain: Union[ndarray, None] = None
        self.__normalizer: Union[int, None] = None  # loudest sample in the file

    def load_signal(self, path: str) -> None:
        self.__sample_rate, self.__time_domain = wf.read(path)
        self.__normalizer = np.max(self.__time_domain)

    def plot_time_domain(self) -> None:
        n: int = len(self.__time_domain)  # number of samples
        sec: float = n / self.__sample_rate  # length of file in seconds

        x_values: ndarray = self.__time_domain / self.__normalizer  # normalize values
        y_values: ndarray = np.linspace(start=0, stop=sec, num=n)  # calculate the scaling of y axis

        # plot graph and set visual parameters
        plt.plot(y_values, x_values)
        plt.xlim(left=0, right=sec)
        plt.ylim(top=1, bottom=-1)
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_freq_domain(self) -> None:
        n = len(self.__time_domain)  # number of time domain samples
        sec: float = n / self.__sample_rate  # length of file in seconds

        # scale the magnitude of the fft by and factor of 2,
        # because we are using only half of the fft spectrum
        # and normalize it by the number of frequency samples
        scaled_x_values = np.abs(self.freq_domain) * 2 / len(self.freq_domain)

        # convert to dBFS (decibels full scale)
        db_x_values = 20 * np.log10(scaled_x_values / self.__normalizer)

        # calculate the scaling of y axis
        y_values = np.arange((n / 2) + 1) / sec

        # frequency labels
        x_ticks = [31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        x_labels = ['31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k']

        # plot graph and set visual parameters
        plt.plot(y_values, db_x_values)
        plt.grid(True)
        plt.xscale('log')
        plt.xticks(x_ticks, x_labels)
        plt.xlim(right=20000)
        plt.ylim(top=0, bottom=-90)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude [dBFS]')
        plt.fill_between(y_values, db_x_values, -90)
        plt.show()

    @property
    def freq_domain(self) -> ndarray:
        if self.__freq_domain is None:  # if we did not calculate the frequency domain yet
            self.__freq_domain = np.fft.rfft(self.__time_domain)
        return self.__freq_domain


def dbfs_rfft(signal: ndarray, fs: int, window: ndarray = None, ref: int = 32768) -> Tuple[ndarray, ndarray]:
    """
    Calculate spectrum in dBFS (decibels full scale)

    Args:
        signal: input signal
        fs: sampling frequency
        window: vector containing window samples (same length as x).
             If not provided, then a rectangular window is used by default.
        ref: reference value used for dBFS scale. 32768 for int16, 8388608 for int24 and 1 for float

    Returns:
        frequencies: frequency vector & dbfs_amp: spectrum in dBFS scale
    """

    N = len(signal)  # Length of input sequence

    if window is None:
        window = np.ones(N)
    if len(signal) != len(window):
        raise ValueError('Signal and window must be of the same length')
    signal = signal * window

    # Calculate real FFT and frequency vector
    amplitudes = np.fft.rfft(signal)
    frequencies = np.arange((N / 2) + 1) / (float(N) / fs)

    # Scale the magnitude of FFT by window and factor of 2, because we are using only half of FFT spectrum.
    scaled_amp = np.abs(amplitudes) * 2 / np.sum(window)

    # Convert to dBFS
    dbfs_amp = 20 * np.log10(scaled_amp / ref)

    return frequencies, dbfs_amp


def main():
    a = '../examples/16-bit-signed-stereo.wav'
    b = '../examples/16-bit-signed-mono.wav'
    c = '../examples/24-bit-signed-stereo.wav'
    d = '../examples/24-bit-signed-mono.wav'
    e = '../examples/32-bit-float-stereo.wav'
    f = '../examples/32-bit-float-mono.wav'

    eq = Equalizer()
    eq.load_signal(b)
    eq.plot_time_domain()
    eq.plot_freq_domain()


if __name__ == "__main__":
    main()
