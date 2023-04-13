from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sqlite3
import sys

class Table(QDialog):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)

        self.Main()

    def Main(self):
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(3)

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QHeaderView.Stretch)
        header.setSectionResizeMode(2,QHeaderView.Stretch)

        self.lookTable()
        add_button = QPushButton("Add",clicked=self.addStudent)
        edit_button = QPushButton("Update",clicked=self.editStudent)

        self.table.setStyleSheet('background:"white"')

        grid = QGridLayout()
        grid.addWidget(self.table,0,0,1,2)
        grid.addWidget(add_button,1,0)
        grid.addWidget(edit_button,1,1)

        self.setLayout(grid)
        self.resize(450,400)

        self.setStyleSheet('background:"#1E90FF"')
        self.table.setStyleSheet('background:"#E6E6FA"')
        self.show()

    def lookTable(self):
        self.table.clear()
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("  NO   ".ljust(12)))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("NAME".ljust(12)))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("SURNAME".ljust(12)))


        connect = sqlite3.connect('students.db')
        cursor = connect.cursor()
        db = cursor.execute ("SELECT no,name,surname FROM student")

        self.noStudent=1
        row = 0
        for i in db:
            column = 0
            self.table.setItem(row,column,QTableWidgetItem(str(i[0])))
            self.table.setItem(row,column+1,QTableWidgetItem(str(i[1])))
            self.table.setItem(row,column+2,QTableWidgetItem(str(i[2])))
            row+=1
            self.noStudent=int(i[0])+1
        connect.close()

    def addStudent(self):
        dialog = AddStudentWindow(self)
        if dialog.exec():
            button_reply = QMessageBox.question(self,"Warning","Do You Want to Add Student",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                connect = sqlite3.connect("students.db")
                cursor = connect.cursor()
                name = dialog.name_line.text()
                surname = dialog.surname_line.text()

                if name and surname:
                    db = cursor.execute("INSERT INTO student (no,name,surname) VALUES (?,?,?)",(self.noStudent,name,surname))
                    connect.commit()
                    connect.close()
                    QMessageBox.about(self,"Message","Selected Student Saved")
                    self.lookTable()
                else:
                    QMessageBox.critical(self,"Warning","Selected Student DIDN'T SAVE")
            else:
                pass
    
    def editStudent(self):
        dialog = EditStudentWindow(self)
        if dialog.exec():
            if dialog.status == "Deleted":
                connect = sqlite3.connect("students.db")
                cursor = connect.cursor()
                db = cursor.execute('DELETE FROM student where no="%d"'%(int(dialog.line_search.text())))
                connect.commit()
                connect.close()
                self.lookTable()
                QMessageBox.information(self,"Message","Selected Student Deleted")
            elif dialog.status == "Updated":
                connect = sqlite3.connect("students.db")
                cursor = connect.cursor()
                db = cursor.execute("UPDATE student SET name=?,surname=? where no=?",(dialog.line_name.text(),dialog.line_surname.text(),int(dialog.line_search.text())))
                connect.commit()
                connect.close()
                self.lookTable()
            
            QMessageBox.information(self,"Message","Selected Student's Information Updated")


class AddStudentWindow(QDialog):
    def __init__(self,parent=None):
        super(AddStudentWindow,self).__init__(parent)

        self.parent = parent
        self.name_line = QLineEdit()
        self.surname_line = QLineEdit()

        button_accept = QPushButton("Add",clicked=self.accept)
        button_cancel = QPushButton("Cancel",clicked=self.reject)

        grid = QGridLayout()
        grid.addWidget(QLabel("Name : "),0,0)
        grid.addWidget(self.name_line,0,1,1,2)
        grid.addWidget(QLabel("Surname : "),1,0)
        grid.addWidget(self.surname_line,1,1,1,2)
        grid.addWidget(button_accept,2,1)
        grid.addWidget(button_cancel,2,2)
        self.setLayout(grid)

        self.setStyleSheet('background:"pink"')
        self.name_line.setStyleSheet('background:"white"')
        self.surname_line.setStyleSheet('background:"white"')

    
class EditStudentWindow(QDialog):
    def __init__(self,parent=None):
        super(EditStudentWindow,self).__init__(parent)

        self.parent = parent

        self.line_search = QLineEdit(self)
        self.line_search.setGeometry(10,10,60,20)
        self.line_search.setInputMask("00")

        self.search_button = QPushButton("Search Student",self,clicked = self.searchStudent)
        self.search_button.setGeometry(80,10,110,20)

        self.line = QLabel("-"*50,self)
        self.line.setGeometry(0,50,250,20)

        self.label_name = QLabel('<font><b>Name : </b></font>',self)
        self.label_name.setGeometry(10,70,50,20)

        self.label_surname = QLabel('<font><b>Surname : </b></font>',self)
        self.label_surname.setGeometry(10,100,50,20)

        self.line_name = QLineEdit(self)
        self.line_name.setEnabled(False)
        self.line_name.setGeometry(80,70,110,20)

        self.line_surname = QLineEdit(self)
        self.line_surname.setEnabled(False)
        self.line_surname.setGeometry(80,100,110,20)

        self.update_button = QPushButton("Update",self,clicked=self.updateStudent)
        self.update_button.setGeometry(10,150,80,50)

        self.delete_button = QPushButton("Delete",self,clicked=self.deleteStudent)
        self.delete_button.setGeometry(110,150,80,50)

        self.save_button = QPushButton("Save",self,clicked=self.saveStudent)
        self.save_button.setGeometry(10,150,80,50)

        self.save_button.setVisible(False)

        self.not_found_label = QLabel('<b>## NOT FOUND STUDENT ##</b>',self)
        self.not_found_label.setGeometry(15,20,180,50)
        self.not_found_label.setVisible(True)

        self.var_list=[self.line,self.label_name,self.label_surname,self.line_name,self.line_surname,self.update_button,self.delete_button]

        for i in self.var_list:
            i.setVisible(False)

        self.not_found_label.setVisible(False)
        self.setFixedSize(200,50)
        self.show()
    
    def searchStudent(self):
        self.line_search.setFocus()
        connect = sqlite3.connect('students.db')
        cursor = connect.cursor()
        try:
            db = cursor.execute('SELECT name,surname from student WHERE no="%d"'%(int(self.line_search.text())))
        except:
            self.not_found_label.setText('<center><font><b>Not Found Student</b></font></center>')
            self.not_found_label.setVisible(True)
            return

        if db.fetchall()!=[]:
            for i in self.var_list:
                i.setVisible(True)
            self.not_found_label.setVisible(False)
            self.setFixedSize(300,350)
            db = cursor.execute('SELECT name,surname from student WHERE no="%d"'%(int(self.line_search.text())))
            for i in db.fetchall():
                self.line_name.setText(i[0])
                self.line_surname.setText(i[1])
        else:
            for i in self.var_list:
                i.setVisible(False)
            
            self.not_found_label.setVisible(True)
            self.setFixedSize(200,60)
            self.not_found_label.setText('<center><font><b>Not Found Student</b></font></center>')
            self.not_found_label.setVisible(True)

        connect.close()

    def deleteStudent(self):
        self.status = "Deleted"
        QDialog.accept(self)
    
    def updateStudent(self):
        self.line_name.setEnabled(True)
        self.line_surname.setEnabled(True)
        self.save_button.setVisible(True)

    def saveStudent(self):
        self.status = "Updated"
        QDialog.accept(self)
        self.save_button.setVisible(False)


app = QApplication(sys.argv)
window = Table()
sys.exit(app.exec())















