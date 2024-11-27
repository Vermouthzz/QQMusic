from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeMenu():
    def __init__(self, parent = None):
        pass
    
    def setupUi(self):
        online_music_layout = QtWidgets.QVBoxLayout()
        #  在线音乐标题
        self.label_title = QtWidgets.QLabel()
        self.label_title.setText('在线音乐')
        self.label_title.setObjectName('online_title')
        online_music_layout.addWidget(self.label_title)

        self.music_ = QtWidgets.QHBoxLayout()
        self.icon_music = 1
        self.music_name = QtWidgets.QLabel()
        self.music_.addWidget(self.icon_music)
        self.music_.addWidget(self.music_name)
        online_music_layout.addLayout(self.music_)


        my_music_layout = QtWidgets.QVBoxLayout()
        #  我的音乐标题
        self.label_title = QtWidgets.QLabel()
        self.label_title.setText('我的音乐')
        self.label_title.setObjectName('my_title')
        online_music_layout.addWidget(self.label_title)


        