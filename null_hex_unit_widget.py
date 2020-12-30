from PyQt5.QtWidgets import QLabel


class NullHexUnitWidget(QLabel):
    def __init__(self, table_widget, position):
        super().__init__()
        self.position_on_page = position
        self.table_widget = table_widget
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.setText("NULL")
        self.setStyleSheet('border-style: solid; border-width: 2px; '
                           'border-color: red;')

    def mousePressEvent(self, ev):
        self.table_widget.open_null_widgets(self)
