from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog

import sys,os

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.type_values = {
            "font_type":"Arial",
            "font_size":15,
            "bold":False,
            "italic":False,
            "align":Qt.AlignLeft
        }

        self.check_save = False
        self.file_name = None
        self.save_directory = QDir().homePath()

        self.main_text = QTextEdit()

        self.main_text.setFontFamily(self.type_values["font_type"])
        self.main_text.setFontPointSize(self.type_values["font_size"])
        self.main_text.textChanged.connect(self.updateDockWindow)
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Program is Ready",3000)

        dock_window = QDockWidget("Statistics",self)
        self.statistics_label = QLabel()

        dock_window.setWidget(self.statistics_label)
        dock_window.setAllowedAreas(Qt.RightDockWidgetArea)
        dock_window.setObjectName("Connect / Statistics")

        self.addDockWidget(Qt.RightDockWidgetArea,dock_window)
        self.setCentralWidget(self.main_text)
        self.resize(800,500)
        self.show()

        self.updateWindowTitle()
        self.updateDockWindow()
        self.action_process()
        self.ToolbarAction()
        self.menus()
    

    def updateWindowTitle(self):
        file = self.file_name if self.file_name else "New File"
        star = "*" if not self.check_save else ""
        self.setWindowTitle("%s - [%s]"%(app.applicationName(),(file)+star))

    def updateDockWindow(self):
        content = self.main_text.toPlainText()
        information = '''<table>
        <tr><td><b>Char : </b></td><td>%d</td></tr>
        <tr><td><b>Word : </b></td><td>%d</td></tr>
        <tr><td><b>Line : </b></td><td>%d</td></tr>'''%(len(content),len(content.split()),content.count("\n"))

        self.statistics_label.setText(information)
        self.check_save = False

        self.updateWindowTitle()
        self.action_process()
    
    def action_process(self):
        self.align_left_action = QAction("&Align Left",self,triggered=self.AlignLeft)
        self.align_left_action.setStatusTip("This option aligns paragraph left")
        self.align_left_action.setCheckable(True)
        self.align_left_action.setShortcut("Alt+Z")

        self.align_center_action = QAction("&Align Center",self,triggered=self.AlignCenter)
        self.align_center_action.setStatusTip("This option aligns paragraph center")
        self.align_center_action.setCheckable(True)
        self.align_center_action.setShortcut("Alt+X")

        self.align_right_action = QAction("&Align Center",self,triggered=self.AlignRight)
        self.align_right_action.setStatusTip("This option aligns paragraph right")
        self.align_right_action.setCheckable(True)
        self.align_right_action.setShortcut("Alt+C")

        self.bold_action = QAction("&Bold",self,triggered=self.EditBold)
        self.bold_action.setStatusTip("This option edits paragraph bold")
        self.bold_action.setCheckable(True)
        self.bold_action.setShortcut("Ctrl+B")

        self.italic_action = QAction("&Italic",self,triggered=self.EditItalic)
        self.italic_action.setStatusTip("This option edits paragraph italic")
        self.italic_action.setCheckable(True)
        self.italic_action.setShortcut("Ctrl+I")

        self.underline_action = QAction("&Underline",self,triggered=self.EditUnderline)
        self.underline_action.setStatusTip("This option edits paragraph underline")
        self.underline_action.setCheckable(True)
        self.underline_action.setShortcut("Ctrl+U")

        self.font_type_action = QAction("&Font Type",self,triggered=self.EditFontType)
        self.font_type_action.setStatusTip("This option edits font type")
        self.font_type_action.setCheckable(True)
        self.font_type_action.setShortcut("Ctrl+Y")

        self.color_type_action = QAction("&Color Type",self,triggered=self.EditColorType)
        self.color_type_action.setStatusTip("This option edits color type")
        self.color_type_action.setShortcut("F5")

        self.save_action = QAction("&Save",self,triggered=self.Save)
        self.save_action.setStatusTip("This option saves file")
        self.save_action.setShortcut(QKeySequence.Save)

        self.save_as_action = QAction("&Save AS",self,triggered=self.SaveAs)
        self.save_as_action.setStatusTip("This option saves as file")
        self.save_as_action.setShortcut(QKeySequence.SaveAs)

        self.open_file_action = QAction("&Open File",self,triggered=self.OpenFile)
        self.open_file_action.setStatusTip("This option opens file")
        self.open_file_action.setShortcut(QKeySequence.Open)

        self.print_file_action = QAction("&Print File",self,triggered=self.PrintFile)
        self.print_file_action.setStatusTip("This option prints file")

        self.convert_pdf = QAction("&Convert PDF",self,triggered=self.ConvertPdf)
        self.convert_pdf.setStatusTip("This option convert pdf file")

        self.subject_action = QAction("&Subject",self,triggered=self.AddSubject)
        self.subject_action.setStatusTip("This option adds Subject")

        self.table_action = QAction("&Add Table",self,triggered=self.AddTable)
        self.table_action.setStatusTip("This option adds table")
        
        #self.image_action = QAction("&Add Image",self,triggered=self.AddImage)
        #self.image_action.setStatusTip("This adds image")


    def ToolbarAction(self):
        paragraph_tool = self.addToolBar("Paragraph")
        paragraph_tool.setObjectName('tool/paragraph')
        paragraph_tool.addAction(self.align_left_action)
        self.align_left_action.setChecked(True)

        paragraph_tool.addAction(self.align_center_action)
        paragraph_tool.addAction(self.align_right_action)

        paragraph_group = QActionGroup(self)
        paragraph_group.addAction(self.align_left_action)
        paragraph_group.addAction(self.align_center_action)
        paragraph_group.addAction(self.align_right_action)

        font_type_tool = QToolBar("Edit")
        font_type_tool.setObjectName("tool/edit")
        font_type_tool.addAction(self.bold_action)
        font_type_tool.addAction(self.italic_action)
        font_type_tool.addAction(self.underline_action)

        self.addToolBar(font_type_tool)

    
    def menus(self):
        menu_bar = QMenuBar()

        self.setMenuBar(menu_bar)

        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("&Edit")
        add_menu = menu_bar.addMenu("&Add")
        help_menu = menu_bar.addMenu("&Menu")

        align_menu = edit_menu.addMenu("&Align")
        align_menu.addAction(self.align_left_action)
        align_menu.addAction(self.align_center_action)
        align_menu.addAction(self.align_right_action)

        edit_menu.addAction(self.font_type_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.color_type_action)

        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(self.open_file_action)
        file_menu.addSeparator()
        file_menu.addAction(self.print_file_action)
        file_menu.addSeparator()
        file_menu.addAction(self.convert_pdf)

        add_menu.addAction(self.subject_action)
        add_menu.addAction(self.table_action)
        #add_menu.addAction(self.image_action)



    def AlignLeft(self):
        self.main_text.setAlignment(Qt.AlignLeft)
    
    def AlignCenter(self):
        self.main_text.setAlignment(Qt.AlignCenter)
    
    def AlignRight(self):
        self.main_text.setAlignment(Qt.AlignRight)

    
    def EditBold(self):
        if self.sender().isChecked():
            self.main_text.setFontWeight(QFont.Bold)
        else:
            self.main_text.setFontWeight(QFont.Normal)
    

    def EditItalic(self):
        if self.sender().isChecked():
            self.main_text.setFontItalic(True)
        else:
            self.main_text.setFontItalic(False)
    
    def EditUnderline(self):
        if self.sender().isChecked():
            self.main_text.setFontUnderline(True)
        else:
            self.main_text.setFontUnderline(False)

    def PrinFile(self):
        f = open(self.file_name,"w")
        f.write(self.main_text.toPlainText())
        f.close()

        self.status_bar.showMessage("File Saved Successfuly",1000)
        self.check_save = True
        self.windowTitleChanged()
    
    def SaveAs(self):
        file = self.file_name if self.file_name else self.save_directory
        selected_file = QFileDialog.getSaveFileName(self,app.applicationName()+"- File Save",file,"*.txt")
        if selected_file:
            self.file_name = selected_file[0]
            self.PrintFile()
            self.save_directory=selected_file[0]
            return True
        else:
            return False

    def Save(self):
        if not self.file_name:
            return self.SaveAs()
        else:
            self.PrintFile()
            return True
        
    def UploadFile(self,file):
        f = open(file).read()
        self.main_text.setText(f)

        self.check_save = True
        self.file_name = file

    def OpenFile(self):
        if not self.check_save:
            if len(self.main_text.toPlainText())>0:
                save_result = self.QuestionSave()
                if save_result=="Yes":
                    self.Save()
                else:
                    return
        selected_file = QFileDialog.getOpenFileName(self,app.applicationName()+" - Open File",self.save_directory,"*.txt")
        print(selected_file)
        if selected_file:
            self.save_directory = selected_file
            self.UploadFile(selected_file[0])
    
    def QuestionSave(self):
        result = QMessageBox.question(self,app.applicationName()," - Selected File Not Save \n Will Save Change?",QMessageBox.Yes , QMessageBox.No)

        if result == QMessageBox.Yes:
            return "Yes"
        elif result == QMessageBox.No:
            return "No"

    def EditColorType(self):
        color_dialog = QColorDialog()
        color_dialog.setCurrentColor(self.main_text.textColor())
        if color_dialog.exec():
            self.main_text.setTextColor(color_dialog.selectedColor())

    def PrintFile(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.PrinterFile)
        dialog.exec()

    def PrinterFile(self,printer):
        self.main_text.print(printer)

    def ConvertPdf(self):
        document = self.main_text.document()
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("file.pdf")
        document.print(printer)
    
    def AddSubject(self):
        subject = QInputDialog.getText(self,"Document Subject","Subject : ",QLineEdit.Normal,"Write Here Subject")
        if subject[1]==True:
            self.main_text.setAlignment(Qt.AlignCenter)
            self.main_text.setFontPointSize(20)
            self.main_text.setFontWeight(QFont.Bold)
            self.main_text.insertPlainText("\n"+subject[0])
            self.main_text.insertPlainText("\n")
        else:
            print("Cancelled Subject")
        

        self.main_text.setAlignment(Qt.AlignLeft)
        self.main_text.setFontPointSize(self.type_values["font_size"])
        self.main_text.setFontWeight(QFont.Normal)
    
    def AddTable(self):
        self.row = int()
        self.column = int()
        dialog = TableDialog(self)
        if dialog.exec():
            cursor = self.main_text.textCursor()
            cursor.insertTable(self.row,self.column)

    
    def EditFontType(self):
        dialog = FontTypeDialog(self)
        dialog.show()
    

