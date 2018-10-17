import os
import signal
import proc_manager as pm

import format_manager as fm

#gui testing..
#import gui.passwd as gui_pwd


def  processing(pname):

    process_name = pname

    if pm.is_running(process_name):
        path_list = pm.get_path(process_name)


        # 여기에  처리 문 , 필터링 처리 문


        #text 변환
        x=fm.get_text_to_process(process_name,path_list)

        print("-----텍스트값----\n",x)

        #pid process Exit 앞으로 빼도될듯?
        for pid in pm.get_proc_pid_list(process_name):
            os.kill(pid, signal.SIGTERM)

        #gui
        #gui_pwd.make_pwd_qt()

    # return print('-------------------processing done-----------------')

'''
cc
메모장 notepad  


w 두개 동시에 열어두고 돌리면 하나만 읽음
파워포인트 POWERPNT

w 탭 하나만 읽는 문제있음
PDF뷰어 AcroRd32

ww 돌리기전에 두개 이상켜놓으면 하나만읽음
word  winword


ww 돌리기전에 두개이상켜놓으면 하나만 읽음
엑셀 excel


준비중
한글  hwp

'''


if __name__ == '__main__':
    processing('notepad')




    # falg = True:
    #
    #
    # while :
    #     processing('excel')

