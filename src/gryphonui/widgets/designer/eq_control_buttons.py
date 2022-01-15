from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


BUTTON_UI_FILE_PATH_PATH: str = 'gryphonui/widgets/designer/assets/button_widget.ui'


class EQControlButtons(QWidget):
    def __init__(self):
        super().__init__()

        # load buttons from ui designer file
        uic.loadUi(BUTTON_UI_FILE_PATH_PATH, self)
