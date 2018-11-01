import win32clipboard  # pywin32
import time
import format_manager  # format_manager.py
import filtering_manager  # filtering_manager.py
import configparser
import os

"""
OpenClipboard() 사용시 반드시 CloseClipboard()를 사용해 닫아주어야 한다.
예외처리에 수정을 가할 경우 주의할 것 
"""


def clear_clipboard():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    # 클립보드 초기화


def check_filtering(filter_list, text, file_name):
    if filtering_manager.text_filtering(filter_list, text):
        clear_clipboard()
        print("[{}] is privacy file!! Delete!!".format(file_name))
    else:
        print("[{}] is not privacy file".format(file_name))


def file_filtering(filter_list, path):
    file_path, file_name, file_ext = filtering_manager.get_fileinfo_from_fullpath(path)
    #파일 확장자 확인 - 확장자에 따라 parsing - filter_list를 참조해 필터링
    if file_ext == ".txt":
        text = format_manager.read_txt(path)
        check_filtering(filter_list, text, file_name)

    elif file_ext == ".pdf":
        text = format_manager.pdf_change_format(path)
        check_filtering(filter_list, text, file_name)

    elif file_ext == ".pptx":
        text = format_manager.pptx_change_format(path)
        check_filtering(filter_list, text, file_name)

    elif file_ext == ".docx":
        text = format_manager.word_change_format(path)
        check_filtering(filter_list, text, file_name)

    elif file_ext == ".xlsx":
        text = format_manager.excel_change_format(path)
        check_filtering(filter_list, text, file_name)

    # else:
    #     print("Skip this file")


def get_filter():  # 필터 가져옴
    abspath = os.path.abspath('../config_make/config.cfg')
    #for test
    #abspath = os.path.abspath('./config_make/config.cfg')
    config = configparser.RawConfigParser()
    config.read(abspath)
    data_list = config.options('RKEYWORD')
    filter_list = list()

    for i in data_list:
        filter_list.append(config.get('RKEYWORD', i))

    return filter_list


def clipboard_copy_monitor():

    while True:
        filter_list = get_filter()

        try:
            # case: 파일 복사
            win32clipboard.OpenClipboard()
            tmp_value = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
            win32clipboard.CloseClipboard()

            for filename in tmp_value:
                path = filename
            # path = 복사한 파일의 경로

            file_filtering(filter_list, path)

        except:
            # case: 텍스트 복사(클립보드 데이터가 파일이 아닌경우)
            try:
                text_data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                # text_data = 복사된 텍스트

                if filtering_manager.text_filtering(filter_list, text_data):
                    print("Privacy TEXT copy detected!! Delete data!!")
                    clear_clipboard()

            except:
                # case: 클립보드에 데이터 = NULL
                win32clipboard.CloseClipboard()
                #print("No data")

        #time.sleep(1)
        # loop delay(~/sec)
