from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *

import sys
import os

icons = "icons/"


class DragRelease(QDialog):
    def __init__(self, parent=None):
        super(DragRelease, self).__init__(parent)

        source_list = QListWidget()
        for i in os.listdir(icons):
            list_item = QListWidgetItem(i)
            list_item.setIcon(QIcon((icons+i)))
            source_list.addItem(list_item)

        source_list.setDragEnabled(True)

        target_list = QListWidget()
        target_list.setAcceptDrops(True)
        target_list.setViewMode(QListView.IconMode)

        h_box = QHBoxLayout()
        h_box.addWidget(source_list)
        h_box.addWidget(target_list)
        self.setLayout(h_box)


app = QApplication(sys.argv)
window = DragRelease()
window.show()
sys.exit(app.exec())
