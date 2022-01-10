from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class ButtonWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('button_widget.ui', self)
        self.show()
