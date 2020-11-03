'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 한 번에 모든 스레드 시작하기
 - 이호섭
'''

import threading
import time
import random

def executeThread(i):
    print("Thread {} started".format(i))
    sleepTime = random.randint(1, 10)
    time.sleep(sleepTime)
    print("Thread {} finished executing".format(i))

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads: ", threading.enumerate())