"""
demo4
"""

import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('我是一个子进程(%s), 我的父进程是(%s).' % (os.getpid(), os.getppid()))
else:
    print("我(%s)仅仅创建了一个子进程(%s)." % (os.getpid(), pid))