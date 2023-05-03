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
        grid.addWidget(QLabel("Font Color : "), 1, 0)
        self.color_line = QLineEdit(self.parent.font_color)

        grid.addWidget(self.color_line, 1, 1)

        button_group = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_group.accepted.connect(self.click_accept)
        button_group.rejected.connect(self.reject)

        grid.addWidget(button_group, 2, 0, 1, 2)
        self.setLayout(grid)
        self.setWindowTitle("Edit Font Type")

    def color_control(self, color):
        if not len(color) == 7:
            return False
        if not color[0] == "#":
            return False
        for i in color[1:]:
            if not i.upper() in "ABCDEF01234556789":
                return False
        return True

    def click_accept(self):
        color = self.color_line.text()
        if not self.color_control(color):
            QMessageBox.question(self, "Error Color",
                                 "Color is Error \n Fix This Problem")
            self.color_line.selectAll()
            self.color_line.setFocus()
            return False

        self.parent.font_type = self.font_type_list.currentFont().family()
        self.parent.font_color = color
        self.parent.label.setText(self.parent.content %
                                  (self.parent.font_type, color))

        QDialog.accept(self)


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.font_type = "Verdana"
        self.font_color = "#FF0000"
        self.content = '<font face="%s" size="+3" color="%s">Hello World</font>'

        self.label = QLabel(self.content % (self.font_type, self.font_color))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        button = QPushButton("Edit Font Type", clicked=self.editFontType)

        v_box.addWidget(button)

        self.setLayout(v_box)
        self.setWindowTitle("Main Dialog")
        self.show()

    def editFontType(self):
        diyalog = FontDialog(self)
        diyalog.exec()


app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())
