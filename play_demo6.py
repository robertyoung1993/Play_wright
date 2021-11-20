"""
demo6
"""

from multiprocessing import Pool
import os
import time
import random

def multi_process_task(name):
    print("任务名称：%s (%s)..." % (name, os.getpid()))
    start_point = time.time()
    time.sleep(random.random() * 3)
    end_point = time.time()
    print('任务%s跑了 %0.2f 秒.' % (name, (end_point - start_point)))

if __name__ == '__main__':
    print('父进程 %s.' % os.getpid())
    p  = Pool(4)
    for i in range(5):
        p.apply_async(multi_process_task, args=(i, ))
    print('等待所有的进程完成')
    p.close()
    p.join()
    print("所有的进程结束了！！！")

