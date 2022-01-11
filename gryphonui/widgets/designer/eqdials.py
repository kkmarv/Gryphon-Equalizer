from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class EQDials(QWidget):
    def __init__(self):
        super().__init__()
        self.dial_1, self.dial_2, self.dial_3, self.dial_4, self.dial_5 = None, None, None, None, None
        self.dial_6, self.dial_7, self.dial_8, self.dial_9, self.dial_10 = None, None, None, None, None

        uic.loadUi('assets/dial_widget.ui', self)  # load in those dials

    def reset_dials(self):
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
