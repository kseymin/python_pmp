import sys
from passwordLayout import *
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtTest

class pwLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_PWWindow()
        self.ui.setupUi(self)

        """UI 각종 이벤트(버튼클릭 등)와 함수를 연결"""
        self.ui.pushButtonPw.clicked.connect(self.pushButtonPw_clickedEvent)  #  비번입력OK버튼
        self.setFixedSize(self.size())

    def pushButtonPw_clickedEvent(self):
        passwd = str(self.ui.lineEditPw.text())

        print(passwd)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mypwLayout = pwLayout()
    mypwLayout.show()
    sys.exit(app.exec_())  # 없으면 창 바로 꺼짐

if __name__ == '__main__':
    main()
