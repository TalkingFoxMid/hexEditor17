from PyQt5.QtGui import QKeyEvent, QWheelEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFileDialog

from controller_widget import ControllerWidget
from HexDataManager.hex_data_manager import HexDataManager
import os
from table_widget import TableWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.hex_data_manager = HexDataManager("")
        self.current_table_widget: TableWidget = TableWidget(
            self.hex_data_manager)
        self.controller_widget = ControllerWidget(self.current_table_widget,
                                                  self)
        self.box_l = QHBoxLayout()
        self.box_l.addWidget(self.current_table_widget)
        self.box_l.addWidget(self.controller_widget)
        self.setLayout(self.box_l)

    def open_file(self):

        file_name, _ = QFileDialog.getOpenFileName()
        if os.path.isfile(file_name):
            self.hex_data_manager = HexDataManager(file_name)
            table_widget = TableWidget(self.hex_data_manager)
            self.current_table_widget.close()
            self.box_l.replaceWidget(self.current_table_widget,
                                     table_widget)
            self.current_table_widget = table_widget
            self.controller_widget.set_table_widget(table_widget)
            self.controller_widget.update_current_page_label()

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName()
        if file_name == "":
            return
        self.hex_data_manager.write_changes_in_file(file_name)

    def new_file(self):
        self.hex_data_manager = HexDataManager("")
        table_widget = TableWidget(self.hex_data_manager)
        self.current_table_widget.close()
        self.box_l.replaceWidget(self.current_table_widget,
                                 table_widget)
        self.current_table_widget = table_widget
        self.controller_widget.set_table_widget(table_widget)
        self.controller_widget.update_current_page_label()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == 16777220:
            self.current_table_widget.disable_edit_mode()
        else:
            self.current_table_widget.handle_representation_symbol(a0.text())

    def wheelEvent(self, a0: QWheelEvent) -> None:
        if a0.angleDelta().y() > 0:
            self.controller_widget.get_right()
        else:
            self.controller_widget.get_left()
