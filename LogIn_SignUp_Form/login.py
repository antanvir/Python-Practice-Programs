# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 341)
        self.log_form = QtWidgets.QLabel(Dialog)
        self.log_form.setGeometry(QtCore.QRect(150, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.log_form.setFont(font)
        self.log_form.setObjectName("log_form")
        self.u_name = QtWidgets.QLabel(Dialog)
        self.u_name.setGeometry(QtCore.QRect(60, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.u_name.setFont(font)
        self.u_name.setObjectName("u_name")
        self.pass1 = QtWidgets.QLabel(Dialog)
        self.pass1.setGeometry(QtCore.QRect(60, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pass1.setFont(font)
        self.pass1.setObjectName("pass")
        self.text_u_name = QtWidgets.QLineEdit(Dialog)
        self.text_u_name.setGeometry(QtCore.QRect(150, 120, 261, 31))
        self.text_u_name.setObjectName("text_u_name")
        self.text_pass = QtWidgets.QLineEdit(Dialog)
        self.text_pass.setGeometry(QtCore.QRect(150, 170, 261, 31))
        self.text_pass.setObjectName("text_pass")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(310, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.signUp = QtWidgets.QPushButton(Dialog)
        self.signUp.setGeometry(QtCore.QRect(150, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setObjectName("signUp")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(60, 80, 351, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LOG IN FORM"))
        self.log_form.setText(_translate("Dialog", "Log In Form"))
        self.u_name.setText(_translate("Dialog", "Username"))
        self.pass1.setText(_translate("Dialog", "Password"))
        self.login.setText(_translate("Dialog", "LogIn"))
        self.signUp.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

