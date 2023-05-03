from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


def accept_clicked():
    print("Accept Button Clicked")


def cancel_clicked():
    print("Cancel Button Clicked")


def Main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 Button Test")

    accept_button = QPushButton("Accept")
    cancel_button = QPushButton("Cancel")

    accept_button.clicked.connect(accept_clicked)
    cancel_button.clicked.connect(cancel_clicked)

    v_box = QVBoxLayout()
    v_box.addWidget(accept_button)
    v_box.addWidget(cancel_button)

    window.setLayout(v_box)
    window.show()
    sys.exit(app.exec())


Main()
