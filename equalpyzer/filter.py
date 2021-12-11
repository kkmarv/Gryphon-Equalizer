import numpy as np
import scipy.io.wavfile as wf

from numpy import ndarray
from scipy.signal import butter
from scipy.signal.signaltools import sosfilt

from typing import Tuple
from equalizer import dbfs_rfft, plot_dbfs
from matplotlib import pyplot as plt


# cut-offs for 10 bandpass filters
super_lows = (0, 31)
lows = (32, 62)
higher_lows = (63, 125)
lower_mids = (126, 250)
mids = (251, 500)
higher_mids = (501, 1000)
lower_highs = (1001, 2000)
highs = (2001, 4000)
super_highs = (4001, 8000)
ultra_highs = (8001, 16000)


def bandpass_filter(signal: ndarray, cutoffs: Tuple[int, int], fs: int, order: int = 5) -> ndarray:
    """Returns the given signal filtered at given lowcut and highcut frequencies.

        Args:
            signal: The input signal.
            cutoffs: The lower and higher cut-off frequencies. Must be specified in this exact order.
            fs: The input signals' sample rate.
            order: (optional) The order of the filter.

        Returns:
            The filtered input signal.
    """

    if cutoffs[1] < cutoffs[0]:
        raise ValueError('The highcut frequency cannot be lower than lowcut.')

    nyquist_freq = 0.5 * fs
    normalized_lowcut = cutoffs[0] / nyquist_freq
    normalized_highcut = cutoffs[1] / nyquist_freq

    sos_filter = butter(order, (normalized_lowcut, normalized_highcut), btype='band', analog=False, output='sos')

    return sosfilt(sos_filter, signal)


def main():
    # Take slice
    N = 8192
    win = np.hamming(N)

    fs, signal = wf.read('../examples/16-bit-signed-mono.wav')
    filtered_signal = bandpass_filter(signal, highs, fs)
    frequencies, dbfs_amp = dbfs_rfft(filtered_signal[0:N], fs, win)
    plot_dbfs(frequencies, dbfs_amp)
    wf.write('./examples/rawr.wav', fs, filtered_signal)


if __name__ == "__main__":
    main()
