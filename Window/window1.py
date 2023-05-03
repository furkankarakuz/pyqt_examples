from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


def Main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 Window")
    window.show()
    sys.exit(app.exec())


Main()
