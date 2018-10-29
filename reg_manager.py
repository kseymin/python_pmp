import winreg
import configparser

# 레지스트리 경로
OFFICE_REG_PATH_LIST = [r'Excel.Sheet.12\shell\Open\command', r'Excel.Sheet.8\shell\Open\command',
                 r'Word.Document.12\shell\Open\command', r'Word.Document.8\shell\Open\command',
                 r'PowerPoint.Show.12\shell\Open\command', r'PowerPoint.Show.8\shell\Open\command']

ACRORD_REG_PATH = r'AcroExch.Document.DC\shell\Read\command'


# 현재 MS Office (Word, Excel, PowerPoint)의 open shell command 레지스트리 데이터 GET
def get_office_reg(name, reg_backup_list):  # name = 'command'
    for REG_PATH in OFFICE_REG_PATH_LIST:
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            reg_backup_list.append(value)
        except WindowsError:
            print("error")
            pass

    return reg_backup_list


# 현재 Adobe Acrobat PDF Reader의 open shell command 레지스트리 데이터 GET
def get_acrord_reg(name, reg_backup_list):  # name = ''
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, ACRORD_REG_PATH, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        reg_backup_list.append(value)
    except WindowsError:
        print("error")
        pass

    return reg_backup_list


# 리스트(the_list)전체에서 특정 값(val) 제거
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


# 기존 레지스트리 데이터를 변경할 레지스트리 데이터로 변환
def reg_data_modify(reg_backup_list, reg_data_list):
    j = 0
    for i in reg_backup_list:
        reg_data = i.split(" ")
        reg_data = remove_values_from_list(reg_data, '')

        if j < 4:
            if r'"%1"' not in reg_data and r"/x" not in reg_data:
                reg_data.append(r'/x "%1"')
            elif r'"%1"' not in reg_data:
                reg_data.append(r'"%1"')
            elif r'/x' not in reg_data:
                reg_data.remove('"%1"')
                reg_data.append(r'/x "%1"')
            else:
                pass

        elif j < 6:
            if r'"%1"' not in reg_data:
                reg_data.append('"%1"')
            else:
                pass

        else:
            if r'"%1"' not in reg_data and r"/n" not in reg_data:
                reg_data.append(r'/n "%1"')
            elif r'"%1"' not in reg_data:
                reg_data.append(r'"%1"')
            elif r'/n' not in reg_data:
                reg_data.remove('"%1"')
                reg_data.append(r'/n "%1"')
            else:
                pass

        s = ' '.join(reg_data)
        reg_data_list.append(s)
        j += 1

    return reg_data_list


def edit_acrord_reg(name, reg_data_list):  # name = ''   원본 데이터 리스트 입력 시 원상복구
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, ACRORD_REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, reg_data_list[6])
        winreg.CloseKey(registry_key)
    except WindowsError:
        print("error")
        pass


def edit_office_reg(name, reg_data_list):  # name = 'command'   원본 데이터 리스트 입력 시 원상복구
    i = 0
    for REG_PATH in OFFICE_REG_PATH_LIST:
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, reg_data_list[i])
            winreg.CloseKey(registry_key)
        except WindowsError:
            print("error")
            pass
        i += 1


def regbackup_set(reg_backup_list):  # regbackup변경하는 함수
    config = configparser.RawConfigParser()
    data_list = ['Excel.Sheet.12', 'Excel.Sheet.8', 'Word.Document.12', 'Word.Document.8',
                 'PowerPoint.Show.12', 'PowerPoint.Show.8', 'AcroExch.Document.DC']
    for i in range(0, 7):
        config.read("test.cfg")
        config.set("regbackup", data_list[i], reg_backup_list[i])
        configFile = open("test.cfg", "w+")
        config.write(configFile)
        configFile.close()


def reg_setup():  # 최초 실행시 레지스트리 환경설정
    reg_backup_list = list()  # 기존 레지스트리 데이터 백업
    reg_data_list = list()  # 변경할 레지스트리 데이터

    reg_backup_list = get_office_reg('command', reg_backup_list)
    reg_backup_list = get_acrord_reg('', reg_backup_list)  # (기본값)

    regbackup_set(reg_backup_list)

    reg_data_list = reg_data_modify(reg_backup_list, reg_data_list)

    edit_office_reg('command', reg_data_list)
    edit_acrord_reg('', reg_data_list)
    for i in reg_data_list:
        print(i)
    print("Registry Setup Complete")


def reg_restore():  # 백업되어있는 레지스트리 데이터 복원
    config = configparser.RawConfigParser()
    data_list = ['Excel.Sheet.12', 'Excel.Sheet.8', 'Word.Document.12', 'Word.Document.8',
                 'PowerPoint.Show.12', 'PowerPoint.Show.8', 'AcroExch.Document.DC']
    reg_backup_data = list()
    config.read("test.cfg")
    for i in range(0, 7):
        reg_backup_data.append(config.get('regbackup', data_list[i]))

    for i in reg_backup_data:
        print(i)
    edit_office_reg('command', reg_backup_data)
    edit_acrord_reg('', reg_backup_data)
    print("Registry Restore Complete")