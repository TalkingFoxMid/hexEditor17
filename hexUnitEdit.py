from PyQt5 import QtCore
from PyQt5.QtWidgets import QLineEdit


class HexUnitEdit(QLineEdit):
    def __init__(self, byte_index, value_hex_at_begin, representation):
        super().__init__()
        self.representation = representation
        self.byte_index = byte_index
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.value_hex_at_begin = value_hex_at_begin
        self.setText(str(value_hex_at_begin))
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
