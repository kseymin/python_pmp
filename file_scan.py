import os
import filtering_manager
import format_manager
import configparser


def get_filter():  # 필터 가져옴
    abspath = os.path.abspath('../config_make/config.cfg')
    config = configparser.RawConfigParser()
    config.read(abspath)
    data_list = config.options('RKEYWORD')
    filter_list = list()

    for i in data_list:
        filter_list.append(config.get('RKEYWORD', i))

    return filter_list


def file_scanning(dir_path):  # 스캔 시작경로
    filter_list = get_filter()
    detected_list = []  # 개인정보가 포함된 파일 경로가 저장될 list

    for (path, dir, files) in os.walk(dir_path):  # 하위 디렉토리 검색
        for filename in files:
            if "~$" in filename:
                ext = " "
            else:
                ext = os.path.splitext(filename)[-1].lower()  # ext = 파일확장자(소문자)
                full_path = path + "/" + filename  # full_path = 현재 검색중인 디렉토리 / 파일명
                print(full_path)  # 스캔한 파일 log 출력

            # 확장자별 파일 필터링
            if ext == '.txt':
                text = format_manager.read_txt(full_path)  # full_path 파일내용 -> text
                if filtering_manager.text_filtering(filter_list, text):  # filter_list에 따라 text 필터링
                    detected_list.append(full_path)  # 필터링된 파일 기록
            # 이하 파일 종류에 따라 동일과정 반복

            elif ext == '.pdf':
                text = format_manager.pdf_change_format(full_path)
                if filtering_manager.text_filtering(filter_list, text):
                    detected_list.append(full_path)

            elif ext == '.pptx':
                text = format_manager.pptx_change_format(full_path)
                if filtering_manager.text_filtering(filter_list, text):
                    detected_list.append(full_path)

            elif ext == '.docx':
                text = format_manager.word_change_format(full_path)
                if filtering_manager.text_filtering(filter_list, text):
                    detected_list.append(full_path)

            elif ext == '.xlsx':
                text = format_manager.excel_change_format(full_path)
                if filtering_manager.text_filtering(filter_list, text):
                    detected_list.append(full_path)

            elif ext == '.bmp' or ext == '.jpg' or ext == '.png' or ext == '.gif':
                text = format_manager.image_change_format(full_path)
                if filtering_manager.text_filtering(filter_list, text):
                    detected_list.append(full_path)

            else:
                pass

    return detected_list

    # print("\n\n==============================Detected files==============================\n\n")
    # for i in detected_list:
    #     print(i)


# file_scanning("C:/Users/baron/Desktop/TestDir")