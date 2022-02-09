# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self, localeData):
        self.localeData = localeData
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 558)
        Form.setMinimumSize(QtCore.QSize(418, 558))
        Form.setMaximumSize(QtCore.QSize(418, 558))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/sources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(100, 10, 231, 51))
        self.title.setObjectName("title")
        self.logIN = QtWidgets.QGroupBox(Form)
        self.logIN.setGeometry(QtCore.QRect(30, 60, 351, 201))
        self.logIN.setObjectName("logIN")
        self.passwordEnter = QtWidgets.QLineEdit(self.logIN)
        self.passwordEnter.setEnabled(True)
        self.passwordEnter.setGeometry(QtCore.QRect(10, 140, 141, 20))
        self.passwordEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEnter.setObjectName("passwordEnter")
        self.userList = QtWidgets.QListWidget(self.logIN)
        self.userList.setGeometry(QtCore.QRect(10, 20, 331, 101))
        self.userList.setObjectName("userList")
        self.usernameEnter = QtWidgets.QLineEdit(self.logIN)
        self.usernameEnter.setEnabled(True)
        self.usernameEnter.setGeometry(QtCore.QRect(10, 120, 141, 20))
        self.usernameEnter.setObjectName("usernameEnter")
        self.showPassword = QtWidgets.QCheckBox(self.logIN)
        self.showPassword.setEnabled(True)
        self.showPassword.setGeometry(QtCore.QRect(10, 160, 131, 17))
        self.showPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showPassword.setObjectName("showPassword")
        self.auth = QtWidgets.QPushButton(self.logIN)
        self.auth.setGeometry(QtCore.QRect(230, 170, 101, 23))
        self.auth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auth.setObjectName("auth")
        self.registerGroup = QtWidgets.QGroupBox(Form)
        self.registerGroup.setGeometry(QtCore.QRect(30, 270, 351, 231))
        self.registerGroup.setObjectName("registerGroup")
        self.set_group = QtWidgets.QComboBox(self.registerGroup)
        self.set_group.setGeometry(QtCore.QRect(140, 50, 161, 22))
        self.set_group.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_group.setObjectName("set_group")
        self.login = QtWidgets.QLineEdit(self.registerGroup)
        self.login.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.login.setObjectName("login")
        self.middleName = QtWidgets.QLineEdit(self.registerGroup)
        self.middleName.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.middleName.setObjectName("middleName")
        self.name = QtWidgets.QLineEdit(self.registerGroup)
        self.name.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.name.setObjectName("name")
        self.text = QtWidgets.QLabel(self.registerGroup)
        self.text.setGeometry(QtCore.QRect(140, 20, 191, 16))
        self.text.setObjectName("text")
        self.createAccount = QtWidgets.QPushButton(self.registerGroup)
        self.createAccount.setGeometry(QtCore.QRect(120, 200, 111, 23))
        self.createAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createAccount.setObjectName("createAccount")
        self.applyPassword = QtWidgets.QCheckBox(self.registerGroup)
        self.applyPassword.setGeometry(QtCore.QRect(140, 80, 211, 17))
        self.applyPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyPassword.setObjectName("applyPassword")
        self.passwordEnter_2 = QtWidgets.QLineEdit(self.registerGroup)
        self.passwordEnter_2.setGeometry(QtCore.QRect(140, 100, 141, 20))
        self.passwordEnter_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEnter_2.setObjectName("passwordEnter_2")
        self.showPassword_2 = QtWidgets.QCheckBox(self.registerGroup)
        self.showPassword_2.setGeometry(QtCore.QRect(140, 120, 131, 17))
        self.showPassword_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showPassword_2.setObjectName("showPassword_2")
        self.typeLearn = QtWidgets.QComboBox(self.registerGroup)
        self.typeLearn.setGeometry(QtCore.QRect(10, 130, 113, 22))
        self.typeLearn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.typeLearn.setObjectName("typeLearn")
        self.typeLearn.addItem("")
        self.typeLearn.addItem("")
        self.typeLearn.addItem("")
        self.typeLearn.addItem("")
        self.text_LT = QtWidgets.QLabel(self.registerGroup)
        self.text_LT.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.text_LT.setObjectName("text_LT")
        self.age = QtWidgets.QSpinBox(self.registerGroup)
        self.age.setGeometry(QtCore.QRect(10, 190, 42, 22))
        self.age.setMinimum(12)
        self.age.setMaximum(65)
        self.age.setProperty("value", 18)
        self.age.setObjectName("age")
        self.textAge = QtWidgets.QLabel(self.registerGroup)
        self.textAge.setGeometry(QtCore.QRect(10, 160, 101, 16))
        self.textAge.setObjectName("textAge")
        self.addGroup = QtWidgets.QPushButton(self.registerGroup)
        self.addGroup.setGeometry(QtCore.QRect(310, 50, 31, 23))
        self.addGroup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addGroup.setObjectName("addGroup")
        self.applyDarkTheme = QtWidgets.QCheckBox(Form)
        self.applyDarkTheme.setGeometry(QtCore.QRect(10, 530, 231, 17))
        self.applyDarkTheme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyDarkTheme.setObjectName("applyDarkTheme")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 530, 41, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.localeData['authTitle']))
        self.title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">%s<br/></span>%s</p></body></html>" % (self.localeData['progamName'], self.localeData['authTitle'])))
        self.logIN.setTitle(_translate("Form", self.localeData["logIn_Text"]))
        self.passwordEnter.setPlaceholderText(_translate("Form", self.localeData['passwordText']))
        self.usernameEnter.setPlaceholderText(_translate("Form", self.localeData['loginText']))
        self.showPassword.setText(_translate("Form", self.localeData['showPassword']))
        self.auth.setText(_translate("Form", self.localeData["auth_act"]))
        self.registerGroup.setTitle(_translate("Form", self.localeData["regText"]))
        self.login.setPlaceholderText(_translate("Form", self.localeData['loginText']))
        self.middleName.setPlaceholderText(_translate("Form", self.localeData["middleNameText"]))
        self.name.setPlaceholderText(_translate("Form", self.localeData["nameText"]))
        self.text.setText(_translate("Form", self.localeData["group_t"]))
        self.createAccount.setText(_translate("Form", self.localeData["createProfileButton"]))
        self.applyPassword.setText(_translate("Form", self.localeData["wantProtect"]))
        self.passwordEnter_2.setPlaceholderText(_translate("Form", self.localeData["passsword"]))
        self.showPassword_2.setText(_translate("Form", self.localeData["show_passsword"]))
        self.typeLearn.setItemText(0, _translate("Form", f"{self.localeData['budget']} ({self.localeData['hereLearn']})"))
        self.typeLearn.setItemText(1, _translate("Form", f"{self.localeData['budget']} ({self.localeData['distantLearn']})"))
        self.typeLearn.setItemText(2, _translate("Form", f"{self.localeData['сommerce']} ({self.localeData['hereLearn']})"))
        self.typeLearn.setItemText(3, _translate("Form", f"{self.localeData['сommerce']} ({self.localeData['distantLearn']})"))
        self.text_LT.setText(_translate("Form", self.localeData['сommerce']))
        self.textAge.setText(_translate("Form", self.localeData['ageTxt']))
        self.addGroup.setText(_translate("Form", "+"))
        self.applyDarkTheme.setText(_translate("Form", f"{self.localeData['activateDarkTheme']} (β)"))
        self.label.setText(_translate("Form", "v. 1.1.1"))
import source_rc
