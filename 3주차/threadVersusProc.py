'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 스레드와 프로세스의 생성시간 비교
 - 이호섭
'''

import threading
from multiprocessing import cpu_count, Process
import time
import os

def MyTask():
    time.sleep(2)


t0 = time.time()
threads = []

for i in range(4):
    thread = threading.Thread(target=MyTask)
    thread.start()
    threads.append(thread)

t1 = time.time()

print("Total Time for Creating 4 Threads: {} seconds".format(t1-t0))

for thread in threads:
    thread.join()

t2 = time.time()
procs = []

for i in range(cpu_count()):
    process = Process(target=MyTask())
    process.start()
    procs.append(process)

t3 = time.time()

print("Total Time for Creating 4 Processes: {} seconds".format(t3-t2))

for proc in procs:
    proc.join()