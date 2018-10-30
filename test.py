import configparser
import os
import re
abspath = os.path.abspath('./config_make/config.cfg')

s = "010-3499-4601 씨발이런아ㅓ리ㅏㅓ리ㅏㄷ저ㅣㅏ륃자루ㅏㅣㄷ줘라ㅣㄷ줘라ㅣㅜㄴ아ㅣ"


def test():  # 필터 가져옴
    config = configparser.RawConfigParser()
    config.read(abspath)
    data_list = config.options('RKEYWORD')
    filter_list = list()
    print(data_list)

    for i in data_list:
        data = config.get('RKEYWORD', i)
        if data[0] == "\\":
            filter_list.append(data)

    for i in filter_list:
        p = re.compile(i)
        m = p.findall(s)
        if len(m) > 0:
            print(m)
            print("fuck!")

test()