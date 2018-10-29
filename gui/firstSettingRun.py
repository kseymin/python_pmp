
import sys
#from firstSetting import *
#from mainLayoutRun6 import *
import gui.firstSetting as firstSetting
import gui.mainLayoutRun as guiMain

from PyQt5 import QtCore, QtGui, QtWidgets
import cofig_make.config_manager as cm

class settingLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = firstSetting.Ui_FirstSetting()
        self.ui.setupUi(self)

        """UI 각종 이벤트(버튼클릭 등)와 함수를 연결"""
        self.ui.pushButtonRegEdit.clicked.connect(self.pushButtonRegEdit_clickedEvent)  #  레지스트리설정OK버튼
        self.ui.pushButtonStart.clicked.connect(self.pushButtonStart_clickedEvent)  #  스타트버튼 클릭
        self.setFixedSize(self.size())

    def pushButtonRegEdit_clickedEvent(self):
        """

        레지스트리 설정 함수

        """

    def pushButtonStart_clickedEvent(self):

        passwd = str(self.ui.lineEditPw.text())
        if passwd != '':
            self.close()  # 현재창 닫기
            self.mainWindow = pmpLayout()
            self.mainWindow.show()

            cm.configpasswd2(passwd)
            return passwd

        elif passwd == '':
            plzInputPasswd = QtWidgets.QMessageBox(self)
            plzInputPasswd.setWindowTitle("비밀번호 입력 오류")
            plzInputPasswd.setIcon(QtWidgets.QMessageBox.Warning)
            plzInputPasswd.setText("비밀번호를 제대로 입력하세요.")
            plzInputPasswd.exec_()
            return print("비밀번호를 입력하세요")

def main():

    """상태에 따라 초기세팅 진행화면 먼저 보여주고 시작할 것인지, 바로 시작할 것인지 나누는 구문"""
    a = int(input('1:초기세팅화면 보고 시작, 2:바로 시작 : '))      ################# 변경사항 이부분 수정해야됨
                                                                ################## 레지스트리 세팅안됐거나 비밀번호 세팅안됐을 시(처음시작시) a를 1로 세팅
                                                                ################## 레지스트리 세팅됐거나 비밀번호 세팅 됐을 시(처음 시작 아닐 시) a를 2로 세팅

    if a == 1:
        # 초기세팅 진행하고 시작
        app = QtWidgets.QApplication(sys.argv)
        mypwLayout = settingLayout()
        mypwLayout.show()
        sys.exit(app.exec_())

    elif a == 2:
        # 바로 시작
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = guiMain.pmpLayout()
        mainWindow.show()
        sys.exit(app.exec_())

    else:
        print("안됨")

if __name__ == '__main__':
    main()
