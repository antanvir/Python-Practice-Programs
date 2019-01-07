import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
import mysql.connector
#from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
    
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = "root",
        passwd = "ant904",
        database = "imageDB"
        #auth_plugin='mysql_native_password'
    )
    myCursor = mydb.cursor()
    

    def showImage(self,filepath):
        label = QLabel(self)
        pixmap = QPixmap(filepath)
        label.setPixmap(pixmap)
        label.setGeometry(50,20,550,400)
        
    def on_click_prev(self, cid):
        if (cid-1) < 1:
            self.buttonP.hide()
        else:
            myCursor.execute("SELECT Path FROM ImagePath where Image_ID = cid-1")
            myresult = myCursor.fetchall()
            for records in myresult:
                print(records)
                file = record
                self.showImage(file)
                curFileId = cid-1
                
    def on_click_next(self, cid):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database = "imageDB"
            #auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor()
        '''
        sql = "SELECT Path FROM ImagePath where Image_ID = %d"
        val = ((cid+1))
        myCursor.execute(sql, val)
        '''
        myCursor.execute("SELECT Path FROM ImagePath")
        myresult = myCursor.fetchall()
        total = myCursor.rowcount

        print("cid: ",cid, " total: ",total, " curFileId: ", self.curFileId)
        if (cid+1) > total:
            self.buttonN.hide()
        else:
            myCursor.execute("SELECT Path FROM ImagePath where Image_ID = %s", (int(cid)))
            myresult = myCursor.fetchall()
            for records in myresult:
                print(records)
                file = record
                self.showImage(file)
                self.curFileId = cid+1
  
    def __init__(self):
        super().__init__()

        self.file = ""
        self.curFileID = 1
        
        self.title = 'Learning Though Images'
        self.left = 200
        self.top = 150
        self.width = 680
        self.height = 480
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
     
    # Image  widget
        label = QLabel(self)
        pixmap = QPixmap('F:\StudyMaterials\Python_pyQt5\Images\Green_Mango.jpg')
        label.setPixmap(pixmap)
        label.setGeometry(50,20,550,400)
        #self.resize(pixmap.width(),pixmap.height())
        #self.resize(640,450)

    # Previous button widget
        self.buttonP = QPushButton('Previous', self)
        self.buttonP.setToolTip('Go to previous picture')
        self.buttonP.move(100,420)
        self.buttonP.clicked.connect(lambda: self.on_click_prev(self.curFileID))
        
    # Next button widget
        self.buttonN = QPushButton('Next', self)
        self.buttonN.setToolTip('Go to next picture')
        self.buttonN.move(400,420)
        self.buttonN.clicked.connect(lambda: self.on_click_next(self.curFileID))
     
        self.show()

          
        
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = App()
    sys.exit(app.exec_())
