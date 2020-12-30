from PyQt5 import QtCore
from PyQt5.QtWidgets import QLineEdit

from hex_unit_widget import HexUnitWidget


class HexUnitEdit(QLineEdit):
    def __init__(self, hex_unit_widget: HexUnitWidget):
        super().__init__()
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.setText(hex_unit_widget.text())
        self.hex_unit_widget = hex_unit_widget
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
