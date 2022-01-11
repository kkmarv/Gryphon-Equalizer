from PyQt6.QtWidgets import QWidget, QHBoxLayout
from gryphonui.dial_widget import DialWidget
from eqcanvas import EQCanvas


class TopWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.canvas = EQCanvas()
        self.dials = DialWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.dials)
        self.setLayout(layout)
