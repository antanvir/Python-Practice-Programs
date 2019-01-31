from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys



def window():
    app = QApplication(sys.argv)
    wid = QWidget()
    wid.setGeometry(10, 10, 640, 500)

    mediaPlayer = QMediaPlayer()

    videoWidget = QVideoWidget()
    videoWidget.move(10, 10)
    lay = QHBoxLayout()
    lay.addWidget(videoWidget)
    wid.setLayout(lay)

    mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(
        "F:\StudyMaterials\Python Exercises\Videos\ARBOVIRUS__HARIYE_JAO.mp4")))
    mediaPlayer.setVideoOutput(videoWidget)

    #videoWidget.show()
    mediaPlayer.play()
    wid.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

