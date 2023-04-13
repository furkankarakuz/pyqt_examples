from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainDialog(QDialog):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)

        self.font_type = "Verdana"
        self.content = '<font face="%s" size="+3">Hello World</font>'
        self.label = QLabel(self.content%(self.font_type))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        button = QPushButton("Edit Font Type")

        button.clicked.connect(self.editFontType)
        
        v_box.addWidget(button)
        self.setLayout(v_box)
        self.setWindowTitle("Dialog Window")
        self.show()
    
    def editFontType(self):
        dialog = FontDialog(self)
        dialog.show()


class FontDialog(QDialog):
    def __init__(self,parent=None):
        super(FontDialog,self).__init__(parent)

        self.parent = parent

        self.setAttribute(Qt.WA_DeleteOnClose)

        grid = QGridLayout()
        grid.addWidget(QLabel("Font Type : "),0,0)

        self.font_type_list = QFontComboBox()
        self.font_type_list.setCurrentFont(QFont(self.parent.font_type))

        grid.addWidget(self.font_type_list,0,1)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        button_box.button(QDialogButtonBox.Ok).setText("Tamam")
        button_box.button(QDialogButtonBox.Cancel).setText("Vazgeç")

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        grid.addWidget(button_box,1,0,1,2)
        self.setLayout(grid)

        self.setWindowTitle("Edit Font Type")
    
    def accept(self):
        self.parent.font_type=self.font_type_list.currentFont().family()
        self.parent.label.setText(self.parent.content%(self.parent.font_type))
        QDialog.accept(self)



app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())
