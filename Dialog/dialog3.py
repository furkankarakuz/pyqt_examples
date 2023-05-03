from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class FontDialog(QDialog):
    def __init__(self, parent=None):
        super(FontDialog, self).__init__(parent)

        self.parent = parent
        grid = QGridLayout()
        grid.addWidget(QLabel("Font Type : "), 0, 0)

        self.font_type_list = QFontComboBox()
        now_font_type = self.parent.content.currentFont()
        self.font_type_list.setCurrentFont(now_font_type)

        self.font_type_list.currentFontChanged.connect(self.editFontType)

        grid.addWidget(self.font_type_list, 0, 1)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        grid.addWidget(close_button, 1, 0, 1, 2)
        self.setLayout(grid)
        self.setWindowTitle("Edit Font Type")

    def editFontType(self):
        font_type = self.font_type_list.currentFont()
        self.parent.content.setCurrentFont(font_type)


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.font_type_object = None
        self.content = QTextEdit()

        v_box = QVBoxLayout()
        v_box.addWidget(self.content)
        button = QPushButton("Edit Font Type", clicked=self.editFontTypes)

        v_box.addWidget(button)
        self.setLayout(v_box)
        self.setWindowTitle("Main Dialog")
        self.show()

    def editFontTypes(self):
        if self.font_type_object is None:
            self.font_type_object = FontDialog(self)

        self.font_type_object.show()
        self.font_type_object.raise_()
        self.font_type_object.activateWindow()

    def closeEvent(self, event):
        if self.font_type_object:
            self.font_type_object.close()


app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())
