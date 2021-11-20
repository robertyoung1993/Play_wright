"""
demo12
"""

import threading


balance = 0
lock1 = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(2000000):
        # 先获取锁
        lock1.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock1.release()



t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(9,))
t4 = threading.Thread(target=run_thread, args=(10,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)