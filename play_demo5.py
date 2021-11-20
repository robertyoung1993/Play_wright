"""
demo5
"""

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_process(name):
    print('启动子进程 %s (%s)...，我的父进程是 %s ' % (name, os.getpid(), os.getppid()))
    print("子进程执行完毕！")

if __name__ == '__main__':
    print('启动父进程 %s.' % os.getpid())
    p = Process(target=run_process, args=('test', ))
    print('子进程要开始了...')
    # 启动子进程
    p.start()
    # 阻塞主进程，直到子进程执行完毕，才开始执行主进程后续的代码
    #p.join()
    print('子进程结束了，主进程才能继续执行～')