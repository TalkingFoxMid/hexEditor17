from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel,\
    QLineEdit

from representation_unit_widget import RepresentationUnitWidget


class RepresentationEditWidget(QLabel):
    def __init__(self, representation_unit_widget: RepresentationUnitWidget):
        super().__init__()
        self.representation_unit_widget = representation_unit_widget
        self.setFixedWidth(18)
        self.setFixedHeight(30)
        self.setText(representation_unit_widget.text())
        self.setStyleSheet('border-style: solid; border-width: 3px; '
                           'border-color: red;')
