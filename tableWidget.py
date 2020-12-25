from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

from NullHexUnitWidget import NullHexUnitWidget
from RepresentationUnitWidget import RepresentationUnitWidget
from TablePageWidget import TablePageWidget
from hexUnitEdit import HexUnitEdit
from hexUnitWidget import HexUnitWidget
from hex_byte_verificator import HexByteVerificator
from hex_int_translator import HexIntTranslator
from integer_hexer import Integer_Hexer

class TableWidget(QWidget):
    def __init__(self, hex_array):
        super().__init__()
        self.verification = HexByteVerificator()
        self.translator = HexIntTranslator()
        self.integer_hexer = Integer_Hexer()
        self.lines_per_page = 16
        self.bytes_per_page = 16*self.lines_per_page
        self.hex_array = hex_array
        self.hex_pages = {}
        self.repr_pages = {}
        self.current_edit: HexUnitEdit = None
        self.current_page = 0
        self.page_count = 0
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.init_pages()

    def init_page(self, page_number):
        representation_page_widget = TablePageWidget(16)
        hex_page_widget = TablePageWidget(17)
        self.hex_pages[page_number] = hex_page_widget
        self.repr_pages[page_number] = representation_page_widget
        for line in range(self.lines_per_page):
            self.hex_pages[page_number].add_table_element(
                QLabel(self.integer_hexer.get_hex_string(self.bytes_per_page * page_number + line * 16)))
            for c in range(16):
                byte_index = page_number * self.lines_per_page * 16 + line * 16 + c
                if byte_index > len(self.hex_array.get_byte_array()) - 1:
                    self.repr_pages[page_number].add_table_element(RepresentationUnitWidget(""))
                    self.hex_pages[page_number].add_table_element(NullHexUnitWidget())
                    continue
                unit_representation = RepresentationUnitWidget(
                    chr(self.hex_array.get_byte_array()[byte_index])
                )
                self.repr_pages[page_number].add_table_element(unit_representation)
                self.hex_pages[page_number].add_table_element(HexUnitWidget(
                    byte_index,
                    self.translator.get_hex(
                        self.hex_array.get_byte_array()[byte_index],
                    ),
                    self.hex_array,
                    self,
                    unit_representation))
    def init_pages(self):
        self.page_count = int(len(self.hex_array.get_byte_array()) / (16*self.lines_per_page)) + 1
        self.init_page(0)
        self.main_layout.addWidget(self.hex_pages[0])
        self.main_layout.addWidget(self.repr_pages[0])


    def disable_edit_mode(self):
        if self.current_edit is not None:
            was_edit = False
            self.current_edit.close()
            new_value = self.current_edit.text()
            if self.verification.verify_hex_byte(new_value):
                new_value_hex = new_value.upper()
            else:
                new_value_hex = self.current_edit.value_hex_at_begin
            was_edit = new_value_hex != self.translator.get_hex(
                self.hex_array.get_byte_start_array()[self.current_edit.byte_index]
            )
            new_value_int = self.translator.get_int(
                new_value_hex
            )
            representation: QLabel = self.current_edit.representation
            representation.setText(chr(new_value_int))
            self.hex_array.get_byte_array()[self.current_edit.byte_index] = new_value_int
            self.hex_pages[self.current_page].new_grid_layout.replaceWidget(self.current_edit, HexUnitWidget(
                self.current_edit.byte_index,
                new_value_hex,
                self.hex_array,
                self,
                representation,
                was_edit=was_edit
            ))
    def make_edit(self, hex_unit_widget: HexUnitWidget):
        self.disable_edit_mode()
        qline = HexUnitEdit(hex_unit_widget.byte_index,
                            self.translator.get_hex(
                                self.hex_array.get_byte_array()[hex_unit_widget.byte_index]
                            ),
                            hex_unit_widget.representation
                            )
        hex_unit_widget.close()
        self.hex_pages[self.current_page].new_grid_layout.replaceWidget(hex_unit_widget, qline)
        self.current_edit = qline
        qline.setFocus()
        qline.selectAll()

    def page_set(self, number):
        self.disable_edit_mode()

        print(self.hex_pages)
        if number not in range(0, self.page_count):
            return
        if number not in self.hex_pages:
            self.init_page(number)
        self.hex_pages[self.current_page].hide()
        self.repr_pages[self.current_page].hide()
        self.main_layout.replaceWidget(
            self.hex_pages[self.current_page],
            self.hex_pages[number],
        )
        self.main_layout.replaceWidget(
            self.repr_pages[self.current_page],
            self.repr_pages[number],
        )
        self.current_page = number
        self.hex_pages[self.current_page].show()
        self.repr_pages[self.current_page].show()




