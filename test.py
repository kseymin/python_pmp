import configparser
import os
abspath = os.path.abspath('./config_make/config.cfg')


def test():  # 필터 가져옴
    config = configparser.RawConfigParser()
    config.read(abspath)
    data_list = config.options('RKEYWORD')
    filter_list = list()
    print(data_list)

    for i in data_list:
        filter_list.append(config.get('RKEYWORD', i))

    for i in filter_list:
        print(i)


test()