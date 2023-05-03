from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.Main()

    def Main(self):
        self.size = 2
        self.content = '<b><div align="%s"><font size="+%d">Hello World</font></b>'
        self.align = "left"

        self.spin = QSpinBox()
        self.spin.setRange(1, 4)
        self.spin.setValue(self.size)
        self.spin.valueChanged.connect(self.textUpdate)

        self.label_text = QLabel(self.content % (self.align, self.size))
        self.label_size = QLabel("&Content Size : ")
        self.label_size.setBuddy(self.spin)

        self.left_radio = QRadioButton("Align &Left")
        self.center_radio = QRadioButton("Align &Center")
        self.right_radio = QRadioButton("Align &Right")
        self.left_radio.setChecked(True)

        grid = QGridLayout()
        grid.addWidget(self.label_text, 0, 0, 1, 3)
        grid.addWidget(self.label_size, 1, 0)
        grid.addWidget(self.spin, 1, 1, 1, 2)
        grid.addWidget(self.left_radio, 2, 0)
        grid.addWidget(self.center_radio, 2, 1)
        grid.addWidget(self.right_radio, 2, 2)

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.left_radio)
        self.radio_group.addButton(self.center_radio)
        self.radio_group.addButton(self.right_radio)
        self.radio_group.buttonClicked.connect(self.textUpdate)

        self.setLayout(grid)
        self.show()

    def textUpdate(self):
        self.size = self.spin.value()

        if self.left_radio.isChecked():
            self.align = "left"
        elif self.center_radio.isChecked():
            self.align = "center"
        elif self.right_radio.isChecked():
            self.align = "right"

        self.label_text.setText(self.content % (self.align, self.size))


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
