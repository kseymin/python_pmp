import os
import signal
import proc_manager as pm
import format_manager as fm
import lock_manager as lm

#gui testing..
#import gui.passwd as gui_pwd

def reopen_file(path_list):
    if len(path_list) is not 1:
        for i in range(0, len(path_list)):
            path = path_list[i][1]
            print('os.startfile path:', path)
            os.startfile(path)
    else:
        for path in path_list:
            os.startfile(path[1])


def  processing(pname, ignore_list):

    process_name = pname
    is_need_kil = True
    path_list = list()

    ignore_path_list = list()

    ignore_pid_list = list()


    #제외된 프로세스 있는지 확인
    print('this is ignore test is not 0 : ', ignore_list)
    if len(ignore_list) is not 0:
        ignore_flag = True
        ignore = ignore_list
    else:
        ignore_flag = False
        ignore = list()



    if pm.is_running(process_name):
        path_list = pm.get_path(process_name)


        # 여기에  처리 문 , 필터링 처리 문


        #text 변환
        x=fm.get_text_to_process(process_name,path_list)

        print("-----텍스트값----\n",x)

        #필터링
        catch = True

        # 텍스트 내용물이 필터링걸리면
        if catch:
            for pid in pm.get_proc_pid_list(process_name):
                if ignore_flag:  #제외된 프로세스 가있으면
                #os.kill(pid, signal.SIGTERM)
                    ignore_pid_list=pm.path_to_pid(process_name,ignore)
                    print('ignore_pid',ignore_pid_list)
                    for ig_pid in ignore_pid_list:
                        if pid == ig_pid:
                            input_password = input('input your password:')
                            if lm.is_key_right(input_password):
                                ignore.pop()
                                print('password matched')
                            else:
                                print('password not match')
                                ignore.pop()
                                os.kill(pid, signal.SIGTERM)
                        else:
                            print('ignore filtered error')

                # 제외된 프로세스가 아니면 (걸러야할 내용이있지만 프로세스가 제외가안되잇으면 x)
                else:
                    print('걸려야할 내용이있지만 프로세스 제외는 안되있음')
                    os.kill(pid, signal.SIGTERM)

                    input_password = input('input your password:')
                    if lm.is_key_right(input_password):

                        #ignore 추가
                        #ignore.append(pid)
                        for path in path_list:
                            ignore += path

                        print('password matched')
                        reopen_file(path_list)
                    else:
                        os.kill(pid, signal.SIGTERM)
                        print('password not match')

        else:#텍스트내용물이 필터링에 안걸리면
            pass
    else:
        print('filterd process not running')

    return ignore




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
    pname = 'notepad'
    stopbutton_flag= False

    first_routine = True

    ignore_list = list()


    while not stopbutton_flag:
        if first_routine :
            ignore_list += processing(pname,ignore_list)
            print('this is first ignore : ',ignore_list )
            if len(ignore_list) is not 0:
                first_routine = False
        else:
            x= processing(pname,ignore_list)
            ignore_list += x

        # if is_need_kill:
        #     pass
        # else:
        #     reopen_file(path_list)
        #     # for ignore in ignore_list:
        #     #     ignore_list.append(ignore)

