from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(timeout=self.timeProcess)
        self.timer.start(500)

        self.line_timer = QTimer(timeout=self.lineProcess)
        self.line_timer.start(250)
        # self.timer.timeout.connect(self.timeProcess)

        self.prog = QProgressBar()

        self.label = QLabel()

        self.percent = 0
        self.point = 0

        v_box = QVBoxLayout()
        v_box.addWidget(self.prog)
        v_box.addWidget(self.label)

        self.setLayout(v_box)
        self.show()

    def timeProcess(self):
        self.percent += 5
        self.prog.setValue(self.percent)
        if self.percent >= 100:
            self.timer.stop()
            self.line_timer.stop()
            self.label.setText("<b>Completed</b>")

    def lineProcess(self):
        self.point = ((self.point+1) % 3)+1
        point_text = "."*self.point
        self.label.setText("<b>%% %d Loding %s</b>" %
                           (self.percent, point_text))


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
