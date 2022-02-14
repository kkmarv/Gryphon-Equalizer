import os
import ctypes

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMenuBar
from typing import Union

from src.equalpyzer.wavefile import WaveFile
from src.equalpyzer.equalizer import Equalizer
from src.gryphonui.widgets.eqwidget import EQWidget
from src.gryphonui.widgets.eqmenubar import EQMenuBar
from src.gryphonui.widgets.designer.eq_control_buttons import EQControlButtons


APP_ID: str = 'wer.das.liest.ist.toni.oder.eben.nich'
ICON_PATH: str = 'gryphonui/widgets/designer/assets/pepe_jam.png'
WINDOW_TITLE: str = 'Gryphon Equalizer'


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        app_id = APP_ID
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        # attribute declarations
        self._eq: Union[Equalizer, None] = None
        self._canvas_view_mode: str = 'frequency-db'
        self._eq_control_buttons: EQControlButtons = EQControlButtons()
        self._eq_widget: EQWidget = EQWidget(
            lambda db_boost, low_cut, high_cut: self.__on_dial_change(db_boost, low_cut, high_cut)
        )

        self.__init_gui()

    def __init_gui(self) -> None:
        """Initialize GUI components"""

        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self.setFixedSize(960, 540)
        self.setMenuBar(EQMenuBar(self))
        self.setCentralWidget(QWidget())

        layout = QVBoxLayout()
        layout.addWidget(self._eq_widget)
        layout.addWidget(self._eq_control_buttons)
        self.centralWidget().setLayout(layout)

        self.__connect_buttons()
        self.__connect_menu_bar_methods()

        self.show()
        self.__on_open()

    def __connect_menu_bar_methods(self) -> None:  # TODO outsource further
        menu_bar: Union[EQMenuBar, QMenuBar] = self.menuBar()
        menu_bar.open_file_action.triggered.connect(lambda: self.__on_open())
        menu_bar.save_file_action.triggered.connect(lambda: self.__on_save())
        menu_bar.exit_app_action.triggered.connect(lambda: self.__on_exit())
        menu_bar.copy_content_action.triggered.connect(lambda: None)
        menu_bar.paste_content_action.triggered.connect(lambda: None)
        menu_bar.change_view_to_time_action.triggered.connect(lambda: self.__update_plot('time'))
        menu_bar.change_view_to_freq_action.triggered.connect(lambda: self.__update_plot('frequency'))
        menu_bar.change_view_to_freqdb_action.triggered.connect(lambda: self.__update_plot('frequency-db'))

    def __connect_buttons(self) -> None:
        self._eq_control_buttons.ResetDialsButton.clicked.connect(lambda: self._eq_widget.eq_dials.__reset_dials())

    def __on_open(self) -> None:  # TODO user must always select a file, prevent him from closing the dialog somehow
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Wave Audio File",
            os.environ['USERPROFILE'],
            "Wave Files (*.wav)"
        )

        if len(file_path) != 0:
            self._eq = Equalizer(WaveFile(file_path))
            self.__update_plot(self._canvas_view_mode)

    def __on_save(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save as Wave Audio File',
            os.environ['USERPROFILE'] + r'\Desktop',
            "Wave Files (*.wav)"
        )
        if len(file_path) != 0:
            self._eq.wav.save_signal(file_path, self._eq.altered_signal)

    def __on_dial_change(self, db_boost: int, low_cut: int, high_cut: int) -> None:
        self._eq.boost(db_boost, low_cut, high_cut)
        self.__update_plot(self._canvas_view_mode)

    @staticmethod
    def __on_exit() -> None:
        exit()

    def __update_plot(self, view_mode, normalize=True) -> None:
        if view_mode == 'time':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_time_domain(
                self._eq.wav.input_signal,
                self._eq.wav.duration,
                self._eq.wav.num_of_samples,
                self._eq.wav.loudest_samp_value,
                normalize=normalize
            )

        elif view_mode == 'frequency':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_freq_domain(
                self._eq.wav.frequencies,
                self._eq.altered_amplitudes,
                normalize=normalize
            )

        elif view_mode == 'frequency-db':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_freq_domain_db(
                self._eq.wav.frequencies,
                self._eq.altered_amplitudes_db
            )

        else:
            raise ValueError(f'Mode {view_mode} is not recognized.')
