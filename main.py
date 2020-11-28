from PyQt5.QtWidgets import *
import sys
from hexArray import HexArray
from tableWidget import TableWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



        self.hex_array = HexArray()
        table_widget = TableWidget(self.hex_array)
        self.setCentralWidget(table_widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()