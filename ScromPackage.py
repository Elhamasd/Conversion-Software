from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableView,
    QWidget,QFileDialog,)
import sys
from CHECK_PARAMETER import CHECK_PARAMETER
import subprocess
import os
from SCORM import Scorm
import random
import glob
class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.Scorm=Scorm()
    def uploadFile(self,MainWindow):
        file_dialog = QFileDialog()
        file_path, file = file_dialog.getOpenFileName(MainWindow)
        dataf=file_path.split("/")
        file_name=dataf[len(dataf)-1]
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Your Selected File</span></p><p align=\"center\"><span style=\" color:#ffffff;\">{}</span></p></body></html>".format(file_name), None))
        CHECK_PARAMETER.file_input=file_path
        CHECK_PARAMETER.file_name=file_name
        self.progressBar_2.setValue(0)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"", None))
    def convert(self,MainWindow): 
        print("converting... !")
        print(CHECK_PARAMETER.file_input)
        print(CHECK_PARAMETER.r_button)
        dataf=CHECK_PARAMETER.file_input.split("/")
        file_name=dataf[len(dataf)-1]
        if file_name.lower().endswith(".md"):
            self.progressBar_2.setValue(random.randint(13,83))
            if CHECK_PARAMETER.r_button.lower()=="pdflatex":
                dir=os.getcwd()
                files = glob.glob(dir+"\\{}".format("resources\\*"))
                for f in files:
                    try:
                        os.remove(f)
                    except:
                        pass
                m=random.randint(0,10000000)

                pdff=dir+"//resources//{}.pdf".format(m)
                self.Scorm.convertMdToPdf(CHECK_PARAMETER.file_input,pdff)  
                self.progressBar_2.setValue(100)
                CHECK_PARAMETER.file_out=pdff
                self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.pdf".format(m)), None))
            elif CHECK_PARAMETER.r_button.lower()=="scorm":
                dir=os.getcwd()
                files = glob.glob(dir+"\\{}".format("resources\\*"))
                for f in files:
                    try:
                        os.remove(f)
                    except:
                        pass
                m=random.randint(0,10000000)
                fileoutputhtml=dir+"//resources//{}.html".format(m)
                m=random.randint(0,10000000)
                fileoutputpdf=dir+"//resources//{}.pdf".format(m)
                m=random.randint(0,10000000)
                pname="{}".format(m)
                self.Scorm.convertMdToScorm(CHECK_PARAMETER.file_input,fileoutputhtml,fileoutputpdf,pname)  
                self.progressBar_2.setValue(100)
                pname=dir+"//{}".format(m)
                CHECK_PARAMETER.file_out=pname+".zip"
                self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.zip".format(m)), None))
        else :
            
            self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"{}".format("The file extension is not valid"), None))
    def updateLabel(self, _):
        if self.radioButton_3.isChecked() == True:
            print("========================= 2")
            print(self.radioButton_3.text())
            CHECK_PARAMETER.r_button=self.radioButton_3.text() 
        if self.radioButton_4.isChecked() == True:
            print("========================= 1")
            print(self.radioButton_4.text())
            CHECK_PARAMETER.r_button=self.radioButton_4.text()
    def openFile(self,file):
        if sys.platform == 'linux2':
            subprocess.call(["xdg-open", file])
        else:
            os.startfile(file)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 292)
        MainWindow.setFixedSize(645, 292)
        MainWindow.setMinimumSize(QSize(401, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 591, 231))
        self.frame.setMinimumSize(QSize(591, 231))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progressBar_2 = QProgressBar(self.frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(50, 160, 521, 20))
        self.progressBar_2.setMinimumSize(QSize(521, 20))
        self.progressBar_2.setValue(0)
        
        
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.clicked.connect(lambda:self.uploadFile(MainWindow))
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 70, 91, 24))
        self.pushButton_4.setMinimumSize(QSize(91, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.clicked.connect(lambda:  self.convert(MainWindow))
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(440, 70, 91, 24))
        self.pushButton_5.setMinimumSize(QSize(91, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 20, 141, 21))
        self.label_4.setMinimumSize(QSize(141, 21))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 70, 141, 51))
        self.label_5.setMinimumSize(QSize(141, 51))
        self.label_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.toggled.connect(self.updateLabel)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(60, 110, 89, 20))
        self.radioButton_3.setMinimumSize(QSize(89, 20))
        self.radioButton_4 = QRadioButton(self.frame)
        self.radioButton_4.toggled.connect(self.updateLabel)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(60, 130, 89, 20))
        self.radioButton_4.setMinimumSize(QSize(89, 20))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 200, 141, 21))
        self.label_6.setMinimumSize(QSize(141, 21))
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.clicked.connect(lambda:self.openFile(CHECK_PARAMETER.file_out))
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(210, 200, 350, 24))
        self.pushButton_6.setMinimumSize(QSize(91, 24))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 180, 611, 21))
        self.line_3.setMinimumSize(QSize(611, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 0, 621, 271))
        self.tableView.setMinimumSize(QSize(621, 271))
        MainWindow.setCentralWidget(self.centralwidget)
        self.tableView.raise_()
        self.frame.raise_()
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">Scorm/Pdf Convertor</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Your Selected File</span></p><p align=\"center\"><span style=\" color:#ffffff;\"></span></p></body></html>", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Pdf", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Scorm", None))
        self.radioButton_3.setChecked(True)
        self.radioButton_4.setChecked(True)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your File  ==========&gt;&gt; clicked for show </p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi




app = QApplication([])
form = Ui_MainWindow()
m=form.setupUi(QMainWindow())
m.show()

sys.exit(app.exec())


