from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget,QFileDialog)
import sys
from CHECK_PARAMETER import CHECK_PARAMETER
import subprocess
import os
from SCORM import Scorm
import random
import glob
class Ui_MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        self.Scorm=Scorm()
        
    def uploadFile(self,MainWindow):
        file_dialog = QFileDialog()
        file_path, file = file_dialog.getOpenFileName(MainWindow)
        dataf=file_path.split("/")
        file_name=dataf[len(dataf)-1]
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Your Selected File</span></p><p align=\"center\"><span style=\" color:#ffffff;\">{}</span></p></body></html>".format(file_name), None))
        CHECK_PARAMETER.file_input=file_path
        CHECK_PARAMETER.file_name=file_name
        self.progressBar.setValue(0)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"", None))
    def convert(self,MainWindow): 
        print("converting... !")
        print(CHECK_PARAMETER.file_input)
        print(CHECK_PARAMETER.r_button)
        dataf=CHECK_PARAMETER.file_input.split("/")
        file_name=dataf[len(dataf)-1]
        if file_name.lower().endswith(".md"):
            self.progressBar.setValue(random.randint(13,83))
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
                self.progressBar.setValue(100)
                CHECK_PARAMETER.file_out=pdff
                self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.pdf".format(m)), None))
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
                self.progressBar.setValue(100)
                pname=dir+"//{}".format(m)
                CHECK_PARAMETER.file_out=pname+".zip"
                self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"{}".format("{}.zip".format(m)), None))
        else :
            
            self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"{}".format("The file extension is not valid"), None))
    def updateLabel(self, _):
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
    

   
    def setupUi(self, MainWindow):
        def dragEnterEvent(event):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()
        def dropEvent( event):
                files = [u.toLocalFile() for u in event.mimeData().urls()]
                for f in files:
                    print(f)
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Convertor")
        MainWindow.setFixedSize(250, 525)
        MainWindow.resize(250, 525)
        MainWindow.setMinimumSize(QSize(401, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setAcceptDrops(True)
       
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 351, 501))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        #self.frame.setAcceptDrops(True)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(70, 20, 201, 31))
        self.pushButton_4.setMinimumSize(QSize(91, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton_4.clicked.connect(lambda:self.uploadFile(MainWindow))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 60, 201, 81))
        self.label_5.setMinimumSize(QSize(141, 51))
        self.label_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 0, 351, 171))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(0, 150, 351, 81))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 160, 141, 21))
        self.label_4.setMinimumSize(QSize(141, 21))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.toggled.connect(self.updateLabel)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(120, 180, 89, 20))
        self.radioButton_3.setMinimumSize(QSize(89, 20))
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.clicked.connect(lambda:  self.convert(MainWindow))
        self.pushButton_5.setGeometry(QRect(80, 280, 191, 24))
        self.pushButton_5.setMinimumSize(QSize(91, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        
        self.radioButton_5 = QRadioButton(self.frame)
        self.radioButton_5.toggled.connect(self.updateLabel)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(120, 200, 89, 20))
        self.radioButton_5.setMinimumSize(QSize(89, 20))
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 350, 341, 23))
        self.progressBar.setValue(24)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 460, 141, 21))
        self.label_7.setMinimumSize(QSize(141, 21))
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.clicked.connect(lambda:self.openFile(CHECK_PARAMETER.file_out))
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(230, 460, 91, 24))
        self.pushButton_7.setMinimumSize(QSize(91, 24))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(0, 420, 351, 81))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(0, 230, 351, 181))
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.radioButton_3.raise_()
        self.pushButton_5.raise_()
        self.radioButton_5.raise_()
        self.progressBar.raise_()
        self.label_7.raise_()
        self.pushButton_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("Convertor", u"Convertor", None))
        self.pushButton_4.setText(QCoreApplication.translate("Convertor", u"Upload File", None))
        self.radioButton_3.setChecked(True)
        self.radioButton_5.setChecked(True)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Your Selected File</span></p><p align=\"center\"><span style=\" color:#ffffff;\">text.html</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Convert To:</p><p align=\"center\"><br/></p></body></html>", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"SCORM", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"PdfLaTeX", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your File  ==========&gt;&gt; clicked for show </p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"text.html", None))
    # retranslateUi




app = QApplication([])
form = Ui_MainWindow()
m=form.setupUi(QMainWindow())
m.show()

sys.exit(app.exec())

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop")
        self.resize(720, 480)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())
