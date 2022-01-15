from PyQt6.QtWidgets import QWidget, QHBoxLayout

from src.gryphonui.widgets.eqcanvas import EQCanvas
from src.gryphonui.widgets.designer.eqdials import EQDials


class EQWidget(QWidget):
    def __init__(self, function, parent=None):  # TODO rename function to match EQs' amplify
        super().__init__(parent)
        self.eq_dials = EQDials(function=function)
        self.eq_canvas = EQCanvas()

        layout = QHBoxLayout()
        layout.addWidget(self.eq_canvas)
        layout.addWidget(self.eq_dials)
        self.setLayout(layout)
