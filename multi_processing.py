'''
进程之间通信的demo
'''

from multiprocessing import Queue, Process
import time, random

l = ['python', 'java', 'js']

def write(queue):
    '''
    向队列中添加数据
    :param queue:
    :return:
    '''
    for value in l:
        print(f'正在向队列种添加数据->{value}')
        queue.put_nowait(value)
        time.sleep(random.random())

def read(queue):
    while True:
        if not queue.empty():
            value = queue.get_nowait()
            print(f'从队列种获取的数据为->{value}')
        else:
            break

if __name__ == '__main__':
    queue = Queue()
    write_data = Process(target=write, args=(queue, ))
    read_data = Process(target=read, args=(queue, ))

    write_data.start()
    write_data.join()
    print('*' * 20)
    read_data.start()
    read_data.join()

