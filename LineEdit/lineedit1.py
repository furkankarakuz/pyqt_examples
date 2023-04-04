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

        self.clear = QPushButton("Clear")
        self.printer = QPushButton("Printer")

        self.clear.clicked.connect(self.clicked)
        self.printer.clicked.connect(self.clicked)
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.line)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.printer)


        self.setLayout(v_box)
        self.show()
    
    def clicked(self):
        if self.sender().text()=="Clear":
            self.line.clear()
        else:
            print(self.line.text())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())        