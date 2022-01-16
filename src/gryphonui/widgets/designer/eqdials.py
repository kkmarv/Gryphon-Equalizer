from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QDial, QLabel

from typing import Union


DIAL_UI_FILE_PATH: str = r'gryphonui/widgets/designer/assets/dial_widget.ui'


def get_sign(number) -> str:
    """Returns a string containing a plus sign if number is positive. Else the string returned contains a blank."""
    return '+' if number > 0 else ' '


class EQDials(QWidget):  # TODO outsource dial and label together into a single class
    def __init__(self, function):  # TODO rename function to match EQs' amplify
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

        # declare QLabels (above the dials)
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

        # declare QLabels (beneath the dials)
        self.value_1: Union[QLabel, None] = None
        self.value_2: Union[QLabel, None] = None
        self.value_3: Union[QLabel, None] = None
        self.value_4: Union[QLabel, None] = None
        self.value_5: Union[QLabel, None] = None
        self.value_6: Union[QLabel, None] = None
        self.value_7: Union[QLabel, None] = None
        self.value_8: Union[QLabel, None] = None
        self.value_9: Union[QLabel, None] = None
        self.value_10: Union[QLabel, None] = None

        # load dials and labels from ui designer file
        uic.loadUi(DIAL_UI_FILE_PATH, baseinstance=self)

        self._function = function

        self.connect_dials()

    def connect_dials(self):
        self.dial_1.valueChanged.connect(lambda: self.woof(self.dial_1, self.label_1, self.value_1))
        self.dial_2.valueChanged.connect(lambda: self.woof(self.dial_2, self.label_2, self.value_2))
        self.dial_3.valueChanged.connect(lambda: self.woof(self.dial_3, self.label_3, self.value_3))
        self.dial_4.valueChanged.connect(lambda: self.woof(self.dial_4, self.label_4, self.value_4))
        self.dial_5.valueChanged.connect(lambda: self.woof(self.dial_5, self.label_5, self.value_5))
        self.dial_6.valueChanged.connect(lambda: self.woof(self.dial_6, self.label_6, self.value_6))
        self.dial_7.valueChanged.connect(lambda: self.woof(self.dial_7, self.label_7, self.value_7))
        self.dial_8.valueChanged.connect(lambda: self.woof(self.dial_8, self.label_8, self.value_8))
        self.dial_9.valueChanged.connect(lambda: self.woof(self.dial_9, self.label_9, self.value_9))
        self.dial_10.valueChanged.connect(lambda: self.woof(self.dial_10, self.label_10, self.value_10))

    def woof(self, dial: QDial, freq_band_label: QLabel, db_label: QLabel):  # TODO this needs an overhaul
        db_label.setText('{0:{1}} dB'.format(dial.value(), get_sign(dial.value())))

        # get desired frequency band from label (this is bad practice, pls fix)
        mid_value: int = int(freq_band_label.text().split(" ")[0])

        low_cut: int = 0
        high_cut: int = 0

        if mid_value == 32:
            low_cut = 0
            high_cut = 63
        elif mid_value == 64:
            low_cut = 33
            high_cut = 124
        elif mid_value == 125:
            low_cut = 65
            high_cut = 249
        elif mid_value == 250:
            low_cut = 126
            high_cut = 499
        elif mid_value == 500:
            low_cut = 251
            high_cut = 999
        elif mid_value == 1000:
            low_cut = 501
            high_cut = 1999
        elif mid_value == 2000:
            low_cut = 1001
            high_cut = 3999
        elif mid_value == 4000:
            low_cut = 2001
            high_cut = 7999
        elif mid_value == 8000:
            low_cut = 4001
            high_cut = 15999
        elif mid_value == 16000:
            low_cut = 8001
            high_cut = 20000

        self._function(dial.value(), low_cut, high_cut)

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
