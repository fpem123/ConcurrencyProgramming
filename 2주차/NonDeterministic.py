'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 2장 병렬화
 - 비결정적 요소를 가진 코드
 - 이호섭
'''

import threading
import time
import random

# 끝나지 않는 프로그램!!

counter = 1


def workerA():
    global counter

    while counter < 1000:
        counter += 1
        print("Worker A is incrementing counter to {}".format(counter))
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)


def workerB():
    global counter

    while counter > -1000:
        counter -= 1
        print("Worker B is decrementing counter to {}".format(counter))
        sleepTime = random.randint(0, 1)
        time.sleep(sleepTime)


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