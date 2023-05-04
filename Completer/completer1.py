from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Main(QDialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        common_fruits = QCompleter([
            'Apple',
            'Apricot',
            'Banana',
            'Carambola',
            'Olive',
            'Oranges',
            'Papaya',
            'Peach',
            'Pineapple',
            'Pomegranate',
            'Rambutan',
            'Ramphal',
            'Raspberries',
            'Rose apple',
            'Starfruit',
            'Strawberries',
            'Water apple',
        ])

        line = QLineEdit()
        line.setCompleter(common_fruits)
        v_box = QVBoxLayout()
        v_box.addWidget(line)

        self.setLayout(v_box)
        self.show()


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
