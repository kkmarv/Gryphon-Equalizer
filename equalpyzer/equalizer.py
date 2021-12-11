import numpy as np
from scipy.io import wavfile as wf

from typing import Tuple
from matplotlib import pyplot as plt


def dbfs_rfft(signal: np.ndarray, fs: int, window: np.ndarray = None, ref: int = 32768) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate spectrum in dBFS scale

    Args:
        x: input signal
        fs: sampling frequency
        win: vector containing window samples (same length as x).
             If not provided, then a rectangular window is used by default.
        ref: reference value used for dBFS scale. 32768 for int16, 8388608 for int24 and 1 for float

    Returns:
        frequencies: frequency vector
        dbfs_amp: spectrum in dBFS scale
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
    dbfs_amp = 20 * np.log10(scaled_amp/ref)

    return frequencies, dbfs_amp


def plot_dbfs(freq: np.ndarray, dbfs_amp: np.ndarray, xscale='log') -> None:
    """
    Plot spectrum in dBFS scale

    Args:
        freq: input frequencies
        dbfs_amp: input amplitudes in dBFS scale
        xscale: x-axis scaling . 'log' for logarithmic and 'lin' for linear

    Returns: None
    """

    # frequency labels
    xticks = [31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    xlabels = ['31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k']

    plt.plot(freq, dbfs_amp)
    plt.grid(True)
    plt.xscale(xscale)
    plt.xticks(xticks, xlabels)
    plt.xlim(right=20000)
    plt.ylim(top=0)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dBFS]')
    plt.show()


def plot_dbfs_custom(freq: np.ndarray, dbfs_amp: np.ndarray, xscale='log') -> None:
    """
    Plot spectrum in dBFS scale

    Args:
        freq: input frequencies
        dbfs_amp: input amplitudes in dBFS scale
        xscale: x-axis scaling . Use 'log' for logarithmic and 'lin' for linear

    Returns: None
    """

    # frequency labels
    xticks = [31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    xlabels = ['31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k']
    color = 'black'

    plt.plot(freq, dbfs_amp, color=color)
    plt.grid(True, color=color)
    plt.xscale(xscale)
    plt.xticks(xticks, xlabels)
    plt.xlim(right=20000)
    plt.ylim(top=0, bottom=-90)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dBFS]')
    plt.fill_between(freq, dbfs_amp, -90, color=color)
    plt.show()


def equalizer_10_band():
    pass


def get_channels(data: np.ndarray) -> int:
    return len(data.shape)  # stereo is 2d while mono is 1d


def get_bit_depth(data: np.ndarray) -> np.dtype:
    return data.dtype  # return np.ndarray's data type


def get_length_in_sec(sample_rate: int, data: np.ndarray) -> float:
    return data.shape[0]/sample_rate


def normalize(data: np.ndarray) -> np.ndarray:
    return data/(np.max(np.abs(data), axis=0))


def main():
    sample_rate_16_s, data_16_s = wf.read('./examples/16-bit-signed-stereo.wav')
    sample_rate_16_m, data_16_m = wf.read('./examples/16-bit-signed-mono.wav')
    sample_rate_24_s, data_24_s = wf.read('./examples/24-bit-signed-stereo.wav')
    sample_rate_24_m, data_24_m = wf.read('./examples/24-bit-signed-mono.wav')
    sample_rate_32_s, data_32_s = wf.read('./examples/32-bit-float-stereo.wav')
    sample_rate_32_m, data_32_m = wf.read('./examples/32-bit-float-mono.wav')

    # Take slice
    N = 8192
    win = np.hamming(N)

    freq, dbfs_amp = dbfs_rfft(data_16_m[0:N], sample_rate_16_m, win, ref=32768)
    plot_dbfs_custom(freq, dbfs_amp)

    x_values = np.linspace(0, 10, num=10*48000)
    y_values = np.sin(2*np.pi*1000*x_values)

    freq, dbfs_amp = dbfs_rfft(y_values, 48000)
    plot_dbfs_custom(freq, dbfs_amp)


if __name__ == "__main__":
    main()
