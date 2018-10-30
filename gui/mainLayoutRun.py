import sys
#from mainLayout6 import *
#from firstSettingRun import *

import gui.mainLayout as guiMain
import gui.firstSettingRun as firstSetting


from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5 import QtTest
import config_make.config_manager as cm

import config_make.config_manager_test as cmt
import lock_manager as lm

# Real Time Search import
import main_operator as mo
import copy_defender as cd
from multiprocessing import Process

# Whole System Search
import file_scan

# Registry Reset
import reg_manager


process_list = []


class secondWindow(QtWidgets.QDialog):  # 두번째 윈도우 창 (기능 제한 설정 창)

    def __init__(self, parent=None):
        super(secondWindow, self).__init__(parent)

        self.label = QtWidgets.QLabel()  #  라벨
        self.lineEditKeyword = QtWidgets.QLineEdit()  #  검색할 키워드 입력 창
        self.pushButtonKeyword = QtWidgets.QPushButton()  #  ok버튼

        layout = QtWidgets.QFormLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.lineEditKeyword)
        layout.addWidget(self.pushButtonKeyword)

        self.setLayout(layout)
        self.setWindowTitle("Keyword")
        self.setMinimumWidth(50)

        self.label.setText("규칙을 입력하세요.")

        self.pushButtonKeyword.clicked.connect(self.pushButtonKeyword_clcikedEvent)
        self.pushButtonKeyword.setText("확인")



    def pushButtonKeyword_clcikedEvent(self):

        text = self.lineEditKeyword.text()
        text = text.strip(' ')

        if text != '' and text != ' ':  #  텍스트에 넣은것이 공백이 아니면
            """
            키워드 저장
            """
            title =cmt.get_tmp()
            cmt.add_left(title, content=text)
            print("키워드 저장됨")
            self.close()

        elif text == '' and text == ' ':
            inputError = QtWidgets.QMessageBox(self)
            inputError.setWindowTitle("키워드 입력 오류")
            inputError.setIcon(QtWidgets.QMessageBox.Warning)
            inputError.setText("키워드를 다시 입력하세요")
            inputError.exec_()
            pass


