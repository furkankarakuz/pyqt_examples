from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
icon_path = "icon/"
class MainPage(QDialog):
    def __init__(self,parent=None):
        super(MainPage,self).__init__(parent)

        self.message = QSystemTrayIcon()
        self.message.setIcon(QIcon(icon_path+"image.jpg"))
        self.message.show()

        self.message.activated.connect(self.send_message)
        self.message.showMessage("Jarvis","Hi :) ",QSystemTrayIcon.MessageIcon(1))

        menu = QMenu()

        option = QAction("Option",self)
        exit = QAction("Exit",self)
        exit.triggered.connect(app.quit)

        menu.addAction(option)
        menu.addAction(exit)
        self.message.setContextMenu(menu)

    def send_message(self):
        self.message.showMessage("Clicked","Message Clicked",QSystemTrayIcon.MessageIcon(3))


app = QApplication(sys.argv)
window = MainPage()
sys.exit(app.exec())