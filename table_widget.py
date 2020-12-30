from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout, \
    QMessageBox

from HexDataManager.hex_data_manager import HexDataManager
from null_hex_unit_widget import NullHexUnitWidget
from representation_edit_widget import RepresentationEditWidget
from representation_unit_widget import RepresentationUnitWidget
from table_page_widget import TablePageWidget
from hex_unit_edit_widget import HexUnitEdit
from hex_unit_widget import HexUnitWidget
from utils.hex_byte_verificator import HexByteVerificator
from utils.hex_int_translator import HexIntTranslator
from utils.integer_hexer import IntegerHexer


class TableWidget(QWidget):
    def __init__(self, hex_data_manager):
        super().__init__()
        self.is_representation_mode_enabled = False
        self.representation_pointer = 0
        self.current_representation_edit: RepresentationEditWidget = None
        self.representation_unit_widgets_dict = {}
        self.hex_unit_widgets_dict = {}
        self.null_widgets_dict = {}
        self.verification = HexByteVerificator()
        self.translator = HexIntTranslator()
        self.hex_data_manager: HexDataManager = hex_data_manager
        self.integer_hexer = IntegerHexer()
        self.lines_per_page = 10
        self.bytes_per_page = 16 * self.lines_per_page
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
        representation_widgets_list = []
        hex_widgets_list = []
        null_widgets = []
        self.null_widgets_dict[page_number] = null_widgets
        self.representation_unit_widgets_dict[
            page_number] = representation_widgets_list
        self.hex_unit_widgets_dict[page_number] = hex_widgets_list
        hex_page_widget = TablePageWidget(17)
        page_array = byte_value = self.hex_data_manager.get_page(page_number)
        self.hex_pages[page_number] = hex_page_widget
        self.repr_pages[page_number] = representation_page_widget
        for line in range(self.lines_per_page):
            self.hex_pages[page_number].add_table_element(
                QLabel(self.integer_hexer.get_hex_string(
                    self.bytes_per_page * page_number + line * 16)))
            for c in range(16):
                byte_position = 16 * line + c
                if byte_position >= len(page_array):
                    unit_representation =\
                        RepresentationUnitWidget("",
                                                 byte_position,
                                                 self)
                    representation_widgets_list.append(unit_representation)
                    self.repr_pages[page_number].add_table_element(
                        unit_representation
                    )
                    null_widget = NullHexUnitWidget(self, byte_position)
                    self.hex_pages[page_number].add_table_element(
                        null_widget)
                    null_widgets.append(null_widget)
                    continue
                unit_representation = RepresentationUnitWidget(
                    chr(page_array[byte_position]),
                    byte_position,
                    self
                )
                representation_widgets_list.append(unit_representation)
                self.repr_pages[page_number].add_table_element(
                    unit_representation)
                hex_unit = HexUnitWidget(
                    page_number, 16 * line + c, page_array,
                    self, unit_representation,
                    self.translator
                )
                self.hex_pages[page_number].add_table_element(hex_unit)
                hex_widgets_list.append(hex_unit)

    def set_element(self, position_on_page, value_int):
        h_widget = self.hex_unit_widgets_dict[self.current_page][
            position_on_page]
        (h_widget.set_value(value_int))
        (self.representation_unit_widgets_dict[self.current_page][
             position_on_page].
         setText(chr(value_int)))
        self.hex_data_manager.set_value(self.current_page, position_on_page,
                                        value_int)
        was_edit = value_int != h_widget.init_value
        h_widget.set_was_edit(was_edit)

    def init_pages(self):
        self.page_count = self.hex_data_manager.pages_count
        self.init_page(0)
        self.main_layout.addWidget(self.hex_pages[0])
        self.main_layout.addWidget(self.repr_pages[0])

    def open_null_widgets(self, null_widget):
        self.disable_representation_edit()
        null_widgets = self.null_widgets_dict[self.current_page]
        index = null_widgets.index(null_widget)
        grid_layout: QGridLayout = self.hex_pages[
            self.current_page].new_grid_layout
        self.hex_data_manager.append_empty_bytes_for_page(self.current_page,
                                                          index + 1)
        for i in range(index + 1):
            hex_unit_widget = HexUnitWidget(
                self.current_page, null_widgets[i].position_on_page,
                self.hex_data_manager.get_page(self.current_page),
                self, self.representation_unit_widgets_dict[self.current_page][
                    null_widgets[i].position_on_page
                ],
                self.translator
            )
            self.hex_unit_widgets_dict[self.current_page].append(
                hex_unit_widget)
            null_widgets[i].close()

            grid_layout.replaceWidget(null_widgets[i], hex_unit_widget)

        self.null_widgets_dict[self.current_page] = null_widgets[index + 1:]

    def set_representation_cursor(self,
                                  representation_unit_widget:
                                  RepresentationUnitWidget):
        self.disable_representation_edit()
        grid_layout: QGridLayout = self.repr_pages[
            self.current_page].new_grid_layout
        self.current_representation_edit = RepresentationEditWidget(
            representation_unit_widget)
        self.is_representation_mode_enabled = True
        self.representation_pointer = (representation_unit_widget.
                                       position_on_page)
        representation_unit_widget.hide()

        grid_layout.replaceWidget(representation_unit_widget,
                                  self.current_representation_edit)

    def handle_representation_symbol(self, key_text: str):
        if len(key_text) == 0:
            return
        if not key_text.isascii():
            return
        if self.current_representation_edit is not None:

            pointer = (self.current_representation_edit.
                       representation_unit_widget.
                       position_on_page) + 1
            if pointer > len(self.hex_unit_widgets_dict[self.current_page]):
                return
            self.disable_representation_edit()

            self.set_element(pointer - 1, ord(key_text))
            if pointer > self.bytes_per_page - 1:
                return
            unit_widget = self.representation_unit_widgets_dict[
                self.current_page
            ][pointer]
            if pointer > len(
                    self.hex_unit_widgets_dict[self.current_page]) - 1:
                return
            self.set_representation_cursor(unit_widget)

    def disable_representation_edit(self):
        if self.current_representation_edit is None:
            return
        grid_layout: QGridLayout = self.repr_pages[
            self.current_page].new_grid_layout
        rep_widget = (self.current_representation_edit.
                      representation_unit_widget)
        grid_layout.replaceWidget(self.current_representation_edit,
                                  rep_widget)
        rep_widget.show()
        self.current_representation_edit.close()
        self.current_representation_edit = None
        self.representation_pointer = 0
        self.is_representation_mode_enabled = False

    def new_page(self):
        if len(self.null_widgets_dict[self.current_page]) > 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "Для того, чтобы создать новую страницу, "
                "необходимо избавиться от NULL на этой."
                "\nНажмите на последний NULL. И все NULL перед ним "
                "превратятся в действующие элементы.")
            msg.setWindowTitle("Не получилось!")

            msg.exec_()
            return
        self.page_count += 1
        self.init_page(self.current_page + 1)
        self.page_set(self.current_page + 1)

    def disable_edit_mode(self):
        self.disable_representation_edit()
        if self.current_edit is not None:
            self.current_edit.close()

            new_value = self.current_edit.text()

            if self.verification.verify_hex_byte(new_value):
                new_value_hex = new_value.upper()
                new_value_int = self.translator.get_int(
                    new_value_hex
                )
            else:
                new_value_int = self.current_edit.hex_unit_widget.value

            was_edit = (new_value_int !=
                        self.current_edit.hex_unit_widget.init_value)
            self.current_edit.hex_unit_widget.set_was_edit(was_edit)

            representation: QLabel = (self.current_edit.hex_unit_widget.
                                      representation)

            representation.setText(chr(new_value_int))
            self.hex_data_manager.set_value(
                self.current_edit.hex_unit_widget.page_on,
                self.current_edit.hex_unit_widget.position_on_page,
                new_value_int)
            self.hex_pages[self.current_page].new_grid_layout.replaceWidget(
                self.current_edit, self.current_edit.hex_unit_widget)

            self.current_edit.hex_unit_widget.set_value(new_value_int)
            self.current_edit.hex_unit_widget.show()

    def make_edit(self, hex_unit_widget: HexUnitWidget):
        self.disable_edit_mode()
        qline = HexUnitEdit(hex_unit_widget)
        hex_unit_widget.hide()
        self.hex_pages[self.current_page].new_grid_layout.replaceWidget(
            hex_unit_widget, qline)
        self.current_edit = qline
        qline.setFocus()
        qline.selectAll()

    def page_set(self, number):
        self.disable_edit_mode()
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
