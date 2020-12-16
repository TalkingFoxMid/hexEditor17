from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QVBoxLayout

from NullHexUnitWidget import NullHexUnitWidget
from TablePageWidget import TablePageWidget
from hexUnitEdit import HexUnitEdit
from hexUnitWidget import HexUnitWidget
from integer_hexer import Integer_Hexer

class TableWidget(QWidget):
    def __init__(self, hex_array):
        super().__init__()
        self.integer_hexer = Integer_Hexer()
        self.lines_per_page = 16
        self.bytes_per_page = 16*self.lines_per_page
        self.hex_array = hex_array
        self.pages = []
        self.current_edit: HexUnitWidget = None
        self.current_page = 0
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.init_pages()

    def init_pages(self):
        for page_number in range(int(len(self.hex_array.get_byte_array()) / (16*self.lines_per_page)) + 1):

            table_page_widget = TablePageWidget()
            self.pages.append(table_page_widget)
            for line in range(self.lines_per_page):
                self.pages[page_number].add_table_element(QLabel(self.integer_hexer.get_hex_string(self.bytes_per_page*page_number+line*16)))
                for c in range(16):
                    byte_index = page_number * self.lines_per_page * 16 + line * 16 + c
                    if byte_index > len(self.hex_array.get_byte_array()) - 1:
                        self.pages[page_number].add_table_element(NullHexUnitWidget())
                        continue
                    self.pages[page_number].add_table_element(HexUnitWidget(
                        byte_index,
                        self.hex_array.get_byte_array()[byte_index]
                        , self.hex_array, self))
        self.main_layout.addWidget(self.pages[0])


    def disable_edit_mode(self):
        if self.current_edit is not None:
            was_edit = False
            self.current_edit.close()
            new_value = self.current_edit.text()
            try:
                new_value_int = int(new_value)
            except:
                new_value_int = self.current_edit.value_int_at_begin
            was_edit = new_value_int != self.hex_array.get_byte_start_array()[self.current_edit.byte_index]
            self.hex_array.get_byte_array()[self.current_edit.byte_index] = new_value_int
            self.pages[self.current_page].new_grid_layout.replaceWidget(self.current_edit, HexUnitWidget(
                self.current_edit.byte_index,
                new_value_int,
                self.hex_array,
                self,
                was_edit=was_edit
            ))
    def make_edit(self, hex_unit_widget: HexUnitWidget):
        self.disable_edit_mode()
        qline = HexUnitEdit(hex_unit_widget.byte_index, self.hex_array.get_byte_array()[hex_unit_widget.byte_index])
        hex_unit_widget.close()
        self.pages[self.current_page].new_grid_layout.replaceWidget(hex_unit_widget, qline)
        self.current_edit = qline
        print(self.hex_array.get_byte_array())

    def page_move(self, shift):
        self.disable_edit_mode()
        if self.current_page + shift not in range(0, len(self.pages)):
            return
        self.pages[self.current_page].hide()
        self.main_layout.replaceWidget(
            self.pages[self.current_page],
            self.pages[self.current_page + shift],
        )
        self.current_page += shift
        self.pages[self.current_page].show()

    def get_right(self):
        self.page_move(1)

    def get_left(self):
        self.page_move(-1)


