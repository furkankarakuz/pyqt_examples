from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import os
import imghdr

file_path = os.getcwd()+"/"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.icon = QIcon("default_profile.jpg")

        self.list = QListWidget(currentTextChanged=self.look_image)

        self.image_label = QLabel()
        self.content_label = QLabel("Content"
                                    "<hr>")

        right_split = QSplitter(Qt.Vertical)
        right_split.addWidget(self.content_label)
        right_split.addWidget(self.image_label)
        right_split.setFixedSize(350, 350)

        main_split = QSplitter(Qt.Horizontal)
        main_split.addWidget(self.list)
        main_split.addWidget(right_split)

        self.prepare_image_list()

        self.setCentralWidget(main_split)
        self.setFixedSize(500, 500)
        self.show()

    def prepare_image_list(self):
        for i in os.listdir(file_path):
            if imghdr.what(i):
                self.list.addItem(QListWidgetItem(self.icon, i))

    def look_image(self, image):
        photo = QPixmap(file_path+image).scaledToWidth(400)
        self.image_label.setPixmap(photo)

        self.content_label.setText("""
                <h3>File Detail : </h3>
                <br>
                <br>
                <b>File : </b> %s
                <br>
                <b>Type : </b> %s
                <br>
                <b>Memory : </b> %s Bayt
                <br>
                <b>Width : </b> %d
                <br>
                <b>Height : </b> %s <hr> """ % (image, imghdr.what(file_path + image), os.stat(file_path + image)[6],
                                                photo.width(), photo.height()))


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
