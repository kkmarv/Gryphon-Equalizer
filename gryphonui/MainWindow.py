import os
import sys
import ctypes
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from button_widget import ButtonWidget
from top_window import TopWindow

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # for taskbar icon bShrug
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.setWindowTitle("Any Jammers In Chat?")
        self.setWindowIcon(QtGui.QIcon('resources/pepe_jam.png'))
        self.first_play = True
        self.paused = False
        self.topwindow = TopWindow()
        self.buttons = ButtonWidget()
        self.connect_buttons()
        self.init_gui()
        self.setFixedSize(960, 540)


    def init_gui(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        layout = QVBoxLayout()
        self.centralwidget.setLayout(layout)
        layout.addWidget(self.topwindow)
        layout.addWidget(self.buttons)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen_wav_File = QtWidgets.QWidgetAction(self)
        self.actionOpen_wav_File.setObjectName("actionOpen_wav_File")
        self.actionClose = QtWidgets.QWidgetAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QWidgetAction(self)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen_wav_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # connect action context menu buttons
        self.actionOpen_wav_File.triggered.connect(lambda: None)     # read file todo
        self.actionSave.triggered.connect(lambda: None)            # save file todo
        self.actionClose.triggered.connect(lambda: quit())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Equalizer"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_wav_File.setText(_translate("MainWindow", "Open wav File"))
        self.actionOpen_wav_File.setStatusTip(_translate("MainWindow", "Open a wav File you want to modify"))
        self.actionOpen_wav_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Exit the Program"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionSave.setText(_translate("MainWindow", "Save as wav File"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save your modified wav File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def connect_buttons(self):
        self.buttons.PlayPauseButton.clicked.connect(lambda: self.play_pause())
        self.buttons.ResetDialsButton.clicked.connect(lambda: self.topwindow.dials.reset_dials())

        self.topwindow.dials.dial_1.valueChanged.connect(lambda: self.topwindow.dials.value_1.setText(
            str(self.topwindow.dials.dial_1.value()) + " dB"))
        self.topwindow.dials.dial_2.valueChanged.connect(lambda: self.topwindow.dials.value_2.setText(
            str(self.topwindow.dials.dial_2.value()) + " dB"))
        self.topwindow.dials.dial_3.valueChanged.connect(lambda: self.topwindow.dials.value_3.setText(
            str(self.topwindow.dials.dial_3.value()) + " dB"))
        self.topwindow.dials.dial_4.valueChanged.connect(lambda: self.topwindow.dials.value_4.setText(
            str(self.topwindow.dials.dial_4.value()) + " dB"))
        self.topwindow.dials.dial_5.valueChanged.connect(lambda: self.topwindow.dials.value_5.setText(
            str(self.topwindow.dials.dial_5.value()) + " dB"))
        self.topwindow.dials.dial_6.valueChanged.connect(lambda: self.topwindow.dials.value_6.setText(
            str(self.topwindow.dials.dial_6.value()) + " dB"))
        self.topwindow.dials.dial_7.valueChanged.connect(lambda: self.topwindow.dials.value_7.setText(
            str(self.topwindow.dials.dial_7.value()) + " dB"))
        self.topwindow.dials.dial_8.valueChanged.connect(lambda: self.topwindow.dials.value_8.setText(
            str(self.topwindow.dials.dial_8.value()) + " dB"))
        self.topwindow.dials.dial_9.valueChanged.connect(lambda: self.topwindow.dials.value_9.setText(
            str(self.topwindow.dials.dial_9.value()) + " dB"))
        self.topwindow.dials.dial_10.valueChanged.connect(lambda: self.topwindow.dials.value_10.setText(
            str(self.topwindow.dials.dial_10.value()) + " dB"))

    #### MUSIC play pepeg stuff
    #
    # class Worker(QObject):
    #     finished = pyqtSignal()
    #     progress = pyqtSignal(int)
    #
    #     def run(self):
    #         """Long-running task."""
    #         for i in range(5):
    #             sys.sleep(1)
    #             self.progress.emit(i + 1)
    #         self.finished.emit()
    #
    #
    # def toggle_btn(self):
    #     if self.buttons.PlayPauseButton.text() == "Pause":
    #         self.buttons.PlayPauseButton.setText("Play")
    #     else:
    #         self.buttons.PlayPauseButton.setText("Pause")
    #
    # def check_event(self):
    #     for event in pygame.event.get():
    #         if event.type == self.MUSIC_END:
    #             self.toggle_btn()
    #             print('music end event')
    #
    # def play_pause(self):
    #     if mixer.get_init():
    #         # first play
    #         if self.first_play and mixer.music:
    #             self.thread = QThread()
    #             self.worker = Worker()
    #             self.worker.moveToThread(self.thread)
    #
    #             self.thread.started.connect(self.worker.run)
    #             self.worker.finished.connect(self.thread.quit)
    #             self.worker.finished.connect(self.worker.deleteLater)
    #             self.thread.finished.connect(self.thread.deleteLater)
    #             self.worker.progress.connect(self.reportProgress)
    #
    #             self.thread.start()
    #             self.toggle_btn()
    #             mixer.music.play()
    #             self.first_play = False
    #             # self.thread.finished.connect(
    #             #     lambda: self.toggle_btn()
    #             # )
    #             self.thread.finished.connect(
    #                 lambda: self.stop_stream()
    #             )
    #         # pause
    #         elif not self.paused and pygame.mixer.music.get_busy():
    #             self.toggle_btn()
    #             mixer.music.pause()
    #             self.paused = True
    #         # unpause
    #         elif self.paused or pygame.mixer.music.get_busy():
    #             self.toggle_btn()
    #             mixer.music.unpause()
    #             mixer.music.set_endevent()
    #             self.paused = False
    #         # restart
    #         else:
    #             self.toggle_btn()
    #             mixer.music.rewind()
    #             mixer.music.play()
    #     else:
    #         print("you need to load a wave file first")
    #
        ###


def create_gui_window():
    app = QApplication([])
    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing...")


if __name__ == '__main__':
    create_gui_window()
