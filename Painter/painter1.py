from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import random


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.color = "#FFFFFF"

        self.color_pix_icon = QPixmap(20, 20)
        self.color_pix_icon.fill(QColor(self.color))

        self.window_label = QLabel()
        self.window_pix = QPixmap(500, 500)
        self.window_pix.fill(QColor(self.color))

        self.spin = QSpinBox()
        self.spin.setRange(1, 10)
        self.spin.valueChanged.connect(self.spin_process)

        self.window_label.setPixmap(self.window_pix)

        self.setCentralWidget(self.window_label)

        self.last_x, self.last_y = None, None
        self.width_value = 1
        self.action_process()
        self.bar_process()
        self.menu_process()

    def action_process(self):
        self.color_action = QAction(QIcon(
            self.color_pix_icon), "Select Color", self, triggered=self.color_action_process)
        self.fill_action = QAction(
            QIcon("icon/bucket.png"), "Fill", self, triggered=self.fill_action_process)

        self.pen_action = QAction(QIcon("icon/pen.png"), "Pen", self)
        self.pen_action.setCheckable(True)

        self.spray_action = QAction(QIcon("icon/spray.png"), "Spray", self)
        self.spray_action.setCheckable(True)

        action_group = QActionGroup(self)
        action_group.addAction(self.fill_action)
        action_group.addAction(self.pen_action)
        action_group.addAction(self.spray_action)

        self.open_file_action = QAction(
            "Open File", self, triggered=self.open_file_action_process)
        self.open_file_action.setShortcut("Ctrl+N")

        self.save_file_action = QAction(
            "Save File", self, triggered=self.save_file_action_process)
        self.save_file_action.setShortcut("Ctrl+S")

    def bar_process(self):
        main_tool = QToolBar("Edit")
        main_tool.setFixedHeight(50)

        main_tool.addAction(self.color_action)
        main_tool.addAction(self.fill_action)
        main_tool.addAction(self.pen_action)
        main_tool.addAction(self.spray_action)
        main_tool.addSeparator()
        main_tool.addWidget(self.spin)

        self.addToolBar(main_tool)

    def menu_process(self):
        menu_bar = QMenuBar()

        file_menu = menu_bar.addMenu("File")
        open_file = file_menu.addAction(self.open_file_action)

        save_file = file_menu.addAction(self.save_file_action)

        self.setMenuBar(menu_bar)

    def color_action_process(self):
        self.fill_action.setChecked(False)
        self.pen_action.setChecked(False)
        self.spray_action.setChecked(False)
        color_dialog = QColorDialog()
        if color_dialog.exec():
            self.color = color_dialog.selectedColor().name()
        self.color_pix_icon.fill(QColor(self.color))
        self.color_action.setIcon(QIcon(self.color_pix_icon))

    def fill_action_process(self):

        self.pen_action.setChecked(False)
        self.spray_action.setChecked(False)

        self.window_pix.fill(QColor(self.color))
        self.window_label.setPixmap(self.window_pix)

    def spin_process(self):
        self.width_value = self.spin.value()

    def open_file_action_process(self):
        selected_file = QFileDialog.getOpenFileName(
            self, app.applicationName()+" - Open File", QDir.homePath(), "*.png\n*.jpg")
        self.window_label.setPixmap(
            QPixmap(selected_file[0]).scaled(self.window_label.size()))

    def save_file_action_process(self):
        selected_file = QFileDialog.getSaveFileName(
            self, app.applicationName()+"- File Save", QDir.homePath(), "*.png")[0]
        if selected_file:
            self.window_label.grab().save(self.selected_file)

    def mouseMoveEvent(self, e):
        if self.pen_action.isChecked() or self.spray_action.isChecked():
            if self.last_x is None:
                self.last_x = e.x()
                self.last_y = e.y()
                return

            painter = QPainter(self.window_label.pixmap())
            p = painter.pen()
            p.setWidth(self.width_value)
            p.setColor(QColor(self.color))
            painter.setPen(p)

            if self.spray_action.isChecked():
                for n in range(100):
                    xo = random.gauss(0, 10)
                    yo = random.gauss(0, 10)
                    painter.drawPoint(e.x() + xo, e.y() + yo)
            else:
                painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            self.update()

            self.last_x = e.x()
            self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())
