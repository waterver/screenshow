import sys
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon,  QPixmap,   QPainter,QPalette,QBrush
from PyQt5.QtCore import QCoreApplication,QTimer
from PyQt5.QtCore import Qt

class PromptText(QWidget):  #弹窗显示
    def __init__(self,parent=None):
        super().__init__() 
        self.setWindowTitle('垃圾类别')
        self.initUI()


    def initUI(self):
        win=QWidget()
        desk=QApplication.desktop()
        screenRect = desk.screenGeometry()
        self.h=screenRect.height()
        self.w=screenRect.width()
        self.palette = QPalette()
        self.textbox = QLabel(self)
        self.textbox.resize(self.w,self.h)
        self.textbox.setAlignment(Qt.AlignCenter)
        self.textbox.setStyleSheet('font:bold 100px;')
        self.textbox.setWindowOpacity(0.3)
        
    def labelchange(self,num=5):
        # self.palette.setBrush(QPalette.Background,QBrush(QPixmap('./pyqt5/backg.jpeg')))
        if num == 1:

            jpg=QPixmap('./pyqt5/backg.jpeg')
            self.jpg=jpg.scaled(self.w,self.h)
            self.textbox.setText("可回收垃圾")
        elif num == 2:

            jpg=QPixmap('./pyqt5/12.jpg')
            self.jpg=jpg.scaled(self.w,self.h)
            self.textbox.setText("厨余垃圾")
        elif num == 3:

            jpg=QPixmap('./pyqt5/backg.jpeg')
            self.jpg=jpg.scaled(self.w,self.h)
            self.textbox.setText("有害垃圾")
        elif num == 4 :

            jpg=QPixmap('./pyqt5/backg.jpeg')
            self.jpg=jpg.scaled(self.w,self.h)
            self.textbox.setText("其他垃圾")
        
        self.palette.setBrush(QPalette.Background,QBrush(self.jpg))  
        self.setPalette(self.palette)
        self.timer = QTimer()
        if num>=5:
            self.timer.start(0)
        else:
            self.timer.start(3000)
            self.showFullScreen()
        self.timer.timeout.connect(self.close)

class MAINWINDOW(QWidget):    #主窗口调用
    def __init__(self):
        super().__init__()
        self.tur=1
        # self.ex = jiemian(self)#调用
        self.mainn()
        
    def mainn(self):
        main=QWidget()
        self.setWindowTitle('垃圾分类汇总')
        #self.showFullScreen()
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(),screen.height())
        
        self.move(0,0)
        self.textbox = QTextEdit(self)
        self.textbox.move(100, 50)
        self.textbox.resize(screen.width()/2-100, screen.height()-100)
        self.textbox.setFontPointSize(60)
        self.table= QTableWidget(4,2)
        self.table.move(screen.width()/2,0)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.verticalHeader().setDefaultSectionSize(300)
        
        self.show()

    def addvalue(self,num=None):
        if num>4 or num<=0 or num==None:
            return

        if num==1:
            self.str="%d\t可回收垃圾"%self.tur
        elif num==2:
            self.str="%d\t厨余垃圾"%self.tur
        elif num==3:
            self.str="%d\t有害垃圾"%self.tur
        elif num==4:
            self.str="%d\t其他垃圾"%self.tur   
        self.textbox.append(self.str)
        self.tur+=1

if __name__=="__main__":
    app = QApplication(sys.argv)
    window1=MAINWINDOW()
    window2=PromptText()
    while True:
        x=int(input("Please input the number of the rubbish:"))
        window2.labelchange(x)
        window1.addvalue(x)
    app.exec_()