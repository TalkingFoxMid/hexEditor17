from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from ControllerWidget import ControllerWidget
from hexArray import HexArray
from tableWidget import TableWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.hex_array = HexArray([])
        self.current_table_widget = TableWidget(self.hex_array)
        self.controller_widget = ControllerWidget(self.current_table_widget, self)
        self.box_l = QHBoxLayout()
        self.box_l.addWidget(self.current_table_widget)
        self.box_l.addWidget(self.controller_widget)
        self.setLayout(self.box_l)
    def open_file(self):
        file_name = self.controller_widget.get_file_name()
        with open(file_name, "rb") as fr:
            list_bytes = list(fr.read())
        self.hex_array = HexArray(list_bytes)
        table_widget = TableWidget(self.hex_array)
        self.current_table_widget.close()
        self.box_l.replaceWidget(self.current_table_widget,
                                 table_widget)
        self.current_table_widget = table_widget
        self.controller_widget.set_table_widget(table_widget)
    def save_file(self):
        file_name = self.controller_widget.get_file_name()
        new_content = bytes(self.hex_array.get_byte_array())
        with open(file_name, "wb") as f:
            f.write(new_content)
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == 16777220:
            self.current_table_widget.disable_edit_mode()





