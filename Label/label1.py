from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


def Main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 Label Test")
    label = QLabel("Hello World", window)
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec())


Main()
