import matplotlib

from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


matplotlib.use('QtAgg')


class EQCanvas(FigureCanvasQTAgg):
    """Matplotlib canvas for displaying the equalizer plot."""

    def __init__(self, initial_x_values, initial_y_values, width=6.4, height=4.8, dpi=100):
        self._figure: Figure = Figure(figsize=(width, height), dpi=dpi)
        self._figure.set_canvas(self)

        super(EQCanvas, self).__init__(self._figure)

        self._axes: Axes = self._figure.add_subplot()
        self.plot: Line2D = self._axes.plot(initial_x_values, initial_y_values)[0]

    def update_y_values(self, y_values) -> None:
        self.plot.set_ydata(y_values)
        self.draw()

    def __del__(self) -> None:
        matplotlib.pyplot.close(self._figure)
