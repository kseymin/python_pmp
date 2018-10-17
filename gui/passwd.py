import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.passwdLayout import *
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class mypasswdLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """버튼클릭Layout과 비번설정 함수를 연결"""
        self.ui.pushButton.clicked.connect(self.pushButton_clickedEvent)  # 비번설정버튼

    """패스워드 넣는 함수"""
    def pushButton_clickedEvent(self):
        # 메세지박스 띄우기
        reply = QtWidgets.QMessageBox.question(self, "규칙 설정", "해당 비밀번호로 설정하시겠습니까?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        # 메시지박스에서 Yes클릭시-
        if reply == QtWidgets.QMessageBox.Yes:
            # 입력 칸에 넣은 값을 텍스트로 받아와서 passwd에 저장
            passwd = self.ui.lineEdit.text()
            print(passwd)

def make_pwd_qt():
    app = QtWidgets.QApplication(sys.argv)
    myapp = mypasswdLayout()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = mypasswdLayout()
    myapp.show()
    sys.exit(app.exec_())