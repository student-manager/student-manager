# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updtr.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/sources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.log = QtWidgets.QListWidget(Form)
        self.log.setGeometry(QtCore.QRect(10, 10, 361, 251))
        self.log.setObjectName("log")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(160, 300, 61, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Обновление базы данных"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.pushButton.setText(_translate("Form", "Finish"))
import source_rc