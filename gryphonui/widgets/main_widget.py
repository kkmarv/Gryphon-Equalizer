from PyQt6.QtWidgets import QWidget, QHBoxLayout

from gryphonui.widgets.eqcanvas import EQCanvas
from gryphonui.widgets.designer.eqdials import EQDials


class EQWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.eq_dials = EQDials()
        self.eq_canvas = EQCanvas()

        layout = QHBoxLayout()
        layout.addWidget(self.eq_canvas)
        layout.addWidget(self.eq_dials)
        self.setLayout(layout)
