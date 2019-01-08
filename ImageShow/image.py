import sys
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QImageReader, QLayout
from PyQt5.QtWidgets import QVBoxLayout
import mysql.connector
#from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
    
    file = ""
    curFileId = 1

    def showImage(self,filepath):
        
        self.label.clear()
        print("from showImage function: ", filepath)
        '''
        #self.label = QLabel(self)
        self.pixmap = QPixmap(filepath)
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(50,20,550,400)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        #self.initUI
        #self.label1.show()
        
        self.label1 = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label1)
        
        #self.label1 = QLabel(self)
        
        image = QImage(QImageReader(filepath).read())
        label1.setPixmap(QPixmap(image))
        
        pixmap = QPixmap(filepath)
        label1.setPixmap(self.pixmap)
        label1.setGeometry(50,20,550,400)
        label1.show()
        '''
        pixmap=QtGui.QPixmap(filepath)
        pixmap=pixmap.scaled(self.label.width(),
            self.label.height(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #print("doesn't show")
        
    def on_click_prev(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database = "imageDB"
            #auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor()
        #global curFileId
        if (App.curFileId-1) < 1:
            self.buttonP.hide()
        else:
            
            #myCursor.execute("SELECT Path FROM ImagePath where Image_ID = %s",(App.curFileId-1))
            sql = "SELECT Path FROM ImagePath where Image_ID = %s"
            val = (App.curFileId-1 ,)
            myCursor.execute(sql,val)
            result = myCursor.fetchone()
            for record in result:
                print(record)
                #file = record
                self.showImage(record)
                #global curFileId
                App.curFileId -= 1
                record = ""
        myCursor.close()
        mydb.close()
                
    def on_click_next(self):
        print("in next click")
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database = "imageDB"
            #auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor()
       
        myCursor.execute("SELECT Path FROM ImagePath")
        myresult = myCursor.fetchall()
        total = myCursor.rowcount
        
        #global curFileId
        
        print(" total: ",total, " curFileId: ", App.curFileId)
        if (App.curFileId+1) > total:
            self.buttonN.hide()
        else:
            #global curFileId
            #myCursor.execute("SELECT Path FROM ImagePath where Image_ID = %s", (App.curFileId+1))
            sql = "SELECT Path FROM ImagePath where Image_ID = %s"
            val = (App.curFileId+1 ,)
            myCursor.execute(sql,val)
            myresult = myCursor.fetchone()
            for data in myresult:
                print(data)
                #file = record
                self.showImage(data)
                #global curFileId
                App.curFileId += 1
                data = ""
        myCursor.close()
        mydb.close()
        
    def __init__(self):
        super().__init__()

        
        
        self.title = 'Learning Though Images'
        self.left = 200
        self.top = 150
        self.width = 1200#680
        self.height = 800#480
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    #=========================================Video Part===============================================#
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        
        self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile
                                  ("F:\StudyMaterials\Python Exercises\Videos\ARBOVIRUS__HARIYE_JAO.mp4")))
        self.playButton.setEnabled(True)
           
        # Create a widget for window contents
        mainlayout = QLayout(self)
        self.setLayout(mainlayout)
        
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(650, 20, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        mainlayout.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)


    #=====================================================================================#
        
    # Image  widget
        self.label = QLabel(self)
        self.pixmap = QPixmap('F:\StudyMaterials\Python_pyQt5\Images\Green_Mango.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(50,20,550,400)
        #self.resize(pixmap.width(),pixmap.height())
        #self.resize(640,450)
        
    # Previous button widget
        self.buttonP = QPushButton('Previous', self)
        self.buttonP.setToolTip('Go to previous picture')
        self.buttonP.move(100,420)
        self.buttonP.clicked.connect(self.on_click_prev)
        
    # Next button widget
        self.buttonN = QPushButton('Next', self)
        self.buttonN.setToolTip('Go to next picture')
        self.buttonN.move(400,420)
        self.buttonN.clicked.connect(self.on_click_next)
     
        self.show()


    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

          
        
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = App()
    sys.exit(app.exec_())
