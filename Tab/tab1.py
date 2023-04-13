from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class MainDialog(QDialog):
    def __init__(self,data,parent=None):
        super(MainDialog,self).__init__(parent)

        self.data = data

        self.name = QLineEdit("Test Name")
        self.surname = QLineEdit("Test Username")
        self.degree = QLineEdit("Software Developer")
        self.instution = QLineEdit("Anonymous")
        self.gsm = QLineEdit("+00 000 000 00 00")

        self.image = QLabel()
        self.image.setPixmap(QPixmap("default_profile.jpg").scaled(100,125))
        self.image.setContextMenuPolicy(Qt.ActionsContextMenu)

        delete_image_action = QAction("Delete Image",self,triggered=self.delete_image)
        change_image_action = QAction("Change Image",self,triggered=self.change_image)

        self.image.addAction(delete_image_action)
        
        brace = QAction(self)
        brace.setSeparator(True)

        self.image.addAction(brace)
        self.image.addAction(change_image_action)

        option = QTabWidget()
        option.setTabShape(QTabWidget.Triangular)
        option.addTab(self.eposta_tab(),"E Posta")
        option.addTab(self.home_tab(),"Home")
        option.addTab(self.work_tab(),"Work")
        option.addTab(self.personal_tab(),"Personal")

        dialog_button = QDialogButtonBox(QDialogButtonBox.Ok|
                                    QDialogButtonBox.Cancel)
        dialog_button.button(QDialogButtonBox.Ok).setText("OK")
        dialog_button.button(QDialogButtonBox.Cancel).setText("CANCEL")

        dialog_button.accepted.connect(self.accept)
        dialog_button.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(QLabel("Name : "),0,0)
        grid.addWidget(self.name,0,1)
        grid.addWidget(self.image,0,2,5,1)
        grid.addWidget(QLabel("Surname : "),1,0)
        grid.addWidget(self.surname,1,1)
        grid.addWidget(QLabel("Degree : "),2,0)
        grid.addWidget(self.degree,2,1)
        grid.addWidget(QLabel("Instutation : "),3,0)
        grid.addWidget(self.instution,3,1)
        grid.addWidget(QLabel("GSM : "),4,0)
        grid.addWidget(self.gsm,4,1)
        grid.addWidget(option,5,0,1,4)
        grid.addWidget(dialog_button,6,0,1,4)

        self.setFixedSize(500,500)
        self.setLayout(grid)
        self.show()

    
    def eposta_tab(self):
        eposta_part = QWidget()
        self.eposta_list = QListWidget()

        add_button = QPushButton("Add",clicked=self.add_eposta)
        edit_button = QPushButton("Edit")
        default_button = QPushButton("Default",clicked = self.default_eposta)
        delete_button = QPushButton("Delete",clicked = self.delete_eposta)

        grid = QGridLayout()
        grid.addWidget(QLabel("E Posta Adresses"),0,0)
        grid.addWidget(self.eposta_list,1,0,4,1)
        grid.addWidget(add_button,1,1)
        grid.addWidget(edit_button,2,1)
        grid.addWidget(default_button,3,1)
        grid.addWidget(delete_button)

        eposta_part.setLayout(grid)
        self.update()
        return eposta_part

    def update(self):
        selected_row = self.data["default_row"]
        self.eposta_list.clear()
        row = 0
        for i in self.data["eposta_data"]:
            if row == selected_row:
                i = i + "(Default)"
            self.eposta_list.addItem(i)
            row+=1

    def add_eposta(self):
        selected = QInputDialog.getText(self,"E-Posta","E-Posta Adresses",QLineEdit.Normal)
        if selected[1] == True:
            eposta = selected[0]
            if eposta.find("@")>-1:
                self.data["eposta_data"].append(eposta)
        self.update()
    
    def default_eposta(self):
        selected_row = self.eposta_list.currentRow()
        self.data["selected_row"]=selected_row
        self.update()

    def delete_eposta(self):
        selected_row = self.eposta_list.currentRow()
        if selected_row > -1:
            self.data["eposta_data"].pop(selected_row)
            if selected_row == self.data["selected_row"]:
                self.data["default_row"]=None
            self.update()

    def home_tab(self):
        home_part = QWidget()

        self.address = QTextEdit()
        self.city = QLineEdit()
        self.post_code = QLineEdit()
        self.telephone = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(QLabel("Adress : "),0,0)
        grid.addWidget(self.address,0,1)
        grid.addWidget(QLabel("City : "),1,0)
        grid.addWidget(self.city,1,1)
        grid.addWidget(QLabel("Post Code : "),2,0)
        grid.addWidget(self.post_code,2,1)
        grid.addWidget(QLabel("Telephone : "),3,0)
        grid.addWidget(self.telephone,3,1)

        home_part.setLayout(grid)
        return home_part

    def work_tab(self):
        work_part = QWidget()
        return work_part

    def personal_tab(self):
        personal_part = QWidget()
        return personal_part

    def delete_image(self):
        pass

    def change_image(self):
        selected_image = QFileDialog.getOpenFileName(self,"Selected Image","","*.png\n*.jpg\n*.gif")
        image_path = selected_image[0]
        self.image.setPixmap(QPixmap(image_path).scaled(100,125))


app = QApplication(sys.argv)
window = MainDialog(
    {"eposta_data":["test@test.com"],
     "default_row":1}
)
sys.exit(app.exec())




