from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
import sys

from MainWidget import MainWidget
from hexArray import HexArray
from tableWidget import TableWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainWidget())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()