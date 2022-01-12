import matplotlib
import numpy as np

from numpy import ndarray
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


matplotlib.use('QtAgg')


class EQCanvas(FigureCanvasQTAgg):
    """Matplotlib canvas as a QWidget. It displays the equalizer plot."""

    def __init__(self, width=6.4, height=4.8, dpi=100):
        # create figure and axes
        self._figure: Figure = Figure(figsize=(width, height), dpi=dpi, facecolor='#f0f0f0')
        self._axes: Axes = self._figure.add_subplot()

        super(EQCanvas, self).__init__(self._figure)
        self._figure.set_canvas(self)  # set this class as the figure's canvas

        # frequency labels for logarithmic x axis scaling
        self._X_TICKS: ndarray = np.asarray([20, 31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000])
        self._X_LABELS: ndarray = np.asarray(['20', '31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k'])

    def plot_time_domain(self, input_signal: ndarray, duration: float, num_of_samples: int, max_sample_value: int,
                         normalize=True) -> None:
        x_values: ndarray = np.linspace(start=0, stop=duration, num=num_of_samples)  # calculate the sampling on x axis
        y_values: ndarray = input_signal / max_sample_value if normalize else input_signal  # normalize values to [-1, 1]

        self._figure.tight_layout()      # prevent cut-off of text on labels

        axes: Axes = self._axes
        axes.clear()

        # plot graph and set visual parameters
        axes.plot(x_values, y_values)
        axes.set_xlim(left=0, right=duration)
        axes.set_ylim(top=1, bottom=-1) if normalize else None
        axes.set_xlabel('Time [sec]')
        axes.set_ylabel('Amplitude')
        axes.grid(True)
        axes.set_axisbelow(True)

        self.draw()  # draw the graph

    # TODO remove minor ticks in freq domain graph
    def plot_freq_domain(self, frequencies: ndarray, amplitudes: ndarray, normalize=True) -> None:
        x_values: ndarray = frequencies
        y_values: ndarray = amplitudes / np.max(amplitudes) if normalize else amplitudes  # normalize values to [-1, 1]

        self._figure.tight_layout()     # prevent cut-off of text on labels

        axes: Axes = self._axes
        axes.clear()

        # plot graph and set visual parameters
        axes.plot(x_values, y_values)
        axes.set_xscale('log')
        axes.set_xticks(self._X_TICKS, self._X_LABELS)
        axes.set_xlim(left=20, right=20000)
        axes.set_ylim(top=1, bottom=-1) if normalize else None
        axes.set_xlabel('Frequency [Hz]')
        axes.set_ylabel('Amplitude')
        axes.grid(True)
        axes.set_axisbelow(True)
        axes.tick_params(which='minor', bottom=False)

        self.draw()  # draw the graph

    # TODO remove minor ticks in freq domain db graph
    def plot_freq_domain_db(self, frequencies: ndarray, amplitudes_db: ndarray) -> None:
        x_values: ndarray = frequencies
        y_values: ndarray = amplitudes_db

        axes: Axes = self._axes
        axes.clear()

        # plot graph and set visual parameters
        axes.plot(x_values, y_values)
        axes.set_xscale('log')
        axes.set_xticks(self._X_TICKS, self._X_LABELS)
        axes.set_xlim(left=20, right=20000)
        axes.set_ylim(top=0, bottom=-90)
        axes.set_xlabel('Frequency [Hz]')
        axes.set_ylabel('Amplitude [dBFS]')
        axes.fill_between(x_values, y_values, -90)
        axes.grid(True)
        axes.set_axisbelow(True)
        axes.tick_params(which='minor', bottom=False)

        self.draw()  # draw the graph
