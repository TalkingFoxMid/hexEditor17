from PyQt5.QtWidgets import QLabel


class NullHexUnitWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(30)
        self.setFixedHeight(30)
        self.setText("NULL")
        self.setStyleSheet('border-style: solid; border-width: 2px; border-color: red;')
