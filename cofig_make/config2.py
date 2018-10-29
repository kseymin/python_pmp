import configparser
#섹션추가하고 값추가하고 저장하는방법
"""
config = configparser.ConfigParser()

config.add_section("KEYWORD")

config.set("KEYWORD", "OPTION1", "VALUE")
"""
"""
config.add_section("password")

config.set("password", "OPTION", "VALUE")
"""
"""
configFile = open("C:/Users/kangmin/Desktop/test/config.cfg", "w+")

config.write(configFile)

configFile.close()

config = configparser.ConfigParser()

config.read("config.cfg")
"""
path = "C:\\Users\\sku205_25\\PycharmProjects\\Layout_ver3\\config.cfg"
def configset2(a):#필터링 할검색어 추가하는 함수

    config = configparser.ConfigParser()
    config.read(path)
    if a == "": #공백을 입력하면 건너띔
        pass
    else: #공백이아니면

        config.set("KEYWORD","%s" %a,"none") #none이 의미하는 바는 기능제한중 복사와 이동만금지시키겠다는뜻.기본값을none으로잡음
        """
        print(config.options("KEYWORD"))
        for i in range(1,len(config.options("KEYWORD"))):
            if config.options("KEYWORD")[i] == None:
                config.set("KEYWORD", "%s" %a, "none")
                break
            else:
                continue
        """
        configFile = open(path, "w+")
        config.write(configFile)
        configFile.close()

def configset3(a,b):# 필터링 할검색어 추가하는 함수 타이틀값은 a 내용은 b

    config = configparser.ConfigParser()
    config.read(path)
    if a == "": #공백을 입력하면 건너띔
        pass
    else: #공백이아니면

        config.set("KEYWORD","%s" %a,"%s" %b) #none이 의미하는 바는 기능제한중 복사와 이동만금지시키겠다는뜻.기본값을none으로잡음
        """
        print(config.options("KEYWORD"))
        for i in range(1,len(config.options("KEYWORD"))):
            if config.options("KEYWORD")[i] == None:
                config.set("KEYWORD", "%s" %a, "none")
                break
            else:
                continue
        """
        configFile = open(path, "w+")
        config.write(configFile)
        configFile.close()

def configright(a):
    #임시값
    config = configparser.ConfigParser()
    config.read(path)
    c = config.get("KEYWORD","%s" %a)
    config.set("RKEYWORD", "%s" % a, "%s" %c)
    config.remove_option("KEYWORD", "%s" %a)
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def configleft(a):
    config = configparser.ConfigParser()
    config.read(path)
    c = config.get("RKEYWORD","%s" %a)
    config.set("KEYWORD", "%s" % a, "%s" %c)
    config.remove_option("RKEYWORD", "%s" %a)
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()



def configdel3(b):  # 필터링할 검색어 삭제하는 함수
    config = configparser.ConfigParser()
    config.read(path)
    # row = 2  # gui와 연동되기전 임시값 ,keyword..
    # a = row  # gui와 연동 keyword버튼의 row값으로 비교

    a = len(config.options("KEYWORD"))
    for i in range(0, a):
        if config.options("KEYWORD")[i] == b:
            config.remove_option("KEYWORD", "%s" % b)
            configFile = open(path, "w+")
            config.write(configFile)
            configFile.close()

            break

        else:
            continue


def confignum(b):#선택한 검색어찾아서 넘버로 반환해주는 함수
    config = configparser.ConfigParser()
    config.read(path)
    b ="option6" #임시값 텍스트로 받아와야함
    a = len(config.options("KEYWORD"))
    for i in range(1,a):
        if config.options("KEYWORD")[i] == b:
            return i
        else:
            continue

