import sys
from passwordLayout import *
from PyQt5.QtCore import pyqtSignal

class comunicator :
    password = pyqtSignal()




class pwLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        self.p = comunicator()
        self.p.password.connet(self.getPassword())


        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_PWWindow()
        self.ui.setupUi(self)
        self.pwd = str()

        """UI 각종 이벤트(버튼클릭 등)와 함수를 연결"""
        self.ui.pushButtonPw.clicked.connect(self.pushButtonPw_clickedEvent)  #  비번입력OK버튼
        self.setFixedSize(self.size())




    def pushButtonPw_clickedEvent(self):

        passwd = str(self.ui.lineEditPw.text())
        self.pwd = passwd
        self.p.password.emit()
        self.close()


    def getPassword(self ):
        print('fuck plz',self.pwd)
        return  self.pwd





def main():
    app = QtWidgets.QApplication(sys.argv)
    mypwLayout = pwLayout()
    mypwLayout.show()


    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
