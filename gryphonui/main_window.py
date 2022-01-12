import os
import sys
import ctypes

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMenuBar
from typing import Union

from equalpyzer.equalizer import Equalizer
from equalpyzer.wavfile import Wavfile
from gryphonui.widgets.designer.eq_control_buttons import EQControlButtons
from gryphonui.widgets.eqmenubar import EQMenuBar
from gryphonui.widgets.main_widget import EQWidget


# prevent downscaling when moving between monitors of different resolutions, may not be working
# os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        app_id = 'hallo.du.bist.doof'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        # attribute declarations
        self._eq_widget: EQWidget = EQWidget()
        self._eq_control_buttons: EQControlButtons = EQControlButtons()
        self._eq: Union[Equalizer, None] = None
        self._canvas_view_mode: str = 'frequency-db'

        self.init_gui()

    def init_gui(self):
        """Initialize GUI components"""
        self.setWindowTitle("Gryphon Equalizer")
        self.setWindowIcon(QtGui.QIcon('assets/pepe_jam.png'))
        self.setFixedSize(960, 540)
        self.setMenuBar(EQMenuBar(self))
        self.setCentralWidget(QWidget())

        layout = QVBoxLayout()
        layout.addWidget(self._eq_widget)
        layout.addWidget(self._eq_control_buttons)
        self.centralWidget().setLayout(layout)

        self.connect_buttons()
        self.connect_menu_bar_methods()

        self.show()

    def connect_menu_bar_methods(self) -> None:  # TODO outsource further
        menu_bar: Union[EQMenuBar, QMenuBar] = self.menuBar()
        menu_bar.open_file_action.triggered.connect(lambda: self.on_open())
        menu_bar.save_file_action.triggered.connect(lambda: self.on_save())
        menu_bar.exit_app_action.triggered.connect(lambda: self.on_exit())
        menu_bar.copy_content_action.triggered.connect(lambda: None)
        menu_bar.paste_content_action.triggered.connect(lambda: None)
        menu_bar.change_view_to_time_action.triggered.connect(lambda: self.update_plot('time'))
        menu_bar.change_view_to_freq_action.triggered.connect(lambda: self.update_plot('frequency'))
        menu_bar.change_view_to_freqdb_action.triggered.connect(lambda: self.update_plot('frequency-db'))

    def connect_buttons(self):  # TODO outsource further into own EQDial and EQPlayer class sonst pussy
        self._eq_control_buttons.PlayPauseButton.setEnabled(False)
        self._eq_control_buttons.ResetDialsButton.clicked.connect(lambda: self._eq_widget.eq_dials.reset_dials())

        self._eq_widget.eq_dials.dial_1.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_1.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_1.value(),
                    '+' if self._eq_widget.eq_dials.dial_1.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_2.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_2.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_2.value(),
                    '+' if self._eq_widget.eq_dials.dial_2.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_3.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_3.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_3.value(),
                    '+' if self._eq_widget.eq_dials.dial_3.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_4.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_4.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_4.value(),
                    '+' if self._eq_widget.eq_dials.dial_4.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_5.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_5.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_5.value(),
                    '+' if self._eq_widget.eq_dials.dial_5.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_6.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_6.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_6.value(),
                    '+' if self._eq_widget.eq_dials.dial_6.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_7.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_7.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_7.value(),
                    '+' if self._eq_widget.eq_dials.dial_7.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_8.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_8.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_8.value(),
                    '+' if self._eq_widget.eq_dials.dial_8.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_9.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_9.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_9.value(),
                    '+' if self._eq_widget.eq_dials.dial_9.value() > 0 else ' '
                )
            )
        )
        self._eq_widget.eq_dials.dial_10.valueChanged.connect(
            lambda: self._eq_widget.eq_dials.value_10.setText(
                '{0:{1}} dB'.format(
                    self._eq_widget.eq_dials.dial_10.value(),
                    '+' if self._eq_widget.eq_dials.dial_10.value() > 0 else ' '
                )
            )
        )

    def on_open(self) -> None:  # TODO user must always select a file, prevent him from closing the dialog somehow
        debug = r"/Documents/_wichtig/Hochschule/3. Semester/MSV/Projekt/gryphon-equalizer/examples"
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Wave Audio File",
            os.environ['USERPROFILE'] + debug,
            "Wave Files (*.wav)"
        )
        if len(file_name) != 0:
            self._wav = Wavfile(file_name)
            self._eq = Equalizer(self._wav)

            self.update_plot(self._canvas_view_mode)

    def on_save(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            'Save as Wave Audio File',
            os.environ['USERPROFILE'] + r'\Desktop',
            "Wave Files (*.wav)"
        )
        if len(file_name) != 0 and self._wav.input_signal is not None:
            self._eq.save_wavfile(file_name)

    @staticmethod
    def on_exit():
        exit()

    def update_plot(self, view_mode, normalize=True):
        if view_mode == 'time':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_time_domain(
                self._wav.input_signal,
                self._wav.duration,
                self._wav.num_of_samples,
                self._wav.max_sample_value,
                normalize=normalize
            )

        elif view_mode == 'frequency':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_freq_domain(
                self._eq.frequencies,
                self._eq.amplitudes,
                normalize=normalize
            )

        elif view_mode == 'frequency-db':
            self._canvas_view_mode = view_mode
            self._eq_widget.eq_canvas.plot_freq_domain_db(
                self._eq.frequencies,
                self._eq.amplitudes_db
            )

        else:
            raise ValueError(f'Mode {view_mode} is not recognized.')


def main():
    app = QApplication([])
    MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
