from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

def Main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 Image Test")
    
    label = QLabel(window)
    label.setPixmap(QPixmap('logo.png'))

    window.resize(300,300)
    window.show()
    sys.exit(app.exec())
Main()