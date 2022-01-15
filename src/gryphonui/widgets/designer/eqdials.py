from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QDial, QLabel

from typing import Union


DIAL_UI_FILE_PATH: str = r'gryphonui/widgets/designer/assets/dial_widget.ui'


def get_sign(number) -> str:
    """Returns a string containing a plus sign if number is positive. Else the string returned is empty."""
    return '+' if number > 0 else ' '


class EQDials(QWidget):  # TODO outsource dial and label together into a single class
    def __init__(self):
        super().__init__()
        # declare QDials
        self.dial_1: Union[QDial, None] = None
        self.dial_2: Union[QDial, None] = None
        self.dial_3: Union[QDial, None] = None
        self.dial_4: Union[QDial, None] = None
        self.dial_5: Union[QDial, None] = None
        self.dial_6: Union[QDial, None] = None
        self.dial_7: Union[QDial, None] = None
        self.dial_8: Union[QDial, None] = None
        self.dial_9: Union[QDial, None] = None
        self.dial_10: Union[QDial, None] = None

        # declare QLabels
        self.label_1: Union[QLabel, None] = None
        self.label_2: Union[QLabel, None] = None
        self.label_3: Union[QLabel, None] = None
        self.label_4: Union[QLabel, None] = None
        self.label_5: Union[QLabel, None] = None
        self.label_6: Union[QLabel, None] = None
        self.label_7: Union[QLabel, None] = None
        self.label_8: Union[QLabel, None] = None
        self.label_9: Union[QLabel, None] = None
        self.label_10: Union[QLabel, None] = None

        # load in those dials and labels
        uic.loadUi(DIAL_UI_FILE_PATH, baseinstance=self)

        self.init_labels_text()

    def init_labels_text(self):
        template: str = '{0:{1}} dB'

        self.dial_1.valueChanged.connect(
            lambda: self.label_1.setText(template.format(self.dial_1.value(), get_sign(self.dial_1.value())))
        )
        self.dial_2.valueChanged.connect(
            lambda: self.label_2.setText(template.format(self.dial_2.value(), get_sign(self.dial_2.value())))
        )
        self.dial_3.valueChanged.connect(
            lambda: self.label_3.setText(template.format(self.dial_3.value(), get_sign(self.dial_3.value())))
        )
        self.dial_4.valueChanged.connect(
            lambda: self.label_4.setText(template.format(self.dial_4.value(), get_sign(self.dial_4.value())))
        )
        self.dial_5.valueChanged.connect(
            lambda: self.label_5.setText(template.format(self.dial_5.value(), get_sign(self.dial_5.value())))
        )
        self.dial_6.valueChanged.connect(
            lambda: self.label_6.setText(template.format(self.dial_6.value(), get_sign(self.dial_6.value())))
        )
        self.dial_7.valueChanged.connect(
            lambda: self.label_7.setText(template.format(self.dial_7.value(), get_sign(self.dial_7.value())))
        )
        self.dial_8.valueChanged.connect(
            lambda: self.label_8.setText(template.format(self.dial_8.value(), get_sign(self.dial_8.value())))
        )
        self.dial_9.valueChanged.connect(
            lambda: self.label_9.setText(template.format(self.dial_9.value(), get_sign(self.dial_9.value())))
        )
        self.dial_10.valueChanged.connect(
            lambda: self.label_10.setText(template.format(self.dial_10.value(), get_sign(self.dial_10.value())))
        )

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
