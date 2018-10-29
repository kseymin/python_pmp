import configparser
import os



abspath = os.path.abspath('../cofig_make/config.cfg')
path = abspath






def add_tmp(title):
    config = configparser.ConfigParser()
    config.read(path)

    config.set("TMP", 'value', title)

    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def get_tmp():
    config = configparser.ConfigParser()
    config.read(path)
    tmp = config.get("TMP", "value")

    return tmp


def add_left(title,content):#필터링 할검색어 추가하는 함수

    config = configparser.ConfigParser()
    config.read(path)

    config.set("LKEYWORD",title,content)

    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def get_keyword_len_all():#전체 키워드 갯수 얻어오기
    config = configparser.ConfigParser()
    config.read(path)
    left_len = len(config.options("LKEYWORD"))
    rigth_len = len(config.options("RKEYWORD"))
    return left_len + rigth_len




def get_left_keyword_len():#왼쪽 키워드 갯수 얻어오기
    config = configparser.ConfigParser()
    config.read(path)
    left_len = len(config.options("LKEYWORD"))
    return left_len

def get_rigth_keyword_len():#오른쪽 키워드 갯수 얻어오기
    config = configparser.ConfigParser()
    config.read(path)
    rigth_len = len(config.options("RKEYWORD"))
    return rigth_len

def delete_item(del_item):  # 왼쪽오른쪽 상관없이 삭제 키워드에 옵션값으로 검색
    config = configparser.ConfigParser()
    config.read(path)
    # row = 2  # gui와 연동되기전 임시값 ,keyword..
    # a = row  # gui와 연동 keyword버튼의 row값으로 비교

    left_len = get_left_keyword_len()
    right_len = get_rigth_keyword_len()

    for i in range(0,left_len-1):
        if config.options("LKEYWORD")[i] == del_item:
            config.remove_option("LKEYWORD", "%s" % del_item)
            configFile = open(path, "w+")
            config.write(configFile)
            configFile.close()
    for i in range(0,right_len-1):
        if config.options("RKEYWORD")[i] == del_item:
            config.remove_option("RKEYWORD", del_item)
            configFile = open(path, "w+")
            config.write(configFile)
            configFile.close()



def get_specific_item(keyword):
    config = configparser.ConfigParser()
    config.read(path)


    left_len = get_left_keyword_len()
    right_len = get_rigth_keyword_len()

    for i in range(left_len):
        if config.options("LKEYWORD")[i] == keyword:
            return config.items("LKEYWORD")[i][1]

    for i in range(right_len):
        if config.options("RKEYWORD")[i] == keyword:
            return config.items("RKEYWORD")[i][1]



def get_all_items():  # 실제 필터링할 검색어 뽑아내는 함수(왼쪽 오른쪽 싹다)
    config = configparser.ConfigParser()
    config.read(path)

    ltmp_list = list()
    rtmp_list = list()
    #output_list = list()

    left_len = get_left_keyword_len()
    right_len = get_rigth_keyword_len()

    for i in range(left_len):
        ltmp_list.append(config.items("LKEYWORD")[i][1])

    for i in range(right_len):
        rtmp_list.append(config.items("RKEYWORD")[i][1])

    output_list = ltmp_list + rtmp_list
    #test code
    print('test ouput:',output_list)
    return output_list



'''
패스워드 관련 함수
'''

#패스워드 있는지 없는지 패스워드 기본값은 키워드는 password 옵션은 value 값은 "" 없음
def have_password():
    config = configparser.ConfigParser()
    config.read(path)

    tmp = config.get("PASSWORD", "value")

    if tmp is "":
        print('test1:',tmp)
        return False
    else:
        print('test2:',tmp)
        return True

# 맨처음 패스워드 설정하고 난이후에 패스워드 바꿀때
def password_change(new_password):
    config = configparser.ConfigParser()
    config.read(path)

    if have_password() is False:
        return print('먼저 비밀번호를 설정해주세요')
    else:
        config.set("PASSWORD",  "value", new_password)

        configFile = open(path, "w+")
        config.write(configFile)
        configFile.close()

#맨처음 패스워드 설정
def password_first_setting(password):
    config = configparser.ConfigParser()
    config.read(path)

    config.set("PASSWORD", "value", password)

    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def get_password():
    config = configparser.ConfigParser()
    config.read(path)
    if have_password():
        tmp = config.get("PASSWORD", "value")
        return tmp
    else:
        return print('비밀번호를 먼저 설정해주세요')





#### Testing..
def left_configbox_text(text):#필터링검색어 클릭했을때 내용표시해주는 함수
    #text는 클릭했을때 받아옴
    config = configparser.ConfigParser()
    config.read(path)
    b = config.items("LKEYWORD")[text][1]
    return b

def left_configbox_i(i):#필터링할 검색어 뽑아내는 함수(버튼에 저장하는용도)
    config = configparser.ConfigParser()
    config.read(path)
    # a = config.get("KEYWORD","option%d" %b) #필터링할 검색어뽑아내기

    b = config.options("LKEYWORD")[i]

    return b

def right_configbox(i):  # 필터링할 검색어 뽑아내는 함수(버튼에 저장하는용도)
    config = configparser.ConfigParser()
    config.read(path)
    # a = config.get("KEYWORD","option%d" %b) #필터링할 검색어뽑아내기
    a = config.options("RKEYWORD")[i]
    return a

def input_right_table(a):
    #임시값
    config = configparser.ConfigParser()
    config.read(path)
    c = config.get("LKEYWORD","%s" %a)
    config.set("RKEYWORD", "%s" %a, "%s" %c)
    config.remove_option("LKEYWORD", "%s" %a)
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()



def configright(a):
    #임시값
    config = configparser.ConfigParser()
    config.read(path)
    c = config.get("LKEYWORD","%s" %a)
    config.set("RKEYWORD", "%s" % a, "%s" %c)
    config.remove_option("LKEYWORD", "%s" %a)
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()




def input_left_table(text):
    config = configparser.ConfigParser()
    config.read(path)
    c = config.get("RKEYWORD",text)
    config.set("LKEYWORD", text, c)
    config.remove_option("RKEYWORD", text)
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()




if __name__ == '__main__':
    input_right_table('예나')