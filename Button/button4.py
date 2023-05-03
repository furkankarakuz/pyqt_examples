from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Button Test")

        self.size = 3
        self.text = '<center><b><font size="+%d">Hello World</font></center></b>'
        self.label = QLabel(self.text % (self.size))

        self.small_button = QPushButton("Small Text")
        self.big_button = QPushButton("Big Text")

        box = QGridLayout()
        box.addWidget(self.label, 0, 0, 1, 2)
        box.addWidget(self.small_button, 1, 0)
        box.addWidget(self.big_button, 1, 1)

        self.setLayout(box)
        self.show()

        self.small_button.pressed.connect(self.small_text)
        self.big_button.pressed.connect(self.big_text)

    def small_text(self):
        if self.size > 0:
            self.size -= 1
        self.refresh_text()

    def big_text(self):
        if self.size < 5:
            self.size += 1
        self.refresh_text()

    def refresh_text(self):
        self.label.setText(self.text % (self.size))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
