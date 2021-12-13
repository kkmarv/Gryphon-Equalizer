import numpy as np
import scipy.io.wavfile as wf

from numpy import ndarray
from scipy.signal import butter
from scipy.signal.signaltools import sosfilt

from typing import Tuple
from equalizer import dbfs_rfft, plot_dbfs
from matplotlib import pyplot as plt


# cut-offs for 10 bandpass filters
super_lows = (1, 31)
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


def bandpass_10band_filter(signal: ndarray, fs: int,
                           gain1: float = 1, gain2: float = 1, gain3: float = 1, gain4: float = 1, gain5: float = 1,
                           gain6: float = 1, gain7: float = 1, gain8: float = 1, gain9: float = 1, gain10: float = 1):
    band1 = bandpass_filter(signal, super_lows, fs) * gain1
    band2 = bandpass_filter(signal, lows, fs) * gain2
    band3 = bandpass_filter(signal, higher_lows, fs) * gain3
    band4 = bandpass_filter(signal, lower_mids, fs) * gain4
    band5 = bandpass_filter(signal, mids, fs) * gain5
    band6 = bandpass_filter(signal, higher_mids, fs) * gain6
    band7 = bandpass_filter(signal, lower_highs, fs) * gain7
    band8 = bandpass_filter(signal, highs, fs) * gain8
    band9 = bandpass_filter(signal, super_highs, fs) * gain9
    # band10 = bandpass_filter(signal, ultra_highs, fs) * gain10

    return band1 + band2 + band3 + band4 + band5 + band6 + band7 + band8 + band9  # + band10


def main():
    fs, signal = wf.read('../examples/16-bit-signed-mono.wav')

    freq_vector, amp_vector = dbfs_rfft(signal, fs)
    plot_dbfs(freq_vector, amp_vector)

    # filtered_signal = bandpass_filter(signal, (1, 1000), fs)
    filtered_signal = bandpass_10band_filter(signal, fs)

    frequencies, dbfs_amp = dbfs_rfft(filtered_signal[0:N], fs, win)
    plot_dbfs(frequencies, dbfs_amp)

    wf.write('irfft.wav', fs, np.fft.irfft(signal))


if __name__ == "__main__":
    main()
