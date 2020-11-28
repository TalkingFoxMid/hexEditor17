from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel
from hexArray import HexArray

class HexUnitWidget(QWidget):
    def __init__(self, byte_index, hex_array):
        super().__init__()
        self.byte_index = byte_index

        box_layout = QVBoxLayout()
        self.setLayout(box_layout)
        box_layout.addWidget(QLabel(str(byte_index)))

