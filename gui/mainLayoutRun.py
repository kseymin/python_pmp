import sys
from PyQt5 import  QtGui, QtWidgets
import gui.mainLayout as mainLayout
from PyQt5.QtWidgets import  QInputDialog, QLineEdit
from PyQt5 import QtTest




import main_operator as mo
import proc_manager as pm



class secondWindow(QtWidgets.QDialog):  #  두번째 윈도우 창 (기능 제한 설정 창)

    def __init__(self):
        super(secondWindow, self).__init__()

        self.checkbox1 = QtWidgets.QCheckBox("메일 첨부 금지")
        self.checkbox2 = QtWidgets.QCheckBox("프린트 금지")

        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.button_box)
        self.setLayout(layout)
        self.setWindowTitle("기능 제한 설정")
        self.setMinimumWidth(50)

class pmpLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = mainLayout.Ui_PMP()
        self.ui.setupUi(self)

        """UI 각종 이벤트(버튼클릭 등)와 함수를 연결"""
        self.ui.pushButtonRuleApplyOk.clicked.connect(self.pushButtonApplyOk_clickedEvent)  #  규칙적용버튼
        self.ui.pushButtonRuleApplyNo.clicked.connect(self.pushButtonApplyNo_clickedEvent)  #  규칙해제버튼
        self.ui.pushButtonRuleAdd.clicked.connect(self.pushButtonAdd_clickedEvent)  #  규칙추가버튼
        self.ui.pushButtonRuleDelete.clicked.connect(self.pushButtonDelete_clickedEvent)  #  규칙제거버튼
        self.ui.pushButtonPasswd.clicked.connect(self.pushButtonPasswd_clickedEvent)  #  패스워드입력버튼
        self.ui.listWidgetRuleNo.itemDoubleClicked.connect(self.showLimitsetting)
        self.ui.pushButtonSearchWhole.clicked.connect(self.pushButtonSearchWhole_clickedEvent)  #  전체검색버튼
        self.ui.pushButtonSearchRT.clicked.connect(self.pushButtonSearchRT_clickedEvent)  #  리얼타임검색버튼
        self.ui.pushButtonStop.clicked.connect(self.pushButtonStop_clickedEvent)  #  STOP버튼
        self.ui.textBrowserSearch.setStyleSheet("background-image: url(mainImg8.png);")  #  백그라운드 이미지 삽입

        self.setFixedSize(self.size())

        self.stop = False  # Search 반복 탈출을 위한 플래그 변수 선언

    def pushButtonSearchWhole_clickedEvent(self):  #  전체검색클릭시 실행 함수

        """폰트설정"""
        myFont = self.ui.textBrowserSearch.font()
        f = QtGui.QFont(myFont)
        f.setPointSize(10)
        f.setFamily("Utsaah")
        f.setItalic(False)
        self.ui.textBrowserSearch.setFont(f)
        self.stop = False  # 반복시작을 위해 다시 반복탈출 플래그를 False로 세팅

        self.ui.textBrowserSearch.setStyleSheet("")  #  백그라운드 이미지 지우기
        self.ui.textBrowserSearch.setText("")  #  백그라운드 텍스트 초기화

        self.ui.pushButtonSearchWhole.setEnabled(False)  # 검색버튼 비활성화
        self.ui.pushButtonSearchRT.setEnabled(False)

        i = 0
        while i < 100:
            self.ui.textBrowserSearch.append('전체검색합니다. %d' % i)
            i = i + 1
            QtTest.QTest.qWait(100)  #  딜레이 속도 설정

            if self.stop is True:
                break

    def pushButtonSearchRT_clickedEvent(self):  #  리얼타임검색시 실행 함수

        """폰트설정"""
        myFont = self.ui.textBrowserSearch.font()
        f = QtGui.QFont(myFont)
        f.setPointSize(10)
        f.setFamily("Utsaah")
        f.setItalic(False)
        self.ui.textBrowserSearch.setFont(f)
        self.stop = False  # 반복시작을 위해 다시 반복탈출 플래그를 False로 세팅

        self.ui.textBrowserSearch.setStyleSheet("")  #  백그라운드 이미지 지우기
        self.ui.textBrowserSearch.setText("")  #  백그라운드 텍스트 초기화

        self.ui.pushButtonSearchWhole.setEnabled(False)  # 검색버튼 비활성화
        self.ui.pushButtonSearchRT.setEnabled(False)


        # self.ui.textBrowserSearch.append
        # #스탑
        # self.stop
        #

        # i = 0
        # while i < 100:
        #     self.ui.textBrowserSearch.append('리얼타임검색합니다. %d' % i)
        #     i = i + 1
        #     QtTest.QTest.qWait(100)  #  딜레이 속도 설정
        #
        #     if self.stop is True:
        #         break

        pname = 'POWERPNT'  # pname = [notepad, winword, POWERPNT, excel, AcroRd32]
        stopbutton_flag = self.stop


        ignore_list = list()

        while not stopbutton_flag:

            mo.realtime_processing(pname)

            for ignore in ignore_list:
                if ignore not in pm.get_proc_pid_list(pname):
                    ignore_list.remove(ignore)
            print(ignore_list)











    def pushButtonStop_clickedEvent(self):

        self.stop = True

        self.ui.textBrowserSearch.setText('중지합니다.')

        self.ui.pushButtonSearchWhole.setEnabled(True)  # 검색버튼 재활성화
        self.ui.pushButtonSearchRT.setEnabled(True)

        self.ui.textBrowserSearch.setStyleSheet("background-image: url(mainImg8.png); background-attachment: scroll;")  #  백그라운드 이미지 삽입

    """왼쪽 리스트에서 규칙 클릭하고 적용시, 규칙을 오른쪽으로 추가하는 부분"""
    def pushButtonApplyOk_clickedEvent(self):
        row = self.ui.listWidgetRuleNo.currentRow()  #  왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.item(row)  #  현재 클릭된 행(row)의 값(item)을 받아옴

        listWidgetRuleOk = self.ui.listWidgetRuleOK
        listWidgetRuleNo = self.ui.listWidgetRuleNo
        countListWidgetRuleOk = listWidgetRuleOk.count()
        countListWidgetRuleNo = listWidgetRuleNo.count()

        if item is None:  #  왼쪽 규칙 리스트에서 마우스 클릭을 안 해서 어떤 item도 선택되지 않았을 시-
            print("선택된 리스트(좌측)가 없습니다")
            return

        else:
            """오른쪽 리스트로 아이템 추가시, 아이템들 폰트 세팅"""
            myFont = listWidgetRuleOk.font()
            f = QtGui.QFont(myFont)
            f.setPointSize(14)
            f.setFamily("Utsaah")
            f.setItalic(False)
            listWidgetRuleOk.setFont(f)

            if countListWidgetRuleOk < 1:
                """오른쪽 리스트의 아이템 개수가 0일때는 그냥 추가 진행"""

                listWidgetRuleOk.addItem(str(item.text()))

                item = listWidgetRuleNo.takeItem(row)
                del item

                """self.ui.listWidgetRuleOk.addItem(str(item.text()))  #  왼쪽 규칙 리스트에서 선택된 아이템의 텍스트를 str형으로 받아서 오른쪽 규칙 리스트에 추가함
                item = self.ui.listWidgetRuleNo.takeItem(row)  #  왼쪽 리스트의 규칙은 삭제함
                del item"""

                print("설정완료")

            else:
                """오른쪽 리스트에 아이템이 하나라도 있을 때- 중복 비교 구문 시작"""
                listItems = []  #  리스트 아이템 받아올 배열 생성
                for index in range(countListWidgetRuleOk):  #  오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                    listItems.append(listWidgetRuleOk.item(index).text())  #  오른쪽 리스트의 아이템을 텍스트형태로 받아와서 listItems배열에 저장

                ruleDuplicateFlag = 0  #  아이템 동일한거 있는지 검사하는 플래그 변수 선언

                """추가할 왼쪽리스트 item의 text문과 listItems에 있는 아이템과 하나라도 동일한게 있는지 반복검사"""
                for i in range(len(listItems)):
                    if item.text() == listItems[i]:  #  동일한 규칙 추가 하려고 할 시,

                        ruleDuplicateFlag = 1  #  중복체크변수 1로 세팅

                        self.showNoDuplicate()  #  중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        continue

                if ruleDuplicateFlag == 0:
                    listWidgetRuleOk.addItem(str(item.text()))  #  반복검사 마치고 난 뒤 왼쪽 규칙 리스트에서 선택된 아이템의 텍스트를 str형으로 받아서 오른쪽 규칙 리스트에 추가함

                    """왼쪽 리스트의 설정은 삭제함"""
                    item = listWidgetRuleNo.takeItem(row)
                    del item
                    print("해당 규칙은 중복되지 않습니다.")
                    print("설정완료")

                else:
                    return

    """오른쪽 리스트에서 규칙 클릭하고 적용해제시, 규칙을 왼쪽으로 돌려놓는 부분"""
    def pushButtonApplyNo_clickedEvent(self):

        listWidgetRuleOk = self.ui.listWidgetRuleOK
        listWidgetRuleNo = self.ui.listWidgetRuleNo

        row = listWidgetRuleOk.currentRow()
        item = listWidgetRuleOk.item(row)

        if item is None:
            print("선택된 리스트(우측)가 없습니다.")
            return

        listWidgetRuleNo.addItem(str(item.text()))  #  다시 왼쪽에 설정을 돌려놓음
        item = listWidgetRuleOk.takeItem(row)
        del item  #  오른쪽 리스트의 설정은 삭제함

        print("해제완료")

    """규칙을 새로 추가하는 함수"""
    def pushButtonAdd_clickedEvent(self):
        row = self.ui.listWidgetRuleNo.currentRow()  #  왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행(currentRow)위치를 row로 받아옴
        text, ok = QInputDialog.getText(self, "규칙 추가", "추가할 규칙을 입력하세요")  #  메세지 입력할 수 있는 다이얼로그 띄움

        listWidgetRuleOk = self.ui.listWidgetRuleOK
        listWidgetRuleNo = self.ui.listWidgetRuleNo
        countListWidgetRuleOk = listWidgetRuleOk.count()
        countListWidgetRuleNo = listWidgetRuleNo.count()

        ruleDuplicateFlag = 0  #  중복 체크 변수 선언
        okListItems = []  #  오른쪽 리스트 아이템 받아올 배열 생성
        noListItems = []  #  왼쪽 리스트 아이템 받아올 배열 생성

        """현재 선택된 규칙 리스트의 아이템에 기능제한 체크박스 체크한 TRUE FALSE값 저장시킴"""
        """변수를 주고 넘겨서 나중에 규칙 리스트 더블클릭하여 수정하고플 시 , 값 읽어오게 해야됨"""

        if countListWidgetRuleNo is None:  #  왼쪽 리스트에 아이템이 하나도 없을 때 -아이템이 오른쪽 리스트로 전부 다 이동했을 때- 이때는 오른쪽 리스트만 배열에 저장한다
            for index in range(countListWidgetRuleOk):  #  오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                okListItems.append(listWidgetRuleOk.item(index).text())  #  오른쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and text != '':

                for i in range(len(okListItems)):
                    if text == okListItems[i]:
                        ruleDuplicateFlag = 1  #  중복체크변수 1로 세팅

                        self.showNoDuplicate()  #  중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        continue

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row, text)  #  왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 text를 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)
                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")

            elif ok and text == '':  # 사용자가 text(규칙)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()

                return

        elif countListWidgetRuleOk is None:  #  오른쪽 리스트에 아이템이 하나도 없을 때 -아이템이 왼쪽 리스트로 전부 다 이동했을 때- 이때는 왼쪽 리스트만 배열에 저장한다
            for index in range(countListWidgetRuleNo):  #  왼쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                noListItems.append(listWidgetRuleNo.item(index).text())  #  왼쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and text != '':

                for i in range(len(noListItems)):
                    if text == noListItems[i]:
                        ruleDuplicateFlag = 1  #  중복체크변수 1로 세팅

                        self.showNoDuplicate()  #  중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        continue

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row, text)  #  왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 text를 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)
                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")

            elif ok and text == '':  # 사용자가 text(규칙)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()

                return

        else:  #  왼쪽, 오른쪽 규칙 리스트에 다 아이템이 있을 때
            for index in range(countListWidgetRuleOk):  #  오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                okListItems.append(listWidgetRuleOk.item(index).text())  #  오른쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장
            for index in range(countListWidgetRuleNo):  #  왼쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                noListItems.append(listWidgetRuleNo.item(index).text())  #  왼쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and text != '':

                for i in range(len(noListItems)):
                    if text == noListItems[i]:
                        ruleDuplicateFlag = 1  #  중복체크변수 1로 세팅

                        self.showNoDuplicate()  #  중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        for j in range(len(okListItems)):
                            if text == okListItems[j]:
                                ruleDuplicateFlag = 1  #  중복체크변수 1로 세팅

                                self.showNoDuplicate()  #  중복 경고메세지박스 출력 함수 호출

                                break
                        continue

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row, text)  #  왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 text를 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)
                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")

            elif ok and text == '':  # 사용자가 text(규칙)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()

                return

    def pushButtonDelete_clickedEvent(self):
        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.takeItem(row)  #  왼쪽 리스트에서 삭제할 현재 클릭된 행의 아이템을 받아옴
        del item

    """규칙을 새로 추가하거나 기존 규칙을 적용시키려 할 때, 규칙 리스트에 해당 규칙이 중복 존재 시, 경고 메시지 박스 출력하는 함수"""
    def showNoDuplicate(self):  #  중복 알림 함수
        msgNo = QtWidgets.QMessageBox()
        msgNo.setIcon(QtWidgets.QMessageBox.Warning)
        msgNo.setWindowTitle("경고")
        msgNo.setText("규칙 리스트에 이미 존재합니다.")
        msgNo.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgNo.exec_()

    def showLimitsetting(self):  #  더블 클릭 시 실행되는 기능 제한 설정 함수
        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.item(row)
        print("현재 선택된 리스트의 키워드는 " + str(item.text()))  #  테스트##################
        print("현재 선택된 리스트의 키워드의 번호는 ", row)   #  테스트#####################
        ######제한설정마친 후 현재 더블클릭돼서 선택된 아이템에 제한설정 체크 정보 변수로 저장해서 인수로 넘겨줘야 함######

        second = secondWindow()
        if second.exec_():  #  두번째 윈도우 창이 정상 종료 되면,

            if second.checkbox1.isChecked() and second.checkbox2.isChecked():
                self.check1selected()
                self.check2selected()
            elif second.checkbox1.isChecked():
                self.check1selected()
            elif second.checkbox2.isChecked():
                self.check2selected()
            else:
                print("nothing")

    def check1selected(self):  #  체크박스 1번 선택됐을 때 실행되는 함수 틀
        print("check1 ok")

    def check2selected(self):  #  체크박스 2번 선택됐을 때 실행되는 함수 틀
        print("check2 ok")

    """패스워드 입력 함수"""
    def pushButtonPasswd_clickedEvent(self):
        text, okPressed = QInputDialog.getText(self, "비밀번호 입력", "Please Input Password ", QLineEdit.Password, "")
        if okPressed and text != '':
            passwd = text
            print("Your password is: " + passwd)

        elif okPressed and text == '':
            plzInputPasswd = QtWidgets.QMessageBox(self)
            plzInputPasswd.setWindowTitle("비밀번호 입력 오류")
            plzInputPasswd.setIcon(QtWidgets.QMessageBox.Warning)
            plzInputPasswd.setText("비밀번호를 제대로 입력하세요.")
            plzInputPasswd.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    mypmpLayout = pmpLayout()
    mypmpLayout.show()
    sys.exit(app.exec_())  # 없으면 창 바로 꺼짐

if __name__ == '__main__':
    main()

