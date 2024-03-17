from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget,QFileDialog,)
import shutil

import sys
from CHECK_PARAMETER import CHECK_PARAMETER
import subprocess
import os
from SCORM import Scorm
import random
import glob
class QWidgetView(QWidget):
    def __init__(self,formobject):
        super().__init__()
        
        self.setAcceptDrops(True)
        self.formobject=formobject
    def dragEnterEvent(self,event):
            
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()
    def dropEvent(self, event):
                files = [u.toLocalFile() for u in event.mimeData().urls()]
                #"".split()
                for f in files:
                    CHECK_PARAMETER.file_input=f
                    m1=f.split("/")
                    self.formobject.label_2.setText(QCoreApplication.translate("MainWindow", m1[len(m1)-1], None))
class Ui_MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        self.Scorm=Scorm()
        
        #self.centralwidget.setAcceptDrops(True)
        
        #self.MainWindow.setAcceptDrops(True)
    def uploadFile(self,MainWindow):
        file_dialog = QFileDialog()
        file_path, file = file_dialog.getOpenFileName(MainWindow)
        dataf=file_path.split("/")
        file_name=dataf[len(dataf)-1]
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"{}".format(file_name), None))
        CHECK_PARAMETER.file_input=file_path
        CHECK_PARAMETER.file_name=file_name
        self.progressBar.setValue(0)
        #self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"", None))
    def convert(self,MainWindow): 
        print("converting... !")
        MainWindow.resize(360, 415)
        MainWindow.setFixedSize(360, 415)
        self.commandLinkButton.setVisible(False)
        self.pushButton_8.setVisible(False)
        self.label_11.setVisible(False)
        self.line_3.setVisible(False)
        print(CHECK_PARAMETER.file_input)
        print(CHECK_PARAMETER.r_button)
        dataf=CHECK_PARAMETER.file_input.split("/")
        file_name=dataf[len(dataf)-1]
        if file_name.lower().endswith(".md"):
            self.progressBar.setValue(random.randint(13,83))
            if CHECK_PARAMETER.r_button.lower()=="pdflatex":
                #dir=os.getcwd()
                dir=os.getenv('LOCALAPPDATA')
                files = glob.glob(dir+"\{}".format("*"))
                #files = glob.glob(dir+"\\{}".format("resources\\*"))
                '''for f in files:
                    try:
                        os.remove(f)
                    except:
                        pass'''
                m=random.randint(0,10000000)

                pdff=dir+"\{}.pdf".format(m)
                self.Scorm.convertMdToPdf(CHECK_PARAMETER.file_input,pdff)  
                self.progressBar.setValue(100)
                CHECK_PARAMETER.file_out=pdff
                #self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.pdf".format(m)), None))
                #m1=CHECK_PARAMETER.file_out.split("\\")
                #print(m1)
                self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Show  {}".format(str(m)+str(".pdf")), None))
                self.commandLinkButton.setVisible(True)
                self.pushButton_8.setVisible(True)
                self.label_11.setVisible(True)
                self.line_3.setVisible(True)
            elif CHECK_PARAMETER.r_button.lower()=="scorm":
                dir1=os.getcwd()
                #files = glob.glob(dir+"\\{}".format("resources\\*"))
                
                dir=os.getenv('LOCALAPPDATA')
                files = glob.glob(dir+"\{}".format("*"))
                
                newpath = dir+r"\resources"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                m=random.randint(0,10000000)
                files = glob.glob(dir1+"//resources//{}".format("*"))
                for f in files:
                    try:
                        os.remove(f)
                    except:
                        pass
                fileoutputhtml=dir1+"//resources//index.html"

                m=random.randint(0,10000000)
                fileoutputpdf=dir1+"//resources//{}.pdf".format(m)
                m=random.randint(0,10000000)
                pname="{}".format(m)
                self.Scorm.convertMdToScorm(CHECK_PARAMETER.file_input,fileoutputhtml,fileoutputpdf,pname)  
                self.progressBar.setValue(100)
                pname=dir+r"\{}".format(m)
                CHECK_PARAMETER.file_out=pname+".zip"
                #self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Download  {}".format(CHECK_PARAMETER.file_out), None))
                m1=CHECK_PARAMETER.file_out.split("/")
                self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Show   {}".format(str(m)+".zip"), None))
                self.commandLinkButton.setVisible(True)
                self.pushButton_8.setVisible(True)
                self.label_11.setVisible(True)
                self.line_3.setVisible(True)
                #self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.zip".format(m)), None))
        else :
            self.commandLinkButton.setVisible(True)
            self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", "The file extension is not valid", None))
            self.pushButton_8.setVisible(True)
            self.label_11.setVisible(True)
            self.line_3.setVisible(True)
            #self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("The file extension is not valid"), None))
        MainWindow.setFixedSize(360, 500)
        MainWindow.resize(360, 500)
    def updateLabel(self,MainWindow):
        if self.radioButton_3.isChecked() == True:
            print("========================= 2")
            print(self.radioButton_3.text())
            CHECK_PARAMETER.r_button=self.radioButton_3.text() 
        if self.radioButton_5.isChecked() == True:
            print("========================= 1")
            print(self.radioButton_5.text())
            CHECK_PARAMETER.r_button=self.radioButton_5.text()
    def openFile(self,file):
        if sys.platform == 'linux2':
            subprocess.call(["xdg-open", file])
        else:
            os.startfile(file)
 
    def setupUi(self,MainWindow,formobject):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 415)
        MainWindow.setFixedSize(360, 415)
        MainWindow.setMinimumSize(QSize(360, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(251, 244, 255);")
        self.centralwidget = QWidgetView(formobject)
        
        #self.centralwidget.event()
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 361, 630))
        self.frame.setStyleSheet(u"background-color: rgb(251, 244, 255);\n"
"border-color: rgb(30, 30, 30);\n"
"border:(\"border: 3px solid blue;\")")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 220, 141, 21))
        self.label_4.setMinimumSize(QSize(141, 21))
        self.label_4.setStyleSheet(u"background-color: rgb(251, 244, 255);")
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(120, 240, 89, 20))
        self.radioButton_3.setMinimumSize(QSize(89, 20))
        self.radioButton_5 = QRadioButton(self.frame)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(120, 260, 89, 20))
        self.radioButton_5.setMinimumSize(QSize(89, 20))
        self.radioButton_3.toggled.connect(self.updateLabel)
        self.radioButton_5.toggled.connect(self.updateLabel)
        self.progressBar = QProgressBar(self.frame)

        self.progressBar.setValue(0)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 340, 341, 23))
        self.progressBar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(11, 11, 11);")
        
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 260, 181))
        self.widget.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 80, 91, 31))
        self.pushButton_4.setMinimumSize(QSize(91, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"\n"
"background-color: rgb(244, 243, 255);")
        
        self.pushButton_4.clicked.connect(lambda:self.uploadFile(MainWindow))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 121, 16))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 130,150, 50))
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 300, 91, 31))
        self.pushButton_6.setMinimumSize(QSize(91, 24))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.pushButton_6.clicked.connect(lambda:  self.convert(MainWindow))

        self.commandLinkButton = QCommandLinkButton(self.frame)
        self.commandLinkButton.setVisible(False)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(60, 400, 250, 100))
        self.commandLinkButton.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.commandLinkButton.clicked.connect(lambda:self.openFile(CHECK_PARAMETER.file_out))
        self.widget_2 = QWidget(self.frame)
        
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(40, 450, 281, 161))
        #self.widget_2.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setVisible(False)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 450, 91, 31))
        self.pushButton_8.setMinimumSize(QSize(91, 24))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.pushButton_8.clicked.connect(lambda:self.file_save(MainWindow))
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 40, 121, 16))
        self.label_9.setVisible(False)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setVisible(False)
        self.label_11.setGeometry(QRect(70, 70, 111, 16))
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 380, 351, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 280, 351, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 430, 351, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 190, 351, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.line_3.setVisible(False)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        return MainWindow
    # setupUi
    def file_save(self,MainWindow):
        name = QFileDialog.getSaveFileName(MainWindow, 'Save File')
        print(name[0])
        name1=str(name[0]).split("/")
        dir=""
        fname=name1[len(name1)-1]
        for i in range(0,len(name1)-1,1):
            if i==0:
                dir+=name1[i]
            else :
                dir+="//"+name1[i]
        
        mn=os.path.basename(CHECK_PARAMETER.file_out)
        mn1=mn.split(".")
        print("===========================")
        print(CHECK_PARAMETER.file_out)
        print(mn1)
        shutil.copy2(CHECK_PARAMETER.file_out, dir+"//"+str(fname)+"."+str(mn1[1]))
        
        print("-------------------------")
        print(dir+str(fname)+str(mn1[1]))
        
        


    def retranslateUi(self,MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Converter", u"Converter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Convert To:</p><p align=\"center\"><br/></p></body></html>", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"SCORM", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"PdfLaTeX", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Drop file here , or ....", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"file.md", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Download  snm.zip", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pop up window", None))
        #self.label_11.setText(QCoreApplication.translate("MainWindow", u"Where to save the file", None))

app = QApplication([])
form = Ui_MainWindow()
m=form.setupUi(QMainWindow(),form)

m.show()
sys.exit(app.exec())