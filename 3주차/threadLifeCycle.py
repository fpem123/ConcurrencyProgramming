'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 스레드 라이프 사이클 예제
 - 이호섭
'''

import threading
import time

def threadWorker():
    # Running state
    print("My Thread has entered the 'Running' State")
    # suspend, Not-Runnable state
    time.sleep(10)
    # terminate
    print("My Thread is terminating")

# New state
myThread = threading.Thread(target=threadWorker)

# Runnable state
myThread.start()

# Dead state
myThread.join()

print("My Thread has entered a 'Dead' state")