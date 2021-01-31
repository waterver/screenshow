import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QPalette, QBrush
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.Qt import QUrl


class VIDEOPLAYER(QMainWindow):
    def __init__(self, dir=None):
        super().__init__()
        self.setWindowTitle("Media")
        self.setWindowOpacity(0.95)
        # screen = QDesktopWidget().screenGeometry()
        # self.resize(screen.width(), screen.height())

        self.default_suffix = ['.mp4', '.flv', '.avi']
        self.default_list(dir)

        self.initUI()
    def default_list(self, dir=None):  # 获取视频资源
        self.list = []
        for f in sorted(os.listdir(dir)):
            for i in self.default_suffix:
                if f.endswith(i):
                    self.list.append(os.path.join(dir, f))
        print(self.list)

    # def change_list()
    def initUI(self):
        self.player = QMediaPlayer()
        self.widget = QVideoWidget()
        self.widget.showFullScreen()
        self.player.setVideoOutput(self.widget)
        if self.list != None:
            self.playlist = QMediaPlaylist(self)
            self.playlist.setPlaybackMode(self.playlist.Loop)  # 列表循环播放模式
            for i in self.list:
                self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(r'%s'%i)))
            # self.player.setMedia(QMediaContent(QUrl.fromLocalFile()))
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def __del__(self):
        self.player.stop()
        self.widget.close()
        print("over")
    # def
# class CONTROL(QWidget):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VIDEOPLAYER("E:/2020大三/工训/pyqt5/video")
    while True:
        if(input("exit with q：")=='q'):
            del player
            break
    app.exec_()
