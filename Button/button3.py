from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Button Test")

        self.label = QLabel(" ")

        self.button = QPushButton("Click")
        self.button.clicked.connect(self.clicked)

        self.number = 0

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.show()

    def clicked(self):
        self.number += 1
        self.label.setText(
            '<b><font size="+3">%s times clicked<font></b>' % (str(self.number)))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
