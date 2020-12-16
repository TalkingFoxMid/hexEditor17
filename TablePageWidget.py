from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel


class TablePageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.new_grid_layout = QGridLayout()
        self.new_grid_layout.setColumnStretch(16, 16)
        self.new_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.new_grid_layout.setSpacing(0)
        self.setLayout(self.new_grid_layout)
    def add_table_element(self, element):
        self.new_grid_layout.addWidget(element)
