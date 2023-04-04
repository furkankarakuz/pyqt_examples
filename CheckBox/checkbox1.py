from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.Main()
    
    def Main(self):
        self.checkbox = QCheckBox("Click")
        self.checkbox.clicked.connect(self.clicked)

        self.label = QLabel("Not Clicked")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.label)
        
        self.setLayout(v_box)
        self.show()
    
    def clicked(self):
        if self.checkbox.isChecked():
            self.label.setText("Clicked")
        else:
            self.label.setText("Not Clicked")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())