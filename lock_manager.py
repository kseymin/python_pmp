import AES_maker as am

AES_key = 'mysecretpassword'


def make_key(password):
    pwd = password

    cipher = am.AESCipher(AES_key)
    encrypted = cipher.encrypt(pwd)


    ##  패스워드 를 암호화해서 파일로 저장
    f = open('./pwd.txt', mode='wb')
    f.write(encrypted)
    f.close()

    return 'password maked'

#키가 설정도있는지 보는 함수
def exist_pwd():
    flag = True
    try:
        fp = open("./pwd.txt", "rt")
        fp.close()
    except IOError as e:\
            flag =False
    return flag



def is_key_right(password):
    ##  암호화된 패스 워드 를 읽어와서 비교
    ## 맞으면 True
    flag = False

    if exist_pwd():
        with open('./pwd.txt',mode='rb') as f:
            existpwd = f.read()

            cipher = am.AESCipher(AES_key)
            decrypted = cipher.decrypt(existpwd)

        if password == decrypted:
            flag = True
    else:
        return '먼저 패스워드를 설정해주세요'

    return flag



    return  flag

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

    make_key('hello')
    print(exist_pwd())

    # pwd = 'hi'
    # print(is_key_right(pwd))
