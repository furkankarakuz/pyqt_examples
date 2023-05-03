from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class FontDialog(QDialog):
    def __init__(self, parent=None):
        super(FontDialog, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(QLabel("Font Type : "), 0, 0)

        self.font_type_list = QComboBox()
        self.font_type_list.addItems(
            ["Arial", "Times New Roman", "Verdana", "Impact"])

        grid.addWidget(self.font_type_list, 0, 1)

        accept_button = QPushButton("Accept")
        cancel_button = QPushButton("Cancel")

        h_box = QHBoxLayout()
        h_box.addWidget(accept_button)
        h_box.addWidget(cancel_button)
        h_box.addStretch()

        grid.addLayout(h_box, 1, 0, 1, 2)

        accept_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.setLayout(grid)
        self.setWindowTitle("Edit Font Type")


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.font_type = "Verdana"
        self.content = '<center><font face="%s" size="+3">Hello World</font></center>'
        self.label = QLabel(self.content % (self.font_type))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)

        button = QPushButton("Edit Font Type", clicked=self.editFontType)

        v_box.addWidget(button)
        self.setLayout(v_box)
        self.setWindowTitle("Main Dialog")

        self.show()

    def editFontType(self):
        dialog = FontDialog()
        if (dialog.exec()):
            self.font_type = dialog.font_type_list.currentText()
            self.label.setText(self.content % (self.font_type))


app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())
