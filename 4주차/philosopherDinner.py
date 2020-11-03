'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - 철학자의 저녁식사 문제
 - 이호섭
'''

import threading
import time
import random

# 교착상태를 유발시키는 철학자 스레드 클래스, 영원히 끝나지 않는다.
class Philosopher(threading.Thread):

    def __init__(self, name, leftFork, rightFork):
        print("{} Has Sat Down At the Table".format(name))
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print("{} has started thinking".format(threading.current_thread().getName()))

        while True:
            time.sleep(random.randint(1, 5))
            print("{} has finished thinking".format(threading.current_thread().getName()))
            self.leftFork.acquire()
            time.sleep(random.randint(1, 5))

            try:
                print("{} has acquired the left fork".format(threading.current_thread().getName()))
                self.rightFork.acquire()
                try:
                    print("{} has attained both forks, currently eating".format(threading.current_thread().getName()))
                finally:
                    self.rightFork.release()
                    print("{} has released the right fork".format(threading.current_thread().getName()))
            finally:
                self.leftFork.release()
                print("{} has released the left fork".format(threading.current_thread().getName()))

# 공유자원
fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

# 경쟁하는 스레드들
philosopher1 = Philosopher("Kant", fork1, fork2)
philosopher2 = Philosopher("Aristotle", fork2, fork3)
philosopher3 = Philosopher("Spinoza", fork3, fork4)
philosopher4 = Philosopher("Marx", fork4, fork5)
philosopher5 = Philosopher("Russell", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()