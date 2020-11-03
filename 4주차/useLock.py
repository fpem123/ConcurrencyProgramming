'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - Lock을 사용해 counter 증감 프로그램 보완
 - 이호섭
'''

import threading
import time
import random

counter = 1                 # 공유 변수
lock = threading.Lock()     # Lock 객체 생성

def workerA():
    global counter
    lock.acquire()

    try:
        while counter < 1000:
            counter += 1
            print("Worker A is incrementing counter to {}".format(counter))
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()

    try:
        while counter > -1000:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
    finally:
        lock.release()

def main():
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time()

    print("Execution Time {}".format(t1-t0))

if __name__ == '__main__':
    main()