from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, \
    QLineEdit


class RepresentationUnitWidget(QLabel):
    def __init__(self, text, position_on_page, table_widget):
        super().__init__()
        self.position_on_page = position_on_page
        self.table_widget = table_widget
        self.setFixedWidth(18)
        self.setFixedHeight(30)
        self.setText(str(text))
        self.setStyleSheet('border-style: solid; border-width: 1px; '
                           'border-color: blue;')

    def mousePressEvent(self, a0) -> None:
        self.table_widget.set_representation_cursor(self)