class FontTypeDialog(QDialog):
    def __init__(self,parent=None):
        super(FontTypeDialog,self).__init__(parent)

        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)

        grid = QGridLayout()
        font_label = QLabel("Font Type : ")
        font_label.addWidget(font_label,0,0)

        self.font_type = QFontComboBox()
        grid.addWidget(self.font_type,0,1)
        font_label.setBuddy(self.font_type)

        size_label = QLabel("&Size : ")
        grid.addWidget(size_label,1,0)
        
        self.spin = QSpinBox()
        self.spin.setRange(1,50)

        grid.addWidget(self.spin,1,1)
        size_label.setBuddy(self.spin)

        h_box = QHBoxLayout()

        self.font_bold = QCheckBox("&Bold")
        h_box.addWidget(self.font_bold)

        self.font_italic = QCheckBox("&Italic")
        h_box.addWidget(self.font_italic)

        self.font_underline = QCheckBox("&Underline")
        h_box.addWidget(self.font_underline)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|
                                      QDialogButtonBox.Cancel)
        
        button_box.accepted.connect(self.accept_clicked)
        button_box.rejected.connect(self.reject)

        grid.addWidget(button_box,3,0,1,2)
        self.setLayout(grid)


        self.setWindowTitle("Edit Font Type")
        self.font_type.setCurrentFont(self.parent.main_text.currentFont())
        self.spin.setValue(self.parent.main_text.fontPointSize())
        self.font_bold.setChecked(True if self.parent.main_text.fontWeight()==QFont.Bold else False)
        self.font_italic.setChecked(self.parent.main_text.fontItalic())
        self.font_underline.setChecked(self.ebeveny.main_text.fontUnderline())

    def accept_clicked(self):
        self.parent.main_text.setCurrentFont(self.font_type.setCurrentFont())
        self.parent.main_text.setFontPointSize(self.spin.value())
        self.parent.main_text.setFontItalic(self.font_italic.isChecked())
        self.parent.main_text.setFontUnderline(self.font_underline.isChecked())
        self.parent.main_text.setFontWeight(QFont.Bold if self.font_bold.isChecked() else QFont.Normal)
        QDialog.accept(self)


class TableDialog(QDialog):
    def __init__(self,parent=None):
        super(TableDialog,self).__init__(parent)

        self.parent = parent

        self.row = QSpinBox()
        self.column = QSpinBox()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|
                                      QDialogButtonBox.Cancel)
        
        button_box.accepted.connect(self.accept_clicked)
        button_box.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(QLabel("Row : "),0,0)
        grid.addWidget(self.row,0,1)
        grid.addWidget(QLabel("Column : "),1,0)
        grid.addWidget(self.column,1,1)
        grid.addWidget(button_box)

        self.setLayout(grid)


    def accept_clicked(self):
        self.parent.row = self.row.value()
        self.parent.column = self.column.value()
        QDialog.accept(self)



        

app = QApplication(sys.argv)
app.setApplicationName("NotePad")
app.setOrganizationName("NotePad Applicaiton")
window = MainWindow()
sys.exit(app.exec())    

