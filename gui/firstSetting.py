# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstSetting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstSetting(object):
    def setupUi(self, FirstSetting):
        FirstSetting.setObjectName("FirstSetting")
        FirstSetting.resize(366, 274)
        self.centralwidget = QtWidgets.QWidget(FirstSetting)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPw = QtWidgets.QLabel(self.centralwidget)
        self.labelPw.setGeometry(QtCore.QRect(20, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.labelPw.setFont(font)
        self.labelPw.setObjectName("labelPw")
        self.lineEditPw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPw.setGeometry(QtCore.QRect(160, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.lineEditPw.setFont(font)
        self.lineEditPw.setObjectName("lineEditPw")
        self.lineEditPw.setEchoMode(QtWidgets.QLineEdit.Password)  #  비밀번호형식으로 마스킹해서 텍스트 입력
        self.labelReg = QtWidgets.QLabel(self.centralwidget)
        self.labelReg.setGeometry(QtCore.QRect(20, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.labelReg.setFont(font)
        self.labelReg.setObjectName("labelReg")
        self.pushButtonRegEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRegEdit.setGeometry(QtCore.QRect(210, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.pushButtonRegEdit.setFont(font)
        self.pushButtonRegEdit.setObjectName("pushButtonRegEdit")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(140, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 341, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 341, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        FirstSetting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FirstSetting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        FirstSetting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FirstSetting)
        self.statusbar.setObjectName("statusbar")
        FirstSetting.setStatusBar(self.statusbar)

        self.retranslateUi(FirstSetting)
        QtCore.QMetaObject.connectSlotsByName(FirstSetting)

    def retranslateUi(self, FirstSetting):
        _translate = QtCore.QCoreApplication.translate
        FirstSetting.setWindowTitle(_translate("FirstSetting", "FirstSetting"))
        self.labelPw.setText(_translate("FirstSetting", "Password Setting"))
        self.labelReg.setText(_translate("FirstSetting", "Registry Setting"))
        self.pushButtonRegEdit.setText(_translate("FirstSetting", "OK"))
        self.pushButtonStart.setText(_translate("FirstSetting", "Start"))

