# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_SIGNUPFORM(object):

    def showMessage(self, msgType, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Warning)
        messageBox.setWindowTitle(msgType)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
        
    def infoInsertion(self):

        fname = self.text_u_name.text()
        uname = self.text_pass.text()
        mail = self.text_u_name_2.text()
        upass = self.text_pass_2.text()
        cpass = self.text_u_name_3.text()

        print(upass, " ", cpass)

        if upass == cpass:
            mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                passwd = "ant904",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
            myCursor = mydb.cursor()

            '''fname = self.text_u_name.text()
            uname = self.text_pass.text()
            mail = self.text_u_name_2.text()
            upass = self.text_pass_2.text()'''
        
            sql = "INSERT INTO Users(name, Username, Email, Password) VALUES(%s, %s, %s, %s)"
            val = (fname, uname, mail, upass) 

            myCursor.execute(sql, val)
            mydb.commit()
            myCursor.close()
            mydb.close()
            ##
            messageBox = QtWidgets.QMessageBox()
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            messageBox.setWindowTitle("Account Creation")
            messageBox.setText("Sign Up completed!\nUse username & password to log in.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
            messageBox.exec_()
            
        else:
            self.showMessage("Retry", 'Password mismatched!\nTry again.')
        
    def setupUi(self, SIGNUPFORM):
        SIGNUPFORM.setObjectName("SIGNUPFORM")
        SIGNUPFORM.resize(480, 441)
        SIGNUPFORM.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(165, 207, 156, 255), stop:0.55 rgba(206, 214, 210, 255), stop:0.98 rgba(241, 255, 225, 255), stop:1 rgba(0, 0, 0, 0))")
        self.log_form = QtWidgets.QLabel(SIGNUPFORM)
        self.log_form.setGeometry(QtCore.QRect(150, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.log_form.setFont(font)
        self.log_form.setObjectName("log_form")
        self.text_u_name = QtWidgets.QLineEdit(SIGNUPFORM)
        self.text_u_name.setGeometry(QtCore.QRect(170, 110, 261, 31))
        self.text_u_name.setObjectName("text_u_name")
        self.u_name = QtWidgets.QLabel(SIGNUPFORM)
        self.u_name.setGeometry(QtCore.QRect(40, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.u_name.setFont(font)
        self.u_name.setObjectName("u_name")
        self.nm2 = QtWidgets.QLabel(SIGNUPFORM)
        self.nm2.setGeometry(QtCore.QRect(40, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.nm2.setFont(font)
        self.nm2.setObjectName("pass")
        self.text_pass = QtWidgets.QLineEdit(SIGNUPFORM)
        self.text_pass.setGeometry(QtCore.QRect(170, 160, 261, 31))
        self.text_pass.setObjectName("text_pass")
        self.text_u_name_2 = QtWidgets.QLineEdit(SIGNUPFORM)
        self.text_u_name_2.setGeometry(QtCore.QRect(170, 220, 261, 31))
        self.text_u_name_2.setObjectName("text_u_name_2")
        self.u_name_2 = QtWidgets.QLabel(SIGNUPFORM)
        self.u_name_2.setGeometry(QtCore.QRect(40, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_2.setFont(font)
        self.u_name_2.setObjectName("u_name_2")
        self.pass_2 = QtWidgets.QLabel(SIGNUPFORM)
        self.pass_2.setGeometry(QtCore.QRect(40, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pass_2.setFont(font)
        self.pass_2.setObjectName("pass_2")
        self.text_pass_2 = QtWidgets.QLineEdit(SIGNUPFORM)
        self.text_pass_2.setGeometry(QtCore.QRect(170, 270, 261, 31))
        self.text_pass_2.setObjectName("text_pass_2")
        self.u_name_3 = QtWidgets.QLabel(SIGNUPFORM)
        self.u_name_3.setGeometry(QtCore.QRect(40, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_3.setFont(font)
        self.u_name_3.setObjectName("u_name_3")
        self.text_u_name_3 = QtWidgets.QLineEdit(SIGNUPFORM)
        self.text_u_name_3.setGeometry(QtCore.QRect(170, 320, 261, 31))
        self.text_u_name_3.setObjectName("text_u_name_3")
        self.signUp = QtWidgets.QPushButton(SIGNUPFORM)
        self.signUp.setGeometry(QtCore.QRect(320, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setObjectName("signUp")

        ############## Button Event#############
        self.signUp.clicked.connect(self.infoInsertion)
        '''self.signUp.clicked.connect(
            p1 = self.text_pass_2.text()
            p2 = self.text_u_name_3.text()
            print(p1," ", p2)
            if p1 == p2:
                #self.signUp.clicked.connect(self.infoInsertion)
                print(p1," ", p2)
            else:
                 self.showMessage("Retry", 'Password mismatched :(\nTry again.')
        )'''
        ############################################
        
        self.line = QtWidgets.QFrame(SIGNUPFORM)
        self.line.setGeometry(QtCore.QRect(40, 70, 391, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(SIGNUPFORM)
        QtCore.QMetaObject.connectSlotsByName(SIGNUPFORM)

    def retranslateUi(self, SIGNUPFORM):
        _translate = QtCore.QCoreApplication.translate
        SIGNUPFORM.setWindowTitle(_translate("SIGNUPFORM", "Dialog"))
        self.log_form.setText(_translate("SIGNUPFORM", "Sign Up Form"))
        self.u_name.setText(_translate("SIGNUPFORM", "Name"))
        self.nm2.setText(_translate("SIGNUPFORM", "Username"))
        self.u_name_2.setText(_translate("SIGNUPFORM", "Email"))
        self.pass_2.setText(_translate("SIGNUPFORM", "Password"))
        self.u_name_3.setText(_translate("SIGNUPFORM", "Confirm Password"))
        self.signUp.setText(_translate("SIGNUPFORM", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIGNUPFORM = QtWidgets.QDialog()
    ui = Ui_SIGNUPFORM()
    ui.setupUi(SIGNUPFORM)
    SIGNUPFORM.show()
    sys.exit(app.exec_())

