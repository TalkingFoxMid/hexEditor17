from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QLabel

from tableWidget import TableWidget


class ControllerWidget(QWidget):
    def __init__(self, table_widget: TableWidget, main_widget):
        super().__init__()
        self.main_widget = main_widget
        self.table_widget = table_widget
        box_l = QVBoxLayout()
        self.qlin = QLineEdit()
        box_l.addWidget(self.qlin)
        self.setLayout(box_l)
        r_button = QPushButton("Right >>")
        r_button.clicked.connect(self.get_right)
        l_button = QPushButton("Left <<")
        l_button.clicked.connect(self.get_left)
        file_name_editor_widget = QWidget()
        file_name_editor_layout = QHBoxLayout()
        file_name_editor_layout.addWidget(QLabel("file_name:"))
        self.file_name_editor_qline = QLineEdit("")
        file_name_editor_layout.addWidget(self.file_name_editor_qline)
        file_name_editor_widget.setLayout(file_name_editor_layout)
        box_l.addWidget(file_name_editor_widget)
        button_open_file = QPushButton("Open File")
        button_open_file.clicked.connect(self.main_widget.open_file)
        button_save_file = QPushButton("Save File")
        button_save_file.clicked.connect(self.main_widget.save_file)

        box_l.addWidget(button_open_file)
        box_l.addWidget(button_save_file)
        box_l.addWidget(r_button)
        box_l.addWidget(l_button)

    def set_table_widget(self, table_widget):
        self.table_widget = table_widget
    def get_right(self):
        self.table_widget.get_right()
    def get_left(self):
        self.table_widget.get_left()
    def get_file_name(self):
        return self.file_name_editor_qline.text()
    def mousePressEvent(self, a0):
        self.table_widget.disable_edit_mode()
        self.qlin.setEnabled(False)
        self.qlin.setEnabled(True)
        self.file_name_editor_qline.setEnabled(False)
        self.file_name_editor_qline.setEnabled(True)


