from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class DialWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/dial_widget.ui', self)


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
