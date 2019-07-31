'''
threading.local的作用
 threading.local()这个方法是用来保存一个全局变量，
 但是这个全局变量只有在当前线程才能访问，如果你在开发多线程应用的时候，
 需要每个线程保存一个单独的数据供当前线程操作，可以考虑使用这个方法，简单有效。代码示例
'''
import random
import threading


g = threading.local()

def worker():
    g.x = random.randint(1, 5)
    print(threading.current_thread(), g.x)

if __name__ == '__main__':
    for i in range(20):
        threading.Thread(target=worker).start()