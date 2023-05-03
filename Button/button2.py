from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import random


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Button Test")

        self.label = QLabel(
            '<b><font color="blue" size="+3">Hello World</font></b>')

        self.button = QPushButton("Click")
        self.button.clicked.connect(self.clicked)

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.show()

    def clicked(self):
        self.selected_color = random.choice(
            ['red', 'green', 'blue', 'orange', 'yellow', 'brown', 'purple', 'pink'])
        self.label.setText(
            '<b><font color="%s" size="+3">Hello World</font></b>' % (self.selected_color))
        print(self.selected_color)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
