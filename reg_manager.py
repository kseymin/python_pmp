import winreg


REG_PATH = r"Software\Microsoft\excel.sheet.8\shell\command"


def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None



print(get_reg('default'))

#
# key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Microsoft\Outlook Express', 0, KEY_ALL_ACCESS)
# QueryValueEx(key, "InstallRoot")