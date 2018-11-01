'''
input
필터링할 프로세스 이름

return
원하는 프로세스 의 path값 return
'''
import re


'''
CommandLine으로 나오는 값이
'"C:\\Windows\\system32\\NOTEPAD.EXE" C:\\Users\\kitri\\Desktop\\설치목록.txt'
형식이라서

해당 형식을 나누기위한 함수
'''
def set_filter(split_string):
    f = re.compile('[A-Z]:')
    s= split_string
    s = re.sub('[", ' ']', '', s)

    output_list= list()

    indexList = []
    for i in f.finditer(s):
        indexList.append(i.span()[0])
    indexList.append(len(s))

    for i in range(0, len(indexList)-1):
        output_list.append(s[indexList[i]:indexList[i+1]])

    return output_list




def is_running(process_name,wmip):
    p = wmip
    process_name += '.exe'
    process_name.lower()

    flag = False

    if  p.Win32_Process(name=process_name):
        flag = True

    return flag

#
def pid_to_path(pname, pid,wmip):
    p = wmip
    pname += '.exe'
    pname.lower()

    result_pid= str()

    win32pid_list = [pid for pid in p.Win32_Process(name = pname)]

    for process in win32pid_list:
        if process == pid:
            result_pid = process.CommandLine

    return result_pid


def path_to_pid_input_string(pname,input_string,wmip):

    #tmp_str = str()
    output_pid = str()
    filter = pname + '.exe'

    p = wmip

    win32pid_list = [pid for pid in p.Win32_Process(name=filter)]

    for process in  win32pid_list:
        if process.CommandLine is not None:
            tmp_list = set_filter(process.CommandLine)
            if tmp_list[1] == input_string:
                output_pid =process.ProcessId

    return output_pid




def path_print(path_list):
    outlist = list()
    # 해당되는 프로세스 여러개일때
    if len(path_list) is not 1:
        for inum in range(0,len(path_list)):
            outlist += inum,path_list[inum][1]
        return outlist
    #outlist 첫번째 인자는 번호 , 두번째인자는 path
    else:
        # 프로세스 하나일때 아웃풋
        return path_list[0][1]



#  실제 연 파일 path 한번에 리턴
def get_path(filter,wmip):
    p = wmip
    filter = filter + '.exe'

    output_tmp = str()
    filtered_output = list()

    win32pid_list = [pid for pid in p.Win32_Process()]

    for process in win32pid_list :
      if process.CommandLine is not None:
          output_tmp += '\n'+process.CommandLine

    need_filter_list = output_tmp.splitlines()
    matching = [s for s in need_filter_list if filter.lower() in s.lower()]

    for lines in matching:
        filtered_output.append(set_filter(lines))

    return filtered_output




#  실제 연 특정 파일 path 한번에 리턴
def get_specific_path(pname,pid,wmip):
    p = wmip
    filter =pname + '.exe'

    #output_tmp = str()
    need_filter_list = list()

    filtered_output = list()

    win32pid_list = [pid for pid in p.Win32_Process()]

    for process in win32pid_list:
        pc = process.CommandLine
        proc_id = process.ProcessId
        if pc is not None:
            if proc_id == pid:
                #output_tmp += '\n' + pc
                need_filter_list.append(pc)

    #need_filter_list = output_tmp.splitlines()
    matching = [s for s in need_filter_list if filter.lower() in s.lower()]

    for lines in matching:
        filtered_output.append(set_filter(lines))
        #filtered_output.append(set_filter(lines))

    return filtered_output


def get_proc_pid_list(process_name,wmip):

    output_pid = list()
    p = wmip

    if process_name is 'AcroRd32':
        #find_string = 'AcroRd32.exe" --type=renderer  /n'
        find_string = '--type=renderer'


        win32pid_list = [pid for pid in p.Win32_Process(name = 'AcroRd32.exe')]

        for process in win32pid_list:
            pc = process.CommandLine
            proc_id = process.ProcessId
            if pc is not None:
                if find_string not in pc:
                    output_pid.append(proc_id)
    else:

        process_name += '.exe'
        #process_name.lower()
        win32pid_list = [pid for pid in p.Win32_Process(name = process_name)]

        for process in win32pid_list:
            output_pid.append(process.ProcessId)


    return  output_pid


#if __name__ == '__main__':
    #test code
    #get_path('AcroRd32')