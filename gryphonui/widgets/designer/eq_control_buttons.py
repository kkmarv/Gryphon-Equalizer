from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class EQControlButtons(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('assets/button_widget.ui', self)  # load in the buttons
