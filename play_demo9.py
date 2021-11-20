"""
多进程 join()
"""

import threading
import time


def test(num):
    time.sleep(1)
    print(num)

# 定义一个用来装子进程的列表
threads = []

for i in range(5):
    thread = threading.Thread(target=test, args=[i])
    threads.append(thread)



for i in threads:
    i.start()
    i.join()

print('end')