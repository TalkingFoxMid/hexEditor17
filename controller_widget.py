from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, \
    QHBoxLayout, QLabel

from table_widget import TableWidget


class ControllerWidget(QWidget):
    def __init__(self, table_widget: TableWidget, main_widget):
        super().__init__()
        self.current_page_index = 0
        self.main_widget = main_widget
        self.table_widget = table_widget
        box_l = QVBoxLayout()
        self.setLayout(box_l)
        r_button = QPushButton(">")
        r_button.clicked.connect(self.get_right)
        l_button = QPushButton("<")
        l_button.clicked.connect(self.get_left)

        button_open_file = QPushButton("Open File")
        button_open_file.clicked.connect(self.main_widget.open_file)
        button_save_file = QPushButton("Save File")
        button_save_file.clicked.connect(self.main_widget.save_file)
        button_new_file = QPushButton("New File")
        button_new_file.clicked.connect(self.main_widget.new_file)

        box_l.addWidget(button_open_file)
        box_l.addWidget(button_save_file)
        box_l.addWidget(button_new_file)
        page_control_widget = QWidget()
        page_control_widget_box_layout = QHBoxLayout()
        page_control_widget.setLayout(page_control_widget_box_layout)
        self.current_page_label_widget = QLabel("1")

        page_control_widget_box_layout.addWidget(l_button)
        page_control_widget_box_layout.addWidget(
            self.current_page_label_widget
        )
        page_control_widget_box_layout.addWidget(r_button)
        box_l.addWidget(page_control_widget)

        button_new_page = QPushButton("New Page!")
        button_new_page.clicked.connect(self.table_widget_add_new_page)
        box_l.addWidget(button_new_page)
        page_move_widget = QWidget()
        box_h = QHBoxLayout()
        page_move_widget.setLayout(box_h)
        box_h.addWidget(QLabel("Select page:"))
        self.page_move_qline_edit = QLineEdit()
        box_h.addWidget(self.page_move_qline_edit)
        move_page_button = QPushButton("Move to page")
        move_page_button.clicked.connect(self.table_widget_move_page)
        box_h.addWidget(move_page_button)
        box_l.addWidget(page_move_widget)
        self.update_current_page_label()

    def table_widget_move_page(self):
        self.table_widget.page_set(int(self.page_move_qline_edit.text()) - 1)
        self.update_current_page_label()

    def table_widget_add_new_page(self):
        self.table_widget.new_page()
        self.update_current_page_label()

    def update_current_page_label(self):
        self.current_page_index = self.table_widget.current_page
        self.current_page_label_widget.setText(
            str(self.table_widget.current_page + 1)
            + "/" + str(self.table_widget.page_count)
        )

    def set_table_widget(self, table_widget):
        self.table_widget = table_widget

    def get_right(self):
        self.current_page_index += 1
        if self.current_page_index >= self.table_widget.page_count:
            self.current_page_index -= 1
            return
        self.table_widget.page_set(self.current_page_index)

        self.update_current_page_label()

    def get_left(self):
        self.current_page_index -= 1
        if self.current_page_index < 0:
            self.current_page_index = 0
            return
        self.table_widget.page_set(self.current_page_index)
        self.update_current_page_label()

    def get_file_name(self):
        return self.file_name_editor_qline.text()

    def add_edited_string(self):
        self.file_name_editor_qline.setText(
            self.file_name_editor_qline.text() + ".edited"
        )

    def mousePressEvent(self, a0):
        self.table_widget.disable_edit_mode()
