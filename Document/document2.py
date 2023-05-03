from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.count = 1

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = QMenuBar()
        self.setMenuBar(bar)

        menu = bar.addMenu("File")
        menu.addAction(QAction("Add Tab", self))
        menu.addAction("Cascade")
        menu.addAction("Edit")

        menu.triggered.connect(self.addTab)
        self.show()

    def addTab(self, q):
        if q.text() == "Add Tab":
            sub = QMdiSubWindow()
            self.setWindowTitle("{}.form".format(self.count))
            self.count += 1

            widget = QWidget()

            v_box = QVBoxLayout()

            v_box.addWidget(QTextEdit())
            v_box.addWidget(QPushButton("Send"))

            widget.setLayout(v_box)
            sub.setWidget(widget)

            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        else:
            self.mdi.tileSubWindows()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
