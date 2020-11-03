'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 스레드와 프로세스의 정의 및 시작하기
 - 이호섭
'''

import threading
import time
import random

def excuteThread(i):
    print("Thread {} started".format(i))
    sleepTime = random.randint(1, 10)
    time.sleep(sleepTime)
    print("Thread {} finished executing".format(i))

for i in range(10):
    thread = threading.Thread(target=excuteThread, args=(i,))
    thread.start()

    print("Active Thread: ", threading.enumerate())