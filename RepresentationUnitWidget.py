from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QLineEdit

class RepresentationUnitWidget(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setFixedWidth(18)
        self.setFixedHeight(30)
        self.setText(str(text))
        self.setStyleSheet('border-style: solid; border-width: 1px; border-color: blue;')

