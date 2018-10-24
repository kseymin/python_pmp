# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PWWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Password")
        MainWindow.resize(287, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPw = QtWidgets.QLabel(self.centralwidget)
        self.labelPw.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.labelPw.setFont(font)
        self.labelPw.setObjectName("labelPw")
        self.lineEditPw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPw.setGeometry(QtCore.QRect(11, 40, 261, 31))
        self.lineEditPw.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(12)
        self.lineEditPw.setFont(font)
        self.lineEditPw.setObjectName("lineEditPw")
        self.pushButtonPw = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPw.setGeometry(QtCore.QRect(103, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        self.pushButtonPw.setFont(font)
        self.pushButtonPw.setObjectName("pushButtonPw")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Password", "Password"))
        self.labelPw.setText(_translate("Password", "Password"))
        self.pushButtonPw.setText(_translate("Password", "OK"))

