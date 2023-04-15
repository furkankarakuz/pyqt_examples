from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
from IPython import embed

import sys
dictionary={"name":"","surname":"","birthday":"","country":"","city":"","eposta":"","job":"","experince":""}
class WizardPage(QWizard):
    def __init__(self,parent=None):
        super(WizardPage,self).__init__(parent)

        self.parent = parent
        self.addPage(LoginPage(self))
        self.addPage(PersonalInfo(self))
        self.addPage(LocationPage(self))
        self.addPage(JobPage(self))
        self.addPage(ResultPage(self))

        self.setButtonText(QWizard.NextButton,"Next")
        self.setButtonText(QWizard.CancelButton,"Cancel")
        self.setButtonText(QWizard.FinishButton,"Bitti")
        self.setButtonText(QWizard.BackButton,"Back")

        #self.button(QWizard.NextButton).clicked.connect(self.next_clicked)

        self.setWizardStyle(QWizard.ClassicStyle)
        self.setOption(QWizard.NoBackButtonOnLastPage)

        self.show()
        #self.resize(500,150)

    def accept(self):
        print("Welcome!")
        super(WizardPage,self).accept()
    
    def reject(self):
        print("Bye Bye!")
    
class LoginPage(QWizardPage):
    def __init__(self,parent=None):
        super(LoginPage,self).__init__(parent)

        v_box = QVBoxLayout()
        v_box.addWidget(QLabel("Continue to get started"))

        self.setLayout(v_box)

        self.setTitle("Hello!")
        self.setSubTitle("Who Are You?")

class PersonalInfo(QWizardPage):
    def __init__(self,parent=None):
        super(PersonalInfo,self).__init__(parent)

        month_list=["January","February","March","April","May","June","July",
                    "August","September","October","November","December"]

        grid = QGridLayout()
        
        self.name_line = QLineEdit("test")

        self.surname_line = QLineEdit()

        self.day_combo = QComboBox()
        self.day_combo.setEditable(True)
        self.day_combo.addItems([str(i) for i in range(1,32)])

        self.month_combo = QComboBox()
        self.month_combo.setEditable(True)
        self.month_combo.addItems(month_list)

        self.year_combo = QComboBox()
        self.year_combo.setEditable(True)
        self.year_combo.addItems([str(i) for i in range(1970,2024)])

        grid.addWidget(QLabel("Name : "),0,0)
        grid.addWidget(self.name_line,0,1,1,3)
        grid.addWidget(QLabel("Surname : "),1,0)
        grid.addWidget(self.surname_line,1,1,1,3)
        grid.addWidget(QLabel("Birthday : "),3,0)
        grid.addWidget(self.day_combo,3,1)
        grid.addWidget(self.month_combo,3,2)
        grid.addWidget(self.year_combo,3,3)

        self.setLayout(grid)
        self.setTitle("Personal Info")
        self.setSubTitle("Please fill your personal info")
    
    def isComplete(self):
        self.name = self.name_line.text()
        return True

class LocationPage(QWizardPage):
    def __init__(self,parent=None):
        super(LocationPage,self).__init__(parent)
        
        self.parent = parent
        grid = QGridLayout()

        f = open('country.json')
        data = json.load(f)
        country_list=list(data.keys())

        self.country_combo = QComboBox()
        
        self.country_combo.addItems(country_list)
        self.country_combo.setEditable(True)
        self.country_combo.setCurrentText("Country")


        self.city_label = QLabel("City")
        self.city_label.setVisible(False)

        self.city_combo = QComboBox()
        self.city_combo.setEditable(True)
        self.city_combo.setVisible(False)

        grid.addWidget(QLabel("Country : "),0,0)
        grid.addWidget(self.country_combo,0,1)
        
        self.country_combo.currentTextChanged.connect(self.selected_country)

        grid.addWidget(self.city_label,1,0)
        grid.addWidget(self.city_combo,1,1)
        self.setLayout(grid)

        self.setTitle("Location Info")
        self.setSubTitle("Please fill your location info")

    def selected_country(self):
        f = open('country.json')
        data = json.load(f)
        print(self.country_combo.currentText())
        city_list = data[self.country_combo.currentText()]
        self.city_combo.clear()
        self.city_combo.addItems(city_list)
        self.city_combo.setVisible(True)
        self.city_label.setVisible(True)
    
    def accept(self):
        print("ad")

class JobPage(QWizardPage):
    def __init__(self,parent=None):
        super(JobPage,self).__init__(parent)

        grid = QGridLayout()

        self.eposta_line=QLineEdit()
        self.eposta_line.setPlaceholderText("example@example.com")

        self.job = QLineEdit()

        self.experience_combo = QComboBox()
        self.experience_combo.addItems(["1-2 Year","3-5 Year","5-10 Year","10+ Year"])
        
        grid.addWidget(QLabel("E Posta : "),0,0)
        grid.addWidget(self.eposta_line,0,1)
        grid.addWidget(QLabel("Your Job"),1,0)
        grid.addWidget(self.job,1,1)
        grid.addWidget(QLabel("Experince Year :"),2,0)
        grid.addWidget(self.experience_combo,2,1)
        self.setLayout(grid)

        self.setTitle("Job Info")
        self.setSubTitle("Please fill your job info")

class ResultPage(QWizardPage):
    def __init__(self,parent=None):
        super(ResultPage,self).__init__(parent)

        self.prog = QProgressBar()

        self.timer = QTimer(timeout=self.time_process)
        self.timer.start(500)

        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.birthday = QLineEdit()
        self.country = QLineEdit()
        self.city = QLineEdit()
        self.eposta = QLineEdit()
        self.job = QLineEdit()
        self.experience = QLineEdit()

        v_box = QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.prog)
        v_box.addStretch()

        grid = QGridLayout()

        grid.addWidget(QLabel("Name"),0,0)
        grid.addWidget(self.name,0,1)
        grid.addWidget(QLabel("Surname"),1,0)
        grid.addWidget(self.surname,1,1)
        grid.addWidget(QLabel("Birthday : "),2,0)
        grid.addWidget(self.birthday,2,1)
        grid.addWidget(QLabel("Country : "),3,0)
        grid.addWidget(self.country,3,1)
        grid.addWidget(QLabel("City : "),4,0)
        grid.addWidget(self.city,4,1)
        grid.addWidget(QLabel("E Posta : "),5,0)
        grid.addWidget(self.eposta,5,1)
        grid.addWidget(QLabel("Job : "),6,0)
        grid.addWidget(self.job,6,1)
        grid.addWidget(QLabel("Experience : "),7,0)
        grid.addWidget(self.experience,7,1)


        self.group = QGroupBox()
        self.group.setLayout(grid)
        v_box.addWidget(self.group)

        self.group.setVisible(False)

        self.setLayout(v_box)

        self.count=0

    def time_process(self):
        self.count+=5
        self.prog.setValue(self.count)
        if self.count>=100:
            self.timer.stop()
            self.prog.deleteLater()
            self.group.setVisible(True)

        
    

app = QApplication(sys.argv)
window = WizardPage()
sys.exit(app.exec())