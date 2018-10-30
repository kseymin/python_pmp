import configparser , os.path
import AES_maker as am



AES_key = 'mysecretpassword'


#config access
#아래 는 이 코드를 메인으로 돌릴때
#abspath = os.path.abspath('./config_make/config.cfg')

abspath = os.path.abspath('../config_make/config.cfg')
isabspath = abspath





def make_key(password):
    pwd = password

    cipher = am.AESCipher(AES_key)
    encrypted = cipher.encrypt(pwd)

    config = configparser.RawConfigParser()
    config.read(isabspath)



    config.set("PASSWORD", "value", encrypted)

    configFile = open(isabspath, "w+")
    config.write(configFile)
    configFile.close()




    return 'password maked'

#키가 설정도있는지 보는 함수
def exist_pwd():
    config = configparser.ConfigParser()
    config.read(isabspath)

    pwd = config.get("PASSWORD", 'value')

    flag = True

    if pwd is not '':
        return flag
    else:
        flag = False
        return flag



def is_key_right(password):
    ##  암호화된 패스 워드 를 읽어와서 비교
    ## 맞으면 True
    flag = False

    config = configparser.ConfigParser()
    config.read(isabspath)

    existpwd = config.get("PASSWORD", 'value')
    tmpstr = existpwd[1:]


    if exist_pwd():

        cipher = am.AESCipher(AES_key)
        decrypted = cipher.decrypt(tmpstr)
        print(type (decrypted))

        if password == decrypted:
            flag = True
        else: # 비밀번호 틀릴때 사실상 맨밑에 리턴값으로 잡긴함
            return flag
    else:
        return '먼저 패스워드를 설정해주세요'

    return flag




#def delete_key():


#
#
#
# def change_key(older_password):
#
#     pwd = older_password
#
#     #원래 패스워드가 맞는지 일단확인
#     if is_key_right(pwd):
#         delete_key()
#         make_key()
#     else:
#         print('This older key is not Right')
#
#
#
# ## key  잃어버렸을 때 어떻게?
#
# def make_key_description():
#
# def find_key():





if __name__ == '__main__':

    # make_key('hello')
    # print(exist_pwd())

    #is_key_right('hello')
    #make_key('hello')
    # t=is_key_right('hello2')
    # print(t)

    #make_key('hello')

    make_key("hello")