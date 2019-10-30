from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QVBoxLayout
import pygame
from test2 import PickFile
from test2 import PickFile
import time
import os

class Ui_MusicMain(object):
    file = 'HarrySong-Ft-Kiss-Daniel-Reekado-Bank-Selense.mp3'
    # file = os.chdir('C:/Users/userx/Music/Adekunle Gold/GOLD')
    # songs = os.listdir()
    def setupUi(self, MusicMain):
        MusicMain.setObjectName("MusicMain")
        MusicMain.setFixedSize(299, 421)
        MusicMain.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.centralwidget = QtWidgets.QWidget(MusicMain)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Next.setGeometry(QtCore.QRect(210, 200, 71, 28))
        self.pushButton_Next.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 252, 252);\n"
"background-color: rgb(0, 3, 8);")
        self.pushButton_Next.setObjectName("pushButton_2")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(90, 200, 41, 28))
        self.pushButton_play.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 252, 252);\n"
"background-color: rgb(0, 3, 8);")
        self.pushButton_play.setObjectName("pushButton_3")
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(150, 200, 41, 28))
        self.pushButton_pause.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 252, 252);\n"
"background-color: rgb(0, 3, 8);")
        self.pushButton_pause.setObjectName("pushButton_4")
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setGeometry(QtCore.QRect(10, 200, 71, 28))
        self.pushButton_previous.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 252, 252);\n"
"background-color: rgb(0, 3, 8);")
        self.pushButton_previous.setObjectName("pushButton_5")
        self.label_displayUpper = QtWidgets.QLabel(self.centralwidget)
        self.label_displayUpper.setGeometry(QtCore.QRect(0, 10, 291, 171))
        self.label_displayUpper.setText("")
        self.label_displayUpper.setPixmap(QtGui.QPixmap("musicimage2.jpg"))
        self.label_displayUpper.setObjectName("label_displayUpper")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-40, 179, 351, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-20, 230, 361, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_displaylower = QtWidgets.QLabel(self.centralwidget)
        self.label_displaylower.setGeometry(QtCore.QRect(-6, 250, 311, 161))
        self.label_displaylower.setText("")
        self.label_displaylower.setObjectName("label_displaylower")
        MusicMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicMain)
        QtCore.QMetaObject.connectSlotsByName(MusicMain)
        self.pushButton_pause.clicked.connect(self.stopmusic)
        self.pushButton_play.clicked.connect(self.playbtn)
        self.pushButton_Next.clicked.connect(self.nextbtn)
        self.label_displaylower.setText(self.musicList)


    def musicList(self):
        pass


    def playbtn(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()

    def stopmusic(self):
       pygame.mixer.music.stop()


    def nextbtn(self):
        pass

    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def initMixer(self):
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN = self.getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)


    def retranslateUi(self, MusicMain):
        _translate = QtCore.QCoreApplication.translate
        MusicMain.setWindowTitle(_translate("MusicMain", "MusicPlayer"))
        self.pushButton_Next.setText(_translate("MusicMain", "Next"))
        self.pushButton_play.setText(_translate("MusicMain", "Play"))
        self.pushButton_pause.setText(_translate("MusicMain", "Pause"))
        self.pushButton_previous.setText(_translate("MusicMain", "Previous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusicMain = QtWidgets.QMainWindow()
    ui = Ui_MusicMain()
    ui.setupUi(MusicMain)
    MusicMain.show()
    sys.exit(app.exec_())

