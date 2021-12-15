import numpy as np

from numpy import ndarray
from scipy.io import wavfile as wf
from matplotlib import pyplot as plt

from typing import Union


class Equalizer:
    def __init__(self):
        self._input_signal: Union[ndarray, None] = None
        self._sample_rate: Union[int, None] = None
        self._normalizer: Union[int, None] = None  # value of loudest sample in the signal

        self._amplitudes: Union[ndarray, None] = None
        self._frequencies: Union[ndarray, None] = None
        self._amplitudes_db: Union[ndarray, None] = None

        # frequency labels for logarithmic x axis
        self._x_ticks: ndarray = np.asarray([20, 31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000])
        self._x_labels: ndarray = np.asarray(['20', '31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k'])

    def load_signal(self, path: str) -> None:
        self._sample_rate, self._input_signal = wf.read(path)
        self._normalizer = np.max(self._input_signal)

    def save_signal(self, path: str) -> None:
        if self._amplitudes is None:  # if we did not fft the signal, just save it
            # this causes 24bit files to convert to 32bit files because numpy is missing 24bit data types
            wf.write(path, self._sample_rate, self._input_signal.astype(self._input_signal.dtype))
        else:
            output_signal: ndarray = np.fft.irfft(self.amplitudes)

            if isinstance(self._input_signal.dtype, np.integer):
                output_signal = np.round(output_signal)

            wf.write(path, self._sample_rate, output_signal.astype(self._input_signal.dtype))

    def amplify(self, gain: float, low_cut: int = 0, high_cut: Union[int, None] = None):
        if high_cut is None:
            high_cut = self.frequencies[-1]  # set to highest frequency in the signal
        if low_cut > high_cut:
            raise ValueError('Low-cut frequency cannot be higher than high-cut frequency!')

        self.amplitudes[(self.frequencies > low_cut) & (self.frequencies < high_cut)] *= gain
        self._amplitudes_db = None  # delete the old db scale

    def plot_time_domain(self) -> None:
        n: int = len(self._input_signal)  # number of samples
        sec: float = n / self._sample_rate  # length of signal in seconds

        y_values: ndarray = self._input_signal / self._normalizer  # normalize values to [-1, 1]
        x_values: ndarray = np.linspace(start=0, stop=sec, num=n)  # calculate the sampling on x axis

        # plot graph and set visual parameters
        plt.plot(x_values, y_values)
        plt.xlim(left=0, right=sec)
        plt.ylim(top=1, bottom=-1)
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_freq_domain(self) -> None:
        y_values: ndarray = self.amplitudes / np.max(self.amplitudes)  # normalize values to [-1, 1]
        x_values: ndarray = self.frequencies

        # plot graph and set visual parameters
        plt.plot(x_values, y_values)
        plt.xscale('log')
        plt.xticks(self._x_ticks, self._x_labels)
        plt.xlim(left=20, right=20000)
        plt.ylim(top=1, bottom=-1)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.show()

    def plot_freq_domain_db(self) -> None:
        y_values: ndarray = self.amplitudes_db
        x_values: ndarray = self.frequencies

        # plot graph and set visual parameters
        plt.plot(x_values, y_values)
        plt.grid(True)
        plt.xscale('log')
        plt.xticks(self._x_ticks, self._x_labels)
        plt.xlim(left=20, right=20000)
        plt.ylim(top=0, bottom=-90)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude [dBFS]')
        plt.fill_between(x_values, y_values, -90)
        plt.show()

    @property
    def amplitudes(self) -> ndarray:
        """Amplitudes from FFT"""
        if self._amplitudes is None:  # if we did not calculate the frequency domain yet
            self._amplitudes = np.fft.rfft(self._input_signal)
        return self._amplitudes

    @property
    def frequencies(self) -> ndarray:
        """Frequencies from FFT"""
        if self._frequencies is None:
            self._frequencies = np.fft.rfftfreq(self._input_signal.size, 1 / self._sample_rate)
        return self._frequencies

    @property
    def amplitudes_db(self) -> ndarray:
        """Amplitudes from FFT but with dBFS scaling"""
        if self._amplitudes_db is None:
            # scale the amplitude of the fft by a factor of 2,
            # because we are using only half of the fft spectrum
            # (and normalize it by the number of frequency samples) # TODO Is this wrong?
            scaled_freq_values = np.abs(self.amplitudes) * 2 / len(self.amplitudes)  # TODO abs() necessary?

            # convert to dBFS (decibels full scale)
            self._amplitudes_db = 20 * np.log10(scaled_freq_values / self._normalizer)

        return self._amplitudes_db


def main():
    a = '../examples/16-bit-signed-stereo.wav'
    b = '../examples/16-bit-signed-mono.wav'
    c = '../examples/24-bit-signed-stereo.wav'
    d = '../examples/24-bit-signed-mono.wav'
    e = '../examples/32-bit-float-stereo.wav'
    f = '../examples/32-bit-float-mono.wav'
    linda = '../examples/drumloop.wav'

    eq = Equalizer()
    eq.load_signal(f)

    eq.plot_time_domain()

    eq.plot_freq_domain()
    eq.plot_freq_domain_db()

    # eq.amplify(0, high_cut=100)
    # eq.amplify(0, low_cut=101)

    eq.plot_freq_domain()
    eq.plot_freq_domain_db()

    eq.save_signal('rawr.wav')


if __name__ == "__main__":
    main()
