from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


BUTTON_UI_FILE_PATH_PATH: str = 'gryphonui/widgets/designer/assets/button_widget.ui'


class EQControlButtons(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(BUTTON_UI_FILE_PATH_PATH, self)  # load in the buttons
