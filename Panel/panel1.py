from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os,sys

class Panel(QDialog):
    def __init__(self,parent=None):
        super(Panel,self).__init__(parent)

        self.panel = app.clipboard()

        self.label = QLabel()

        v_box = QVBoxLayout()
        self.setLayout(v_box)

        self.content = QLineEdit()
        v_box.addWidget(self.content)
        v_box.addWidget(self.label)


        content_button=QPushButton("Add Content on Panel")
        v_box.addWidget(content_button)
        content_button.clicked.connect(self.add_content)

        image_button=QPushButton("Add Image on Panel")
        v_box.addWidget(image_button)
        image_button.clicked.connect(self.add_image)

        html_button=QPushButton("Add HTML on Panel")
        v_box.addWidget(html_button)
        html_button.clicked.connect(self.add_html)

        dugme=QPushButton("Get from Panel")
        v_box.addWidget(dugme)

        dugme.clicked.connect(self.update_content)

        self.show()

    def add_content(self):
        self.panel.setText(self.content.text())
    
    def add_image(self):
        self.panel.setImage(QImage("icon/image.jpg").scaled(100,125))
    
    def add_html(self):
        mime=QMimeData()
        mime.setHtml(
        '<table border=1 style="border-collapse: collapse">'
        '<tr><th bgcolor="#AABBCC">Qt Panel Content</th></tr>'
        '<tr><td>%s</td></tr>'
        '</table>'%(self.content.text()))

        self.panel.setMimeData(mime)
        self.panel.dataChanged.connect(self.warning_message)
    
    def update_content(self):
        mime = self.panel.mimeData()

        if mime.hasText():
            self.label.setText(mime.text())
        elif mime.hasHtml():
            self.label.setTextFormat(Qt.RichText)
            self.label.setText(mime.html())
        
        elif mime.hasImage():
            self.label.setPixmap(self.panel.pixmap().scaled(100,125))
            image = self.panel.pixmap()
            result = QMessageBox.question(self,"Question","Do you want to register?",QMessageBox.Yes,QMessageBox.No)


            if result == QMessageBox.Yes:
                files = os.listdir("icon/")
                counter = 0
                stop = False
                while True:
                    file_name = "Panel"+str(counter)+".png"
                    if not file_name in files:
                        break
                    counter+=1

                image.save("icon/"+file_name)

    def warning_message(self):
        QMessageBox.warning(self,"Updated","Data Updated on the Panel")




app=QApplication(sys.argv)
window=Panel()
sys.exit(app.exec())