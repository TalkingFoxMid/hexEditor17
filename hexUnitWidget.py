from PyQt5.QtGui import QMouseEvent, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QLineEdit
from hexArray import HexArray

class HexUnitWidget(QLabel):
    def __init__(self, byte_index, init_value, hex_array, table_widget, representation, was_edit=False):
        super().__init__()
        self.representation = representation
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.setText(str(init_value))
        self.table_widget = table_widget

        self.byte_index = byte_index

        if was_edit:
            self.setStyleSheet('border-style: solid; border-width: 2px; border-color: blue;')
        else:
            self.setStyleSheet('border-style: solid; border-width: 2px; border-color: green;')



    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.table_widget.make_edit(self)

