from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainDialog(QDialog):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)


        self.stack = QStackedWidget()
        self.stack.addWidget(self.fridge_menu())
        self.stack.addWidget(self.washer_menu())

        self.product_combo = QComboBox(currentIndexChanged=self.stack.setCurrentIndex)
        self.product_combo.addItems(["Fridge","Washer","Bulaşık Makinası"])

        button_diyalog=QDialogButtonBox(QDialogButtonBox.Ok|
                                   QDialogButtonBox.Cancel)

        button_diyalog.button(QDialogButtonBox.Ok).setText("OK")
        button_diyalog.button(QDialogButtonBox.Cancel).setText("CANCEL")


        button_diyalog.accepted.connect(self.accept)
        button_diyalog.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(QLabel("Product Type : "),0,0)
        grid.addWidget(self.product_combo,0,1,Qt.Alignment(1))
        grid.setColumnStretch(1,1)
        grid.addWidget(self.stack,1,0,1,2)
        grid.addWidget(button_diyalog,2,0,1,2)

        self.setLayout(grid)
        self.show()
    
    def fridge_menu(self):
        fridge_part = QWidget()

        model = QLineEdit()
        length = QLineEdit()


        current_spin = QSpinBox()
        current_spin.setRange(1,20)
        current_spin.setSuffix(" A")

        capacity_spin = QSpinBox()
        capacity_spin.setRange(200,2000)
        capacity_spin.setSuffix(" Lt")

        star_class_combo = QComboBox()
        star_class_combo.addItems(["*","**","***","****","*****"])

        energy_class_combo = QComboBox()
        energy_class_combo.addItems(["A+","A","B","C","D","E"])

        grid = QGridLayout()
        grid.addWidget(QLabel("Model : "),0,0)
        grid.addWidget(model,0,1)
        grid.addWidget(QLabel("Width x Deep (mm) : "),1,0)
        grid.addWidget(length,1,1)
        grid.addWidget(QLabel("Max Current"),2,0)
        grid.addWidget(current_spin,2,1,Qt.Alignment(1))
        grid.addWidget(QLabel("Sum Capacity : "),3,0)
        grid.addWidget(capacity_spin,3,1,Qt.Alignment(1))
        grid.addWidget(QLabel("Star Class : "),4,0)
        grid.addWidget(star_class_combo,4,1,Qt.Alignment(1))
        grid.addWidget(QLabel("Energy Class : "),5,0)
        grid.addWidget(energy_class_combo,5,1,Qt.Alignment(1))

        fridge_part.setLayout(grid)
        return fridge_part
    
    def washer_menu(self):
        washer_part = QWidget()

        model = QLineEdit()
        length = QLineEdit()


        net_weight = QLineEdit()

        capacity_spin = QSpinBox()
        capacity_spin.setRange(200,2000)
        capacity_spin.setSuffix(" Lt")

        star_class_combo = QComboBox()
        star_class_combo.addItems(["*","**","***","****","*****"])

        energy_class_combo = QComboBox()
        energy_class_combo.addItems(["A+","A","B","C","D","E"])

        grid = QGridLayout()
        grid.addWidget(QLabel("Model : "),0,0)
        grid.addWidget(model,0,1)
        grid.addWidget(QLabel("Width x Deep (mm) : "),1,0)
        grid.addWidget(length,1,1)
        grid.addWidget(QLabel("Max Current"),2,0)
        grid.addWidget(net_weight,2,1)
        grid.addWidget(QLabel("Sum Capacity : "),3,0)
        grid.addWidget(capacity_spin,3,1,Qt.Alignment(1))
        grid.addWidget(QLabel("Star Class : "),4,0)
        grid.addWidget(star_class_combo,4,1,Qt.Alignment(1))
        grid.addWidget(QLabel("Energy Class : "),5,0)
        grid.addWidget(energy_class_combo,5,1,Qt.Alignment(1))



        washer_part.setLayout(grid)
        return washer_part


app = QApplication(sys.argv)
window = MainDialog()
sys.exit(app.exec())