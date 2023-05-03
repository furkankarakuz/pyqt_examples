from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class FontDialog(QDialog):
    def __init__(self, parent=None):
        super(FontDialog, self).__init__(parent)

        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)

        grid = QGridLayout()
        grid.addWidget(QLabel("Font Type : "), 0, 0)

        self.font_type_list = QFontComboBox()
        self.font_type_list.setCurrentFont(QFont(self.parent.font_type))

        grid.addWidget(self.font_type_list, 0, 1)

        button_group = QDialogButtonBox(QDialogButtonBox.Ok |
                                        QDialogButtonBox.Apply |
                                        QDialogButtonBox.Reset |
                                        QDialogButtonBox.Cancel)

        button_group.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
        button_group.button(QDialogButtonBox.Reset).clicked.connect(self.clear)
        button_group.accepted.connect(self.click_accept)
        button_group.rejected.connect(self.click_reject)

        grid.addWidget(button_group, 1, 0, 1, 2)
        self.setLayout(grid)

        self.setWindowTitle("Edit Font Type")

    def click_accept(self):
        self.parent.font_type = self.font_type_list.currentFont().family()
        self.parent.label.setText(self.parent.content %
                                  (self.parent.font_type))
        QDialog.accept(self)

    def apply(self):
        self.parent.label.setText(self.parent.content % (
            self.font_type_list.currentFont().family()))

    def clear(self):
        self.parent.label.setText(self.parent.content % self.parent.font_type)
        self.font_type_list.setCurrentFont(QFont(self.parent.font_type))

    def click_reject(self):
        self.parent.label.setText(self.parent.content %
                                  (self.parent.font_type))
        QDialog.reject(self)


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.font_type = "Verdana"
        self.content = '<font face="%s" size="+3">Hello World</font>'
        self.label = QLabel(self.content % (self.font_type))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)

        button = QPushButton("Edit Font Type", clicked=self.editFontType)

        v_box.addWidget(button)
        self.setLayout(v_box)
        self.setWindowTitle("Main Dialog")
        self.show()

    def editFontType(self):
        dialog = FontDialog(self)
        dialog.exec()


app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())
