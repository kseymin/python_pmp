# import tkinter as tk
#
#
# def center_window(width=300, height=200):
#     # get screen width and height
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#
#     # calculate position x and y coordinates
#     x = (screen_width/2) - (width/2)
#     y = (screen_height/2) - (height/2)
#     root.geometry('%dx%d+%d+%d' % (width, height, x, y))
#
#
# root = tk.Tk()
# center_window(500, 400)
# root.mainloop()
# import cofig_make.config_manager_test as cmt
# import os
# print(os.path.abspath('./'))
# # x=cmt.get_left_keyword_len()
# # print(x)
# print(os.path.abspath('./config_make/config.cfg'))


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

                    cm.configset2(
                        title)  #############################변경사항 text -> title 로 인자이름 변경 ########################################################
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

                    cm.configset2(
                        title)  #############################변경사항 text -> title 로 인자이름 변경 ########################################################
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

##################################