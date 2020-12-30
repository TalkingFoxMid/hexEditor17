from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel

from utils.hex_int_translator import HexIntTranslator


class HexUnitWidget(QLabel):
    def __init__(self, page_on, position_on_page, page_array,
                 table_widget, representation, translator: HexIntTranslator,
                 was_edit=False):
        super().__init__()

        self.representation = representation
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.translator = translator
        self.table_widget = table_widget
        self.set_value(page_array[position_on_page])
        self.init_value = self.value
        self.page_on = page_on
        self.position_on_page = position_on_page
        self.was_edit = False
        self.setStyleSheet(
            'border-style: solid; border-width: 2px; border-color: green;')

    def set_was_edit(self, was_edit):

        if was_edit != self.was_edit:
            if was_edit:
                self.setStyleSheet(
                    'border-style: solid; border-width: 2px; border-color: '
                    'blue;')
            else:
                self.setStyleSheet(
                    'border-style: solid; border-width: 2px; border-color: '
                    'green;')
        self.was_edit = was_edit

    def set_value(self, new_value):

        self.value = new_value
        self.setText(
            str(self.translator.get_hex(self.value))
        )

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.table_widget.make_edit(self)
