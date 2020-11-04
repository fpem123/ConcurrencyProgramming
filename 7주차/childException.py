'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - 자식 스레드에서 발생한 예외 처리하기
 - 이호섭
'''

import sys
import threading
import time
import queue


def myThread(queue):
    while True:
        try:
            time.sleep(2)
            raise Exception("Exception Thrown in Child Thread {}".format(threading.current_thread()))
        except:
            queue.put(sys.exc_info())


myQueue = queue.Queue()
myThread = threading.Thread(target=myThread, args=(myQueue,))
myThread.start()

while True:
    try:
        exception = myQueue.get()
    except queue.Empty:
        pass
    else:
        print("Child Exception: {}".format(exception))
        break