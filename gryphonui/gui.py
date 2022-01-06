import os
import sys
import ctypes
import pyaudio
import pygame
from pygame import mixer
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        for i in range(5):
            sys.sleep(1)
            self.progress.emit(i + 1)
        self.finished.emit()


class EqualizerGui(QMainWindow):
    def __init__(self):
        super(EqualizerGui, self).__init__()

        # for taskbar icon bShrug
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.setWindowTitle("Any Jammers In Chat?")
        self.setWindowIcon(QtGui.QIcon('pepe_jam.png'))
        self.resize(960, 540)
        self.first_play = True
        self.paused = False

        self.p = None
        self.stream = None
        self.stop_stream = False

        self.equalizer = None   # TODO give path to file and get signal

        self.init_gui()
        #self.setFixedSize(self.layout.sizeHint())
        self.layout().sizeHint()
        #self.centerscreen()
        self.sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.dial_1.setSizePolicy(self.sizePolicy)
        self.show()


    def init_gui(self):
        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("Kool Keppa Kleb")
        # self.label.move(self.width()//2, self.height()//2)
        #
        # self.b1 = QtWidgets.QPushButton(self)
        # self.b1.setText("Gligg de belle")
        # self.b1.clicked.connect(self.clicked)
        self.setObjectName("self")
        self.setEnabled(True)
        #self.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(960, 540))
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.playPauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.playPauseButton.setGeometry(QtCore.QRect(290, 340, 51, 51))
        self.playPauseButton.setObjectName("playPauseButton")
        self.playPauseButton.setText("Play")
        self.playPauseButton.clicked.connect(lambda: self.play_pause())

        self.resetDials = QtWidgets.QPushButton(self.centralwidget)
        self.resetDials.setGeometry(QtCore.QRect(390, 340, 51, 51))
        self.resetDials.setObjectName("resetDialsButton")
        self.resetDials.setText("Reset")
        self.resetDials.clicked.connect(lambda: self.resetDials())

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(640, 130, 47, 14))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 130, 47, 14))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 130, 47, 14))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 130, 47, 14))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(880, 130, 47, 14))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 260, 47, 14))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 260, 47, 14))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(760, 260, 47, 14))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(820, 260, 47, 14))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(880, 260, 47, 14))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.dial_1 = QtWidgets.QDial(self.centralwidget)
        self.dial_1.setGeometry(QtCore.QRect(640, 150, 50, 64))
        self.dial_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_1.setMinimum(-18)
        self.dial_1.setMaximum(18)
        self.dial_1.setProperty("value", 0)
        self.dial_1.setNotchesVisible(True)
        self.dial_1.setObjectName("dial_1")
        self.dial_1.valueChanged.connect(lambda: self.value_1.setText(str(self.dial_1.value()) + " dB"))

        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(700, 150, 50, 64))
        self.dial_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_2.setMinimum(-18)
        self.dial_2.setMaximum(18)
        self.dial_2.setProperty("value", 0)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName("dial_2")
        self.dial_2.valueChanged.connect(lambda: self.value_2.setText(str(self.dial_2.value()) + " dB"))

        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(760, 150, 50, 64))
        self.dial_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_3.setMinimum(-18)
        self.dial_3.setMaximum(18)
        self.dial_3.setProperty("value", 0)
        self.dial_3.setNotchesVisible(True)
        self.dial_3.setObjectName("dial_3")
        self.dial_3.valueChanged.connect(lambda: self.value_3.setText(str(self.dial_3.value()) + " dB"))

        self.dial_4 = QtWidgets.QDial(self.centralwidget)
        self.dial_4.setGeometry(QtCore.QRect(820, 150, 50, 64))
        self.dial_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_4.setMinimum(-18)
        self.dial_4.setMaximum(18)
        self.dial_4.setProperty("value", 0)
        self.dial_4.setNotchesVisible(True)
        self.dial_4.setObjectName("dial_4")
        self.dial_4.valueChanged.connect(lambda: self.value_4.setText(str(self.dial_4.value()) + " dB"))

        self.dial_5 = QtWidgets.QDial(self.centralwidget)
        self.dial_5.setGeometry(QtCore.QRect(880, 150, 50, 64))
        self.dial_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_5.setMinimum(-18)
        self.dial_5.setMaximum(18)
        self.dial_5.setProperty("value", 0)
        self.dial_5.setNotchesVisible(True)
        self.dial_5.setObjectName("dial_5")
        self.dial_5.valueChanged.connect(lambda: self.value_5.setText(str(self.dial_5.value()) + " dB"))

        self.dial_6 = QtWidgets.QDial(self.centralwidget)
        self.dial_6.setGeometry(QtCore.QRect(640, 280, 50, 64))
        self.dial_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_6.setMinimum(-18)
        self.dial_6.setMaximum(18)
        self.dial_6.setProperty("value", 0)
        self.dial_6.setNotchesVisible(True)
        self.dial_6.setObjectName("dial_6")
        self.dial_6.valueChanged.connect(lambda: self.value_6.setText(str(self.dial_6.value()) + " dB"))

        self.dial_7 = QtWidgets.QDial(self.centralwidget)
        self.dial_7.setGeometry(QtCore.QRect(700, 280, 50, 64))
        self.dial_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_7.setMinimum(-18)
        self.dial_7.setMaximum(18)
        self.dial_7.setProperty("value", 0)
        self.dial_7.setNotchesVisible(True)
        self.dial_7.setObjectName("dial_7")
        self.dial_7.valueChanged.connect(lambda: self.value_7.setText(str(self.dial_7.value()) + " dB"))

        self.dial_8 = QtWidgets.QDial(self.centralwidget)
        self.dial_8.setGeometry(QtCore.QRect(760, 280, 50, 64))
        self.dial_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_8.setMinimum(-18)
        self.dial_8.setMaximum(18)
        self.dial_8.setProperty("value", 0)
        self.dial_8.setNotchesVisible(True)
        self.dial_8.setObjectName("dial_8")
        self.dial_8.valueChanged.connect(lambda: self.value_8.setText(str(self.dial_8.value()) + " dB"))

        self.dial_9 = QtWidgets.QDial(self.centralwidget)
        self.dial_9.setGeometry(QtCore.QRect(820, 280, 50, 64))
        self.dial_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_9.setMinimum(-18)
        self.dial_9.setMaximum(18)
        self.dial_9.setProperty("value", 0)
        self.dial_9.setNotchesVisible(True)
        self.dial_9.setObjectName("dial_9")
        self.dial_9.valueChanged.connect(lambda: self.value_9.setText(str(self.dial_9.value()) + " dB"))

        self.dial_10 = QtWidgets.QDial(self.centralwidget)
        self.dial_10.setGeometry(QtCore.QRect(880, 280, 50, 64))
        self.dial_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_10.setMinimum(-18)
        self.dial_10.setMaximum(18)
        self.dial_10.setProperty("value", 0)
        self.dial_10.setNotchesVisible(True)
        self.dial_10.setObjectName("dial_10")
        self.dial_10.valueChanged.connect(lambda: self.value_10.setText(str(self.dial_10.value()) + " dB"))

        self.value_1 = QtWidgets.QLabel(self.centralwidget)
        self.value_1.setGeometry(QtCore.QRect(640, 220, 47, 14))
        self.value_1.setAlignment(QtCore.Qt.AlignCenter)
        self.value_1.setObjectName("value_1")
        self.value_2 = QtWidgets.QLabel(self.centralwidget)
        self.value_2.setGeometry(QtCore.QRect(700, 220, 47, 14))
        self.value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.value_2.setObjectName("value_2")
        self.value_3 = QtWidgets.QLabel(self.centralwidget)
        self.value_3.setGeometry(QtCore.QRect(760, 220, 47, 14))
        self.value_3.setAlignment(QtCore.Qt.AlignCenter)
        self.value_3.setObjectName("value_3")
        self.value_4 = QtWidgets.QLabel(self.centralwidget)
        self.value_4.setGeometry(QtCore.QRect(820, 220, 47, 14))
        self.value_4.setAlignment(QtCore.Qt.AlignCenter)
        self.value_4.setObjectName("value_4")
        self.value_5 = QtWidgets.QLabel(self.centralwidget)
        self.value_5.setGeometry(QtCore.QRect(880, 220, 47, 14))
        self.value_5.setAlignment(QtCore.Qt.AlignCenter)
        self.value_5.setObjectName("value_5")
        self.value_6 = QtWidgets.QLabel(self.centralwidget)
        self.value_6.setGeometry(QtCore.QRect(640, 350, 47, 14))
        self.value_6.setAlignment(QtCore.Qt.AlignCenter)
        self.value_6.setObjectName("value_6")
        self.value_7 = QtWidgets.QLabel(self.centralwidget)
        self.value_7.setGeometry(QtCore.QRect(700, 350, 47, 14))
        self.value_7.setAlignment(QtCore.Qt.AlignCenter)
        self.value_7.setObjectName("value_7")
        self.value_8 = QtWidgets.QLabel(self.centralwidget)
        self.value_8.setGeometry(QtCore.QRect(760, 350, 47, 14))
        self.value_8.setAlignment(QtCore.Qt.AlignCenter)
        self.value_8.setObjectName("value_8")
        self.value_9 = QtWidgets.QLabel(self.centralwidget)
        self.value_9.setGeometry(QtCore.QRect(820, 350, 47, 14))
        self.value_9.setAlignment(QtCore.Qt.AlignCenter)
        self.value_9.setObjectName("value_9")
        self.value_10 = QtWidgets.QLabel(self.centralwidget)
        self.value_10.setGeometry(QtCore.QRect(880, 350, 47, 14))
        self.value_10.setAlignment(QtCore.Qt.AlignCenter)
        self.value_10.setObjectName("value_10")

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
        self.actionOpen_wav_File = QtWidgets.QAction(self)
        self.actionOpen_wav_File.setObjectName("actionOpen_wav_File")
        self.actionOpen_Microphone_Stream = QtWidgets.QAction(self)
        self.actionOpen_Microphone_Stream.setObjectName("actionOpen_Microphone_Stream")
        self.actionEnd_Microphone_Stream = QtWidgets.QAction(self)
        self.actionEnd_Microphone_Stream.setObjectName("actionEnd_Microphone_Stream")
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen_wav_File)
        self.menuFile.addAction(self.actionOpen_Microphone_Stream)
        self.menuFile.addAction(self.actionEnd_Microphone_Stream)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)

        # connect action context menu buttons
        self.actionOpen_wav_File.triggered.connect(lambda: self.action_openwav())
        self.actionOpen_Microphone_Stream.triggered.connect(lambda: self.action_openmic())
        self.actionEnd_Microphone_Stream.triggered.connect(lambda: self.stop_stream(self.stream, self.p))
        self.actionSave.triggered.connect(lambda: self.action_savewav())
        self.actionClose.triggered.connect(lambda: self.action_exit())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Equalizer"))

        #self.pushButton.setText(_translate("MainWindow", "Play"))

        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "9"))
        self.label_10.setText(_translate("MainWindow", "10"))
        self.value_2.setText(_translate("MainWindow", "0 dB"))
        self.value_1.setText(_translate("MainWindow", "0 dB"))
        self.value_3.setText(_translate("MainWindow", "0 dB"))
        self.value_4.setText(_translate("MainWindow", "0 dB"))
        self.value_5.setText(_translate("MainWindow", "0 dB"))
        self.value_10.setText(_translate("MainWindow", "0 dB"))
        self.value_7.setText(_translate("MainWindow", "0 dB"))
        self.value_8.setText(_translate("MainWindow", "0 dB"))
        self.value_9.setText(_translate("MainWindow", "0 dB"))
        self.value_6.setText(_translate("MainWindow", "0 dB"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_wav_File.setText(_translate("MainWindow", "Open .wav File"))
        self.actionOpen_wav_File.setStatusTip(_translate("MainWindow", "Open a .wav File you want to modify"))
        self.actionOpen_wav_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_Microphone_Stream.setText(_translate("MainWindow", "Open Mic Stream"))
        self.actionOpen_Microphone_Stream.setStatusTip(_translate("MainWindow", "Open a sound stream from your microphone"))
        self.actionOpen_Microphone_Stream.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionEnd_Microphone_Stream.setText(_translate("MainWindow", "End Mic Stream"))
        self.actionEnd_Microphone_Stream.setStatusTip(_translate("MainWindow", "Ends the sound stream from your microphone"))
        self.actionEnd_Microphone_Stream.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Exit the Program"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionSave.setText(_translate("MainWindow", "Save as .wav File"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save your modified .wav File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def resetDials(self):
        self.dial_1.setValue(0)
        self.dial_2.setValue(0)
        self.dial_3.setValue(0)
        self.dial_4.setValue(0)
        self.dial_5.setValue(0)
        self.dial_6.setValue(0)
        self.dial_7.setValue(0)
        self.dial_8.setValue(0)
        self.dial_9.setValue(0)
        self.dial_10.setValue(0)


    def toggle_btn(self):
        if self.playPauseButton.text() == "Pause":
            self.playPauseButton.setText("Play")
        else:
            self.playPauseButton.setText("Pause")

    def check_event(self):
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                self.toggle_btn()
                print('music end event')

    def play_pause(self):
        if mixer.get_init():
            # first play
            if self.first_play and mixer.music:
                self.thread = QThread()
                self.worker = Worker()
                self.worker.moveToThread(self.thread)

                self.thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                #self.worker.progress.connect(self.reportProgress)

                self.thread.start()
                self.toggle_btn()
                mixer.music.play()
                self.first_play = False
                # self.thread.finished.connect(
                #     lambda: self.toggle_btn()
                # )
                self.thread.finished.connect(
                    lambda: self.stop_stream()
                )
            # pause
            elif not self.paused and pygame.mixer.music.get_busy():
                self.toggle_btn()
                mixer.music.pause()
                self.paused = True
            # unpause
            elif self.paused or pygame.mixer.music.get_busy():
                self.toggle_btn()
                mixer.music.unpause()
                mixer.music.set_endevent()
                self.paused = False
            # restart
            else:
                self.toggle_btn()
                mixer.music.rewind()
                mixer.music.play()
        else:
            print("you need to load a wave file first")

        ### change to play when finished

    def clicked(self, text='fenk ju you fucking retard'):
        self.label.setText(text)
        self.update()

    def action_openwav(self):
        pygame.init()
        mixer.init()
        # self.MUSIC_END = pygame.USEREVENT + 1
        # pygame.mixer.music.set_endevent(self.MUSIC_END)

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open .wav Audio File", os.environ['USERPROFILE'] + "\Music\sounds",
                                                  "Wave Files (*.wav)", options=options)
        with open(fileName) as file:
            mixer.music.load(fileName)

    def stop_stream(self):
        print("ENDE")

    def action_openmic(self):
        ###
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.thread.finished.connect(
            lambda: self.stop_stream()
        )
        ###
        # TODO

        chunk = 1024
        width = 2
        channels = 1
        rate = 44100
        record_seconds = 10

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(width),
                        channels=channels,
                        rate=rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)

        print("> playback started")

        while not self.stop_stream:
            data = stream.read(chunk)
            stream.write(data, chunk)
            if self.stop_stream:
                print("STOPPT DEN STRIMMMMM!")
        print("STOPPT DEN STRIMMMMM!")

        #self.stop_stream(p, stream)

        print("> playback done")

        #stream.stop_stream()
        #stream.close()

        #p.terminate()


    def action_savewav(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save as .wav Audio File", "",
                                                  "Wave Files (*.wav)", options=options)
        print(fileName)

    def action_exit(self):
        quit()


    def update(self):
        self.b1.adjustSize()
        self.label.adjustSize()


def create_window():
    app = QApplication(sys.argv)
    res = app.desktop().screenGeometry()
    gui = EqualizerGui()
    width, height = res.width() // 2, res.height() // 2
    x_pos, y_pos = res.width() // 4, res.height() // 4
    gui.setGeometry(x_pos, y_pos, width, height)
    gui.setFixedSize(width, height)

    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    create_window()

### TODO
# > resizable elements & window initialized with right isze
# > (mic stream)
# > reset dial values
# > use dial values for plot (kek)