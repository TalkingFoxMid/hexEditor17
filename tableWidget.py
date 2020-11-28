from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from hexUnitWidget import HexUnitWidget

class TableWidget(QWidget):
    def __init__(self, hex_array):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(5, 4)
        self.setLayout(self.grid_layout)
        self.hex_array = hex_array
        self.init_table()
    def init_table(self):
        for i in self.hex_array.get_byte_array():
            print("sdf")
            self.grid_layout.addWidget(HexUnitWidget(i, self.hex_array))