class pmpLayout(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = guiMain.Ui_PMP()
        self.ui.setupUi(self)

        """UI 각종 이벤트(버튼클릭 등)와 함수를 연결"""
        self.ui.pushButtonRuleApplyOk.clicked.connect(self.pushButtonApplyOk_clickedEvent)  # 규칙적용버튼
        self.ui.pushButtonRuleApplyNo.clicked.connect(self.pushButtonApplyNo_clickedEvent)  # 규칙해제버튼
        self.ui.pushButtonRuleAdd.clicked.connect(self.pushButtonAdd_clickedEvent)  # 규칙추가버튼
        self.ui.pushButtonRuleDelete.clicked.connect(self.pushButtonDelete_clickedEvent)  # 규칙제거버튼
        self.ui.pushButtonChangePassword.clicked.connect(self.pushButtonChangePassword_clickedEvent)  # 패스워드변경버튼
        self.ui.listWidgetRuleNo.itemDoubleClicked.connect(self.showKeyword)  # 리스트위젯 아이템 더블클릭 버튼
        self.ui.pushButtonSearchWhole.clicked.connect(self.pushButtonSearchWhole_clickedEvent)  # 전체검색버튼
        self.ui.pushButtonSearchRT.clicked.connect(self.pushButtonSearchRT_clickedEvent)  # 리얼타임검색버튼
        self.ui.pushButtonStop.clicked.connect(self.pushButtonStop_clickedEvent)  # 검색 STOP버튼
        self.ui.pushButtonResetReg.clicked.connect(self.pushButtonResetReg_clickedEvent)  # 레지스트리 초기화 버튼
        self.ui.textBrowserSearch.setStyleSheet("background-image: url(backgroundImg.png);")  # 백그라운드 이미지 삽입
        self.setFixedSize(self.size())

        self.stop = False  # Search 반복 탈출을 위한 플래그 변수 선언

    def showKeyword(self):   #  아이템 더블클릭 시 키워드 보여줌
        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.item(row)
        print("현재 선택된 리스트의 키워드는 " + str(item.text()))  # 테스트##################
        print("현재 선택된 리스트의 키워드의 번호는 ", row)  # 테스트#####################

        output_text = cmt.get_specific_item( str(item.text()))



        showKeyword = QtWidgets.QMessageBox(self)
        showKeyword.setWindowTitle("Keyword")
        showKeyword.setIcon(QtWidgets.QMessageBox.Information)
        showKeyword.setText("해당 키워드는 " + output_text + " 입니다.")
        showKeyword.exec_()

    def pushButtonSearchWhole_clickedEvent(self):  # 전체검색클릭시 실행 함수

        path, okPressed = QInputDialog.getText(self, "경로 입력", "Please Input Path ")
        # C:/Users/baron/Desktop/TestDir

        if okPressed is not None and path != '':
            """폰트설정"""
            myFont = self.ui.textBrowserSearch.font()
            f = QtGui.QFont(myFont)
            f.setPointSize(10)
            f.setFamily("Utsaah")
            f.setItalic(False)
            self.ui.textBrowserSearch.setFont(f)
            self.stop = False  # 반복시작을 위해 다시 반복탈출 플래그를 False로 세팅

            self.ui.textBrowserSearch.setStyleSheet("")  # 백그라운드 이미지 지우기
            self.ui.textBrowserSearch.setText("")  # 백그라운드 텍스트 초기화

            self.ui.pushButtonSearchWhole.setEnabled(False)  # 검색버튼 비활성화
            self.ui.pushButtonSearchRT.setEnabled(False)

            detected_list = file_scan.file_scanning(path)
            for i in detected_list:
                self.ui.textBrowserSearch.append("[Detected Files]")
                self.ui.textBrowserSearch.append(i)

            # if self.stop is True:
            #     break

        elif okPressed and path == '':

            plzInputPasswd = QtWidgets.QMessageBox(self)
            plzInputPasswd.setWindowTitle("경로 입력 오류")
            plzInputPasswd.setIcon(QtWidgets.QMessageBox.Warning)
            plzInputPasswd.setText("경로를 제대로 입력하세요.")
            plzInputPasswd.exec_()

        else:
            return

    def pushButtonSearchRT_clickedEvent(self):  # 리얼타임검색시 실행 함수

        """폰트설정"""
        myFont = self.ui.textBrowserSearch.font()
        f = QtGui.QFont(myFont)
        f.setPointSize(10)
        f.setFamily("Utsaah")
        f.setItalic(False)
        self.ui.textBrowserSearch.setFont(f)
        self.stop = False  # 반복시작을 위해 다시 반복탈출 플래그를 False로 세팅

        self.ui.textBrowserSearch.setStyleSheet("")  # 백그라운드 이미지 지우기
        self.ui.textBrowserSearch.setText("")  # 백그라운드 텍스트 초기화

        self.ui.pushButtonSearchWhole.setEnabled(False)  # 검색버튼 비활성화
        self.ui.pushButtonSearchRT.setEnabled(False)

        #
        # i = 0
        # while i < 100:
        #     self.ui.textBrowserSearch.append('리얼타임검색합니다. %d' % i)
        #     i = i + 1
        #     QtTest.QTest.qWait(100)  # 딜레이 속도 설정
        #
        #     if self.stop is True:
        #         break

        pname_list = ['notepad', 'winword', 'POWERPNT', 'excel', 'AcroRd32']

        #process_list = []

        filter_list = ['test']

        for pname in pname_list:
            process = Process(target=mo.run,args=(pname,), name=pname)
            process_list.append(process)

        process = Process(target=cd.clipboard_copy_monitor, args=(filter_list,), name='copyDefender')
        process_list.append(process)

        print(process_list)

        for p in process_list:
            output_tmp = 'Real Time process :'+p.name +' is Running..'
            self.ui.textBrowserSearch.append(output_tmp)
            p.start()

    def pushButtonStop_clickedEvent(self):


        self.stop = True

        self.ui.labelReport.setText('Search Stop')  ####################################################################
        #QtTest.QTest.qWait(100)                     ###################   변경사항1 글 띄웠다가 없앰   ####################
                  ####################################################################

        self.ui.pushButtonSearchWhole.setEnabled(True)  # 검색버튼 재활성화
        self.ui.pushButtonSearchRT.setEnabled(True)

        self.ui.textBrowserSearch.setText('')
        for p in process_list:
            output_tmp = 'Real Time process :'+p.name+' is Terminated.'
            self.ui.textBrowserSearch.append(output_tmp)
            p.terminate()

        QtTest.QTest.qWait(1000)
        self.ui.labelReport.setText('')

        self.ui.textBrowserSearch.setStyleSheet(
            "background-image: url(backgroundImg.png); background-attachment: scroll;")  # 백그라운드 이미지 삽입
        self.ui.textBrowserSearch.setText('')

    """왼쪽 리스트에서 규칙 클릭하고 적용시, 규칙을 오른쪽으로 추가하는 부분"""

    def pushButtonApplyOk_clickedEvent(self):
        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.item(row)  # 현재 클릭된 행(row)의 값(item)을 받아옴

        listWidgetRuleOk = self.ui.listWidgetRuleOK
        listWidgetRuleNo = self.ui.listWidgetRuleNo
        countListWidgetRuleOk = listWidgetRuleOk.count()
        countListWidgetRuleNo = listWidgetRuleNo.count()

        if item is None:  # 왼쪽 규칙 리스트에서 마우스 클릭을 안 해서 어떤 item도 선택되지 않았을 시-
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
                # config2.configright(item.text())
                cmt.input_right_table(item.text())
                item = listWidgetRuleNo.takeItem(row)
                del item

                """self.ui.listWidgetRuleOk.addItem(str(item.text()))  #  왼쪽 규칙 리스트에서 선택된 아이템의 텍스트를 str형으로 받아서 오른쪽 규칙 리스트에 추가함
                item = self.ui.listWidgetRuleNo.takeItem(row)  #  왼쪽 리스트의 규칙은 삭제함
                del item"""

                print("설정완료")

            else:
                """오른쪽 리스트에 아이템이 하나라도 있을 때- 중복 비교 구문 시작"""
                listItems = []  # 리스트 아이템 받아올 배열 생성
                for index in range(countListWidgetRuleOk):  # 오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                    listItems.append(listWidgetRuleOk.item(index).text())  # 오른쪽 리스트의 아이템을 텍스트형태로 받아와서 listItems배열에 저장

                ruleDuplicateFlag = 0  # 아이템 동일한거 있는지 검사하는 플래그 변수 선언

                """추가할 왼쪽리스트 item의 text문과 listItems에 있는 아이템과 하나라도 동일한게 있는지 반복검사"""
                for i in range(len(listItems)):
                    if item.text() == listItems[i]:  # 동일한 규칙 추가 하려고 할 시,

                        ruleDuplicateFlag = 1  # 중복체크변수 1로 세팅

                        self.showNoDuplicate()  # 중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        continue

                if ruleDuplicateFlag == 0:
                    listWidgetRuleOk.addItem(
                        str(item.text()))  # 반복검사 마치고 난 뒤 왼쪽 규칙 리스트에서 선택된 아이템의 텍스트를 str형으로 받아서 오른쪽 규칙 리스트에 추가함
                    # config2.configright(item.text())
                    # cmt.configright(item.text())
                    cmt.input_right_table(item.text())
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

        else:
            listWidgetRuleNo.addItem(str(item.text()))  # 다시 왼쪽에 설정을 돌려놓음
            # cm.configleft(item.text())
            cmt.input_left_table(str(item.text()))
            item = listWidgetRuleOk.takeItem(row)
            del item  # 오른쪽 리스트의 설정은 삭제함

            print("해제완료")


    def pushButtonAdd_clickedEvent(
            self):  ########################변경내용: text -> title로 인자이름 변경 밑 추가##############################################################

        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행(currentRow)위치를 row로 받아옴
        title, ok = QInputDialog.getText(self, "규칙 이름 추가", "추가할 규칙의 이름을 입력하세요.")  # 메세지 입력할 수 있는 다이얼로그 띄움

        tmp = title.strip(' ')

        title = tmp

        ##############################타이틀에 해당하는 검색 키워드 저장하는 구문 추가해야됨 ##############################################################

        listWidgetRuleOk = self.ui.listWidgetRuleOK
        listWidgetRuleNo = self.ui.listWidgetRuleNo
        countListWidgetRuleOk = listWidgetRuleOk.count()
        countListWidgetRuleNo = listWidgetRuleNo.count()

        ruleDuplicateFlag = 0  # 중복 체크 변수 선언
        okListItems = []  # 오른쪽 리스트 아이템 받아올 배열 생성
        noListItems = []  # 왼쪽 리스트 아이템 받아올 배열 생성

        """현재 선택된 규칙 리스트의 아이템에 기능제한 체크박스 체크한 TRUE FALSE값 저장시킴"""
        """변수를 주고 넘겨서 나중에 규칙 리스트 더블클릭하여 수정하고플 시 , 값 읽어오게 해야됨"""

        if countListWidgetRuleNo is None:  # 왼쪽 리스트에 아이템이 하나도 없을 때 -아이템이 오른쪽 리스트로 전부 다 이동했을 때- 이때는 오른쪽 리스트만 배열에 저장한다
            for index in range(countListWidgetRuleOk):  # 오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                okListItems.append(listWidgetRuleOk.item(index).text())  # 오른쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and title != '':

                for i in range(len(okListItems)):
                    if title == okListItems[i]:
                        ruleDuplicateFlag = 1  # 중복체크변수 1로 세팅

                        self.showNoDuplicate()  # 중복 경고메세지박스 출력 함수 호출

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row,
                                                title)  # 왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 title을 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)

                    # cm.configset2(title)  #############################변경사항 text -> title 로 인자이름 변경 ########################################################

                    cmt.add_tmp(title)

                    # print("되냐")
                    self.second = secondWindow()
                    self.second.show()
                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")

            elif ok:  # 사용자가 text(규칙)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()




        elif countListWidgetRuleOk is None:  # 오른쪽 리스트에 아이템이 하나도 없을 때 -아이템이 왼쪽 리스트로 전부 다 이동했을 때- 이때는 왼쪽 리스트만 배열에 저장한다
            for index in range(countListWidgetRuleNo):  # 왼쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                noListItems.append(listWidgetRuleNo.item(index).text())  # 왼쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and title != '':

                for i in range(len(noListItems)):
                    if title == noListItems[i]:
                        ruleDuplicateFlag = 1  # 중복체크변수 1로 세팅

                        self.showNoDuplicate()  # 중복 경고메세지박스 출력 함수 호출

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row,
                                                title)  # 왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 title을 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)

                    # cm.configset2(title)  #############################변경사항 text -> title 로 인자이름 변경 ########################################################
                    cmt.add_tmp(title)
                    print("되냐")
                    self.second = secondWindow()
                    self.second.show()

                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")

            elif ok:  # 사용자가 title(규칙제목)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()



        else:  # 왼쪽, 오른쪽 규칙 리스트에 다 아이템이 있을 때
            for index in range(countListWidgetRuleOk):  # 오른쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                okListItems.append(listWidgetRuleOk.item(index).text())  # 오른쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장
            for index in range(countListWidgetRuleNo):  # 왼쪽 리스트를 count()하여 item의 갯수를 알아내어 반복
                noListItems.append(listWidgetRuleNo.item(index).text())  # 왼쪽 리스트의 아이템을 텍스트형태로 받아와서 noListItems배열에 저장

            if ok and title != '':

                for i in range(len(noListItems)):
                    if title == noListItems[i]:
                        ruleDuplicateFlag = 1  # 중복체크변수 1로 세팅

                        self.showNoDuplicate()  # 중복 경고메세지박스 출력 함수 호출

                        break
                    else:
                        for j in range(len(okListItems)):
                            if title == okListItems[j]:
                                ruleDuplicateFlag = 1  # 중복체크변수 1로 세팅

                                self.showNoDuplicate()  # 중복 경고메세지박스 출력 함수 호출

                if ruleDuplicateFlag == 0:
                    listWidgetRuleNo.insertItem(row,
                                                title)  # 왼쪽 규칙 리스트에서 현재 클릭된 아이템의 행 바로 위에 입력한 text를 추가함 (아이템을 클릭하지 않았다면 기본 값은 맨 위)

                    # cm.configset2(title)  #############################변경사항 text -> title 로 인자이름 변경 ########################################################
                    cmt.add_tmp(title)
                    print("되냐")
                    self.second = secondWindow()
                    self.second.show()

                    print("해당 규칙은 중복되지 않습니다.")
                    print("추가완료")



            elif ok:  # 사용자가 text(규칙)에 값을 안 넣었을 때 오류 메세지박스 띄움
                plzInputRule = QtWidgets.QMessageBox(self)
                plzInputRule.setWindowTitle("규칙 입력 오류")
                plzInputRule.setIcon(QtWidgets.QMessageBox.Warning)
                plzInputRule.setText("규칙을 제대로 입력하세요.")
                plzInputRule.exec_()






    def pushButtonDelete_clickedEvent(self):
        row = self.ui.listWidgetRuleNo.currentRow()  # 왼쪽 리스트에서 현재 클릭된 행(currentRow)을 row로 받아옴
        item = self.ui.listWidgetRuleNo.takeItem(row)  # 왼쪽 리스트에서 삭제할 현재 클릭된 행의 아이템을 받아옴

        ###########################################해당 타이틀의 키워드 지우는 구문 추가해야됨#########################################
        print(type(item))
        print(item)
        print(row)
        if item is None:
            pass
        else:
            #cm.configdel3(item.text())
            cmt.delete_item(item.text())
            del item


    """규칙을 새로 추가하거나 기존 규칙을 적용시키려 할 때, 규칙 리스트에 해당 규칙이 중복 존재 시, 경고 메시지 박스 출력하는 함수"""

    def showNoDuplicate(self):  # 중복 알림 함수
        msgNo = QtWidgets.QMessageBox()
        msgNo.setIcon(QtWidgets.QMessageBox.Warning)
        msgNo.setWindowTitle("경고")
        msgNo.setText("규칙 리스트에 이미 존재합니다.")
        msgNo.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgNo.exec_()

    def pushButtonChangePassword_clickedEvent(
            self):  # 비번 변경             #######################변수명 변경#########################
        text, okPressed = QInputDialog.getText(self, "기존 비밀번호 입력", "Please Input Password ", QLineEdit.Password, "")

        if okPressed and text != '':
            input_password = text

            print('input_password:', type(input_password), '  ', input_password)
            if lm.is_key_right(input_password):  # 비번 맞는지 비교
                print("비번 인증 성공")
                new_pwd, okclicked = QInputDialog.getText(self, "새 비밀번호 입력", "Please Input New Password",
                                                          QLineEdit.Password, "")

                if okclicked and new_pwd != '':
                    # oldPassword = newPassword  # 변경한 새 비밀번호를 예전 비밀번호 변수에 대입
                    # print('new pwd:',new_pwd)  # 변경된 새 비밀번호 확인 테스트
                    print("인증 완료")
                    # cm.configpasswd2(newtext)
                    # cmt.password_change(newtext)
                    lm.make_key(new_pwd)
                    print("변경 완료")

                elif okclicked and new_pwd == '':
                    plzInputPasswd = QtWidgets.QMessageBox(self)
                    plzInputPasswd.setWindowTitle("비밀번호 입력 오류")
                    plzInputPasswd.setIcon(QtWidgets.QMessageBox.Warning)
                    plzInputPasswd.setText("비밀번호를 제대로 입력하세요.")
                    plzInputPasswd.exec_()

            else:
                print("비밀번호가 틀렸습니다.")
                wrongPasswd = QtWidgets.QMessageBox(self)
                wrongPasswd.setWindowTitle("비밀번호가 틀렸습니다.")
                wrongPasswd.setIcon(QtWidgets.QMessageBox.Warning)
                wrongPasswd.setText("비밀번호를 확인하세요.")
                wrongPasswd.exec_()

        elif okPressed and text == '':

            plzInputPasswd = QtWidgets.QMessageBox(self)
            plzInputPasswd.setWindowTitle("비밀번호 입력 오류")
            plzInputPasswd.setIcon(QtWidgets.QMessageBox.Warning)
            plzInputPasswd.setText("비밀번호를 제대로 입력하세요.")
            plzInputPasswd.exec_()


    def pushButtonResetReg_clickedEvent(self):  ###############변수명 변경 ################
        """
        레지스트리 초기화 함수
        """
        reg_manager.reg_restore()

        """모든 버튼 비활성화"""
        # self.ui.pushButtonSearchWhole.setEnabled(False)
        # self.ui.pushButtonSearchRT.setEnabled(False)
        # self.ui.pushButtonStop.setEnabled(False)
        # self.ui.pushButtonChangePassword.setEnabled(False)
        # self.ui.pushButtonRuleAdd.setEnabled(False)
        # self.ui.pushButtonRuleApplyNo.setEnabled(False)
        # self.ui.pushButtonRuleApplyOk.setEnabled(False)
        # self.ui.pushButtonRuleDelete.setEnabled(False)
        #
        # self.ui.listWidgetRuleNo.setEnabled(False)
        # self.ui.listWidgetRuleOK.setEnabled(False)
        #
        # self.ui.pushButtonResetReg.setEnabled(False)
        """
        패스워드 설정한 것 삭제 -> 추후 프로그램 실행 시 처음 시작한것과 동일하게 판단
        """

def main():
    app = QtWidgets.QApplication(sys.argv)
    mypmpLayout = pmpLayout()

    mypmpLayout.show()
    sys.exit(app.exec_())  # 없으면 창 바로 꺼짐

if __name__ == '__main__':
    main()