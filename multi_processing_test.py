import main_operator as mo

from multiprocessing import Process

if __name__ == '__main__':
    pname_list = ['notepad', 'winword', 'POWERPNT', 'excel', 'AcroRd32']

    threads = []
    process_list = []

    for pname in pname_list:
        process = Process(target=mo.run, args=(pname,),name=pname)
        process_list.append(process)

    for p in process_list:
        print(p.name)
        p.start()





