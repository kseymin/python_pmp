import os
import signal
import proc_manager as pm
import format_manager as fm
import lock_manager as lm

#import gui.passwdLayoutRun as pwd_gui
#import config_make.config_manager_test as cmt
import configparser




# gui testing..
import gui_password_dialog as gui_pwd

ignore_list = list()


abspath = os.path.abspath('../config_make/config.cfg')
#이 코드를 메인으로 쓰려면 아래 경로로(테스트용)
#abspath = os.path.abspath('./config_make/config.cfg')
isabspath = abspath






def reopen_file(path_list):
    if len(path_list) is not 1:
        for i in range(0, len(path_list)):
            path = path_list[i][1]
            print('os.startfile path:', path)
            os.startfile(path)
    else:
        for path in path_list:
            os.startfile(path[1])


def realtime_processing(pname):
    process_name = pname
    filter_flag = False

    current_path_list = pm.get_path(process_name)
    print("current_path  : ", current_path_list)
    print("proc_name : ", process_name)

    file_text = fm.get_text_to_process(process_name, current_path_list)

    print("file_text : ", file_text)

    if file_text is not None:

        # filtering 문제가있음
        need_filter_list = list()
        config = configparser.RawConfigParser()
        config.read(isabspath)

        config_len = len(config.options("RKEYWORD"))
        data_list = config.options('RKEYWORD')

        if config_len is 0:
            print('먼저 필터링할 키워드를 넣어주세요')
            return print('ERROR: no keyword filtering')

        else:
            for i in data_list:
                need_filter_list.append(config.get('RKEYWORD', i))

            for filter in need_filter_list:
                if filter in file_text:
                    filter_flag = True
                    break


    # if filter catch
    # filter_flag = True

    if filter_flag:
        for pid in pm.get_proc_pid_list(process_name):
            if ignore_list:
                print("====123====")
                if pid in ignore_list:
                    pass
                else:
                    open_need_path = pm.get_specific_path(process_name, pid)
                    print(open_need_path)

                    os.kill(pid, signal.SIGTERM)

                    #input_password = input('input your password:')
                    input_password= gui_pwd.run()

                    if lm.is_key_right(input_password):
                        print('Correct Password')
                        reopen_file(open_need_path)
                        reopen_pid = pm.path_to_pid_input_string(process_name, open_need_path[0][1])
                        print('reopen pid : ', reopen_pid)
                        ignore_list.append(reopen_pid)
                        break
                    else:
                        print('not matched password')

            else:
                print("====456====")
                open_need_path = pm.get_specific_path(process_name, pid)
                # open_need_path = open_need_path[0][1]
                print(open_need_path)
                os.kill(pid, signal.SIGTERM)

                #input_password = input('input your password:')
                input_password = gui_pwd.run()
                if lm.is_key_right(input_password):
                    print('Correct Password')
                    reopen_file(open_need_path)

                    reopen_pid = pm.path_to_pid_input_string(process_name, open_need_path[0][1])

                    print('reopen pid : ', reopen_pid)

                    ignore_list.append(reopen_pid)

                else:
                    print('not matched password')


    # 필터에 안걸림
    else:
        print('no filterd')



def run(pname):
    pname = pname  # pname = [notepad, winword, POWERPNT, excel, AcroRd32]

    ignore_list = list()

    while True:

        realtime_processing(pname)

        for ignore in ignore_list:
            if ignore not in pm.get_proc_pid_list(pname):
                ignore_list.remove(ignore)
        print(ignore_list)






if __name__ == '__main__':
    pname = 'winword'  # pname = [notepad, winword, POWERPNT, excel, AcroRd32]
    run(pname)

    stopbutton_flag = False

    first_routine = True

    ignore_list = list()

    while True:

        realtime_processing(pname)


        for ignore in ignore_list:
            if ignore not in pm.get_proc_pid_list(pname):
                ignore_list.remove(ignore)
        print(ignore_list)


