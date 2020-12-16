from PyQt5.QtWidgets import QLineEdit


class HexUnitEdit(QLineEdit):
    def __init__(self, byte_index, value_int_at_begin):
        super().__init__()
        self.byte_index = byte_index
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.value_int_at_begin = value_int_at_begin
        self.setText(str(value_int_at_begin))