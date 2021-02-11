import sys
from PyQt5.QtWidgets import QWidget,QLabel,QTextEdit,QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QHeaderView,QSizePolicy,QGraphicsOpacityEffect
from PyQt5.QtCore import Qt,QDate
from PyQt5.QtGui import QFont,QMovie,QPixmap
# from PyQt import QBrush

class MAINWINDOW(QWidget):
    def __init__(self):
        super(MAINWINDOW,self).__init__()
        self.num=1      #history
        self.total=[0,0,0,0]
        # #获取窗口尺寸
        # desk=QApplication.desktop()
        # screenrect=desk.screenGeometry()
        # self.screen_heigh=screenrect.height()
        # self.screen_width=screenrect.width()
        self.mainwindow()
        self.setWindowTitle('垃圾分类汇总')
        self.resize(1024,768)
        # self.setWindowOpacity(0.9)
        # self.show()
        # self.showFullScreen()

    def mainwindow(self):

        self.lefthistory()
        self.rightall()

        self.mainlayout=QHBoxLayout()
        self.mainlayout.addLayout(self.leftlayout,1)
        self.mainlayout.addLayout(self.rightlayout,1)
        self.setLayout(self.mainlayout)
        self.show()
        # self.mainlayout.setGeometry(0,0,self.screen_width,self.screen_heigh)

    def lefthistory(self):  #左侧历史
        # self.leftlayout=QGroupBox()
        self.leftlayout=QVBoxLayout()

        self.history_title=QLabel("History")
        # self.history_title.setAlignment(Qt.AlignCenter)
        self.history_title.setStyleSheet('font:bold 20px;')
        # self.history_title.setText("History")

        self.history_textbox=QTextEdit(self)
        self.history_textbox.setFontPointSize(50)
        self.history_textbox.setFocusPolicy(Qt.NoFocus)
        self.history_textbox.setMinimumWidth(500)
        self.leftlayout.addWidget(self.history_title,0,Qt.AlignTop|Qt.AlignCenter)
        # self.leftlayout.setSpacing(50)
        self.leftlayout.addWidget(self.history_textbox)
        # self.leftlayout.setLayout(layout)
    
    def rightall(self): #右侧三个窗口
        self.rightlayout=QVBoxLayout()
        
        self.sum_title=QLabel("统计：")
        self.sum_table=QTableWidget(4,2)
        # self.sum_table.setRowCount(4)
        # self.sum_table.setColumnCount(2)
        self.sum_table.setHorizontalHeaderLabels(['类型', '数量'])
        self.sum_table.verticalHeader().setVisible(False)
        self.sum_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sum_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sum_table.setFocusPolicy(Qt.NoFocus)
        # self.sum_table.setMaximumHeight(600)

        self.positions=[(i,j) for i in range(4) for j in range(2)]
        temp=['可回收垃圾','%d'%self.total[0],'厨余垃圾','%d'%self.total[1],'有害垃圾','%d'%self.total[2],'其他垃圾','%d'%self.total[3]]
        for position,value in zip(self.positions,temp):
            # print(position,value)
            item=QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignCenter)
            self.sum_table.setItem(*position, QTableWidgetItem(item))

        # layout_top=QFormLayout()

        # layout_middle=QHBoxLayout()
        # self.movie=QMovie('./bin.gif')
        self.pic=QPixmap('./pic2.png')
        self.pic=self.pic.scaled(400,600,Qt.KeepAspectRatio)
        self.gif=QLabel()
        # self.gif.setMovie(self.movie)
        # self.movie.start()
        # self.gif.setMaximumSize(200,200)
        self.gif.setPixmap(self.pic)
        # self.gif.setGraphicsEffect(QGraphicsOpacityEffect().setOpacity(0.4))
        # self.gif.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        

        #下方状态
        self.data=QLabel('%s'%QDate.currentDate().toString())
        self.logo=QLabel("504robot_club")

        self.logo.setFont(QFont("方正舒体"))
        self.logo.setStyleSheet("font:20px;")
        self.state_light=QLabel()
        self.free=QPixmap('./green.png')
        self.rush=QPixmap('./red.png')
        self.state_light.setPixmap(self.free)
        self.state_light.setMaximumSize(12,12)
        self.state=QLabel("空闲")

        
        layout_bottom=QHBoxLayout()
        layout_bottom.addWidget(self.logo,1,Qt.AlignBottom|Qt.AlignLeft)
        layout_bottom.addWidget(self.data,1,Qt.AlignBottom|Qt.AlignVCenter)
        layout_bottom.addWidget(self.state_light,0,Qt.AlignBottom|Qt.AlignRight)
        layout_bottom.addWidget(self.state,0,Qt.AlignBottom|Qt.AlignRight)

        self.rightlayout.setSpacing(15)
        self.rightlayout.addWidget(self.sum_title)
        self.rightlayout.addWidget(self.sum_table,0,Qt.AlignTop)
        self.rightlayout.addWidget(self.gif,1,Qt.AlignCenter)
        # self.rightlayout.setStretch(1
        self.rightlayout.addLayout(layout_bottom)
        # self.rightlayout.addLayout()

        # self.rightlayout.addLayout(laytop)



    def addvalue(self,num=None):
        if num>=4 or num<0 or num==None:
            return
        self.state_light.setPixmap(self.free)
        self.state.setText("空闲")
        self.total[num]+=1

        if num==0:
            self.str="%d\t可回收垃圾"%self.num
        elif num==1:
            self.str="%d\t厨余垃圾"%self.num
        elif num==2:
            self.str="%d\t有害垃圾"%self.num
        elif num==3:
            self.str="%d\t其他垃圾"%self.num   
        item=QTableWidgetItem('%d'%self.total[num])
        item.setTextAlignment(Qt.AlignCenter)
        self.sum_table.setItem(num,1,item)
        self.history_textbox.append(self.str)
        self.num+=1
    
    def detect(self):
        self.state_light.setPixmap(self.rush)
        self.state.setText("识别中")



if __name__=="__main__":
    app = QApplication(sys.argv)
    window1=MAINWINDOW()
    while True:
        x=int(input("Please input the number of the rubbish:"))
        # window2.labelchange(x)
        if x>4:
            window1.detect()
        else:
            window1.addvalue(x)
        

    app.exec_()