def configpasswd2(b):#패스워드 입력받고 저장하는 함수
    config = configparser.ConfigParser()
    config.read(path)


    config.set("password", "value" ,"%s"  %b)

    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def configrestriction(a):#박스클릭했을때 제한기능바꾸는 함수 아무것도 안바꿨을때
    config = configparser.ConfigParser()
    config.read(path)
     #인자값으로 텍스트를 받아와서
    config.set("KEYWORD", "%s"% a,"none") # 아무것도선택안했을때
    configFile = open(path, "w+")
    config.write(configFile)
    configFile.close()

def configbox(text):#필터링검색어 클릭했을때 내용표시해주는 함수
    #text는 클릭했을때 받아옴
    config = configparser.ConfigParser()
    config.read(path)
    b = config.items("KEYWORD")[text][1]
    return b
def openconfig(i):#필터링할 검색어 뽑아내는 함수(버튼에 저장하는용도)
    config = configparser.ConfigParser()
    config.read(path)
    # a = config.get("KEYWORD","option%d" %b) #필터링할 검색어뽑아내기

    b = config.items("KEYWORD")[i][1]

    return b
def configlen():#필터링할 검색어 갯수 알려주는 함수
    config = configparser.ConfigParser()
    config.read(path)
    a = len(config.options("KEYWORD"))
    return a

def rkeywordlen():#오른쪽 키워드 갯수 알아내는 함수
    config = configparser.ConfigParser()
    config.read(path)
    a = len(config.options("RKEYWORD"))
    return a


def openconfigpasswd():#비밀번호를 뽑아내서 비교
    config = configparser.ConfigParser()
    config.read(path)
    b = config.get("password", "value")  # password뽑아내기
    return b




def openconfigright(i):  # 필터링할 검색어 뽑아내는 함수(버튼에 저장하는용도)
    config = configparser.ConfigParser()
    config.read(path)
    # a = config.get("KEYWORD","option%d" %b) #필터링할 검색어뽑아내기
    a = config.options("RKEYWORD")[i]
    return a

def openconfigright2(i):  # 실제 필터링할 검색어 뽑아내는 함수(오른쪽)
    config = configparser.ConfigParser()
    config.read(path)
    # a = config.get("KEYWORD","option%d" %b) #필터링할 검색어뽑아내기

    b = config.items("RKEYWORD")[i][1]

    return b


def configdel2():  # 양쪽에서필터링할 검색어 삭제하고 삭제한 넘버 리턴값으로 알려주는 함수 (삭제한넘버는 -1이므로 +1해줘야함)
    config = configparser.ConfigParser()
    config.read(path)
    b = "oin7"  # 임시값 텍스트로 받아와야함
    a = len(config.options("KEYWORD"))
    c = len(config.options("RKEYWORD"))
    for i in range(0, a):
        if  config.options("KEYWORD")[i] == b:
            config.remove_option("KEYWORD", "%s" % b)
            configFile = open(path, "w+")
            config.write(configFile)
            configFile.close()

            return i

        else:
            continue
    for j in range(0, c):
        if  config.options("RKEYWORD")[j] == b:
            config.remove_option("RKEYWORD", "%s" % b)
            configFile = open(path, "w+")
            config.write(configFile)
            configFile.close()

            return j
        else:
            continue



    """ #길이 구하기
    config = configparser.ConfigParser()
    config.read(path)
    print(len(config.options("KEYWORD")))
    b = config.options("KEYWORD")
    for i in config.options("KEYWORD"):
        print('a')
    """

def passwdcomparison(a):#passwd불러와서 비교하는 함수
    config = configparser.ConfigParser()
    config.read(path)
    b = config.get("password","value")

def passwdcomparison2():#passwd불러와서 비교하는 함수 테스트용
    config = configparser.ConfigParser()
    config.read(path)
    b = config.get("password","value")
    c = config.has_option("password","value")

    if b == "":
        print ("none")
    else :
        print("not none")
    print (b)
    print (c)


if __name__ == "__main__":
    #configset2()
    #configdel()
    #configdel2()
    passwdcomparison2()
    #optres()
    #keyopt()
    #confignum()
    #configdel()
