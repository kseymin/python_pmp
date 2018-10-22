'''
input
필터링할 프로세스 이름

return
원하는 프로세스 의 path값 return
'''
import re
import wmi

'''
CommandLine으로 나오는 값이
'"C:\\Windows\\system32\\NOTEPAD.EXE" C:\\Users\\kitri\\Desktop\\설치목록.txt'
형식이라서

해당 형식을 나누기위한 함수
'''
def set_filter(split_string ):
    f = re.compile('[A-Z]:')
    #s = '"C:\\Windows\\system32\\NOTEPAD.EXE" C:\\Users\\kitri\\Desktop\\설치목록.txt'
    s= split_string
    s = re.sub('[", ' ']', '', s)

    output_list= list()
    # print (s)
    indexList = []
    for i in f.finditer(s):
        indexList.append(i.span()[0])
    indexList.append(len(s))
    #print (indexList)

    for i in range(0, len(indexList)-1):
        #s[indexList[i]:indexList[i+1]]
        output_list.append(s[indexList[i]:indexList[i+1]])
    #print('test filter index:',output_list)
    return output_list
'''
get_proc_pid
프로세스 리스트화 함수

리스트 로 결과 리턴
'''
def  get_proc_pid_list(process_name):
    p = wmi.WMI()
    process_name += '.exe'
    process_name.lower()

    pid_list = list()
    for process in p.Win32_Process(name = process_name):
        pid_list.append(process.ProcessId)

    return pid_list

def is_running(process_name):
    p = wmi.WMI()
    process_name += '.exe'
    process_name.lower()

    flag = False

    if  p.Win32_Process(name=process_name):
        flag = True

    return flag

#


# 제외할 파일 패스 를 주면 현재 돌아가는것중에 제외할 파일패스로 킨 pid를 줘야함
def path_to_pid(pname,ignore_path_list):

    tmp_str = str()
    output_process_list = list()
    filter = pname + '.exe'
    current_process_path_list = list()


    p = wmi.WMI()

    for process in p.Win32_Process():
        if process.CommandLine is not None:
            tmp_str += '\n' + process.CommandLine

        ##
        need_filter_list = tmp_str.splitlines()

        matching = [s for s in need_filter_list if filter.lower() in s.lower()]

        for lines in matching:
            current_process_path_list.append(set_filter(lines))

        ###
        for cp_path in current_process_path_list:
            for ig_path in ignore_path_list:
                if cp_path[1] == ig_path:
                    output_process_list.append(process.ProcessId)

    return output_process_list



##


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
def get_path(filter):
    p = wmi.WMI ()
    filter =filter + '.exe'

    output_tmp = str()
    filtered_output = list()

    for process in p.Win32_Process ():
      if process.CommandLine is not None:
          output_tmp += '\n'+process.CommandLine

    need_filter_list = output_tmp.splitlines()


    matching = [s for s in need_filter_list if filter.lower() in s.lower()]
    #print('matching :',matching)
    for lines in matching:
        #print('lines:',lines)
        filtered_output.append(set_filter(lines))

    return filtered_output


if __name__ == '__main__':
    #test code

    filtering_process = 'notepad'
    path_list = get_path(filtering_process)

    if len(path_list) is not 1:

        print('this is path_list :   ',path_list)

        for inum in range(0,len(path_list)):
            print(filtering_process+' :{}  path:  {}'.format(inum,path_list[inum][1]))

    else:
        print(filtering_process+' 실제 파일 경로 {}'.format(path_list[0][1]))
