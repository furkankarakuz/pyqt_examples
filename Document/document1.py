from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tailed")

        file.triggered.connect(self.windowAction)
        self.setWindowTitle("MDI Demo")

    def windowAction(self, q):
        print("Triggered")

        if q.text() == "New":
            MainWindow.count = MainWindow.count+1

            sub = QMdiSubWindow()

            widget = QWidget()

            v_box = QVBoxLayout()

            button = QPushButton("Button")

            v_box.addWidget(button)
            widget.setLayout(v_box)

            sub.setWidget(widget)
            sub.setWindowTitle("Test")
            self.mdi.addSubWindow(sub)

            sub.show()

        if q.text() == "Cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tailed":
            self.mdi.tileSubWindows()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
