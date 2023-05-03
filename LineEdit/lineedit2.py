from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.Main()

    def Main(self):
        self.line = QLineEdit()
        self.line.textChanged.connect(self.textChange)

        self.label = QLabel()

        v_box = QVBoxLayout()
        v_box.addWidget(self.line)
        v_box.addWidget(self.label)

        self.setLayout(v_box)
        self.show()

    def textChange(self):
        self.label.setText(self.line.text())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
