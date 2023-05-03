from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Events(QMainWindow):
    def __init__(self, parent=None):
        super(Events, self).__init__(parent)

        self.label = QLabel("Click Escape, Q or other enter key button")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)
        self.resize(250, 250)

    def event(self, eventt):
        if eventt.type() == QEvent.KeyPress:
            if eventt.key() == Qt.Key_Escape:
                self.label.setText("You entered ESC Key")
                return True
        return QWidget.event(self, eventt)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.label.setText("You entered Left Key")
        elif event.key() == Qt.Key_Q:
            if event.modifiers() & Qt.ControlModifier:
                self.label.setText("You entered Ctrl+Q Key")
            elif event.modifiers() & Qt.ShiftModifier:
                self.label.setText("You entered Shift+Q Key")
            elif event.modifiers() & Qt.MetaModifier:
                self.label.setText("You entered Meta+Q Key")
            else:
                self.label.setText("You entered Q Key")

    def mousePressEvent(self, event):
        screen_position = self.mapToGlobal(event.pos())
        self.label.setText("You clicked mouse"
                           "<br>"
                           "<br>"
                           "The position of the mouse on the window (%d,%d)"
                           "<br>"
                           "The position of the mouse on the screen (%d,%d)"
                           % (event.pos().x(), event.pos().y(), screen_position.x(), screen_position.y()))

    def mouseMoveEvent(self, event):
        self.label.setText("You moved the mouse")

    def mouseReleaseEvent(self, event):
        self.label.setText("You released the mouse")

    def resizeEvent(self, event):
        self.label.setText("You resized the window"
                           "<br>"
                           "<br>"
                           "<b>New Size</b>"
                           "<br><b>Width</b> : %d"
                           "<br><b>Height</b> : %d"
                           % (event.size().width(), event.size().height()))

    def moveEvent(self, event):
        self.label.setText("You moved the window"
                           "<br>Old Position of the mouse (%d,%d)"
                           "<br>New Position of the mouse (%d,%d)"
                           % (event.oldPos().x(), event.oldPos().y(), event.pos().x(), event.pos().y()))


app = QApplication(sys.argv)
window = Events()
window.show()
sys.exit(app.exec())
