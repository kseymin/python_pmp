import main_operator as mo
import copy_defender as cd
from multiprocessing import Process

if __name__ == '__main__':
    pname_list = ['notepad', 'winword', 'POWERPNT', 'excel', 'AcroRd32']

    threads = []
    process_list = []

    filter_list = ['test']

    for pname in pname_list:
        process = Process(target=mo.run, args=(pname,),name=pname)
        process_list.append(process)

    process = Process(target=cd.clipboard_copy_monitor,args=(filter_list,), name = 'copyDefender')
    process_list.append(process)


    for p in process_list:
        print(p.name)
        p.start()





