'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - cProfile 사용 예제 2
 - 이호섭

cProfile 사용법
 >> python -m cProfile cProfileExam2.py
'''

import threading
import random
import time


def myWorker():
    for i in range(5):
        print("Starting wait time")
        time.sleep(random.randint(1, 5))
        print("Completed Wait")


thread1 = threading.Thread(target=myWorker)
thread2 = threading.Thread(target=myWorker)
thread3 = threading.Thread(target=myWorker)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()