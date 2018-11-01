# Real Time Search import
import main_operator as mo
import copy_defender as cd
from multiprocessing import Process
from concurrent.futures import Executor
from concurrent import futures
def main():
    process_list = []
    pname_list = ['notepad', 'winword', 'POWERPNT', 'excel', 'AcroRd32']

    with futures.ProcessPoolExecutor() as executor:
        executor.map(cd.clear_clipboard)
        executor.map(mo.run,pname_list)

    # with futures.ThreadPoolExecutor(max_workers=6) as executor:
    #     executor.submit(cd.clear_clipboard,)
    #     executor.map(mo.run,pname_list)







    # process = Process(target=cd.clipboard_copy_monitor, name='copyDefender')
    # process_list.append(process)
    # process.start()
    #
    #
    # for pname in pname_list:
    #     process = Process(target=mo.run, args=(pname,), name=pname)
    #     process_list.append(process)
    #     process.start()
    #
    #
    #
    # for p in process_list:
    #     p.join()
    #     print('Real Time process : ' +p.name +' is Running..')

if __name__ == '__main__':
    main()