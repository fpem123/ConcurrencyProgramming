'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - RLock을 사용
 - 이호섭
'''

import threading
import time

class myWorker():

    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock()

    def modifyA(self):
        # with으로 자동으로 self.rlock.acquire()
        with self.rlock:
            print("Modyfiying A: RLock Acquired: {}".format(self.rlock._is_owned()))
            print("{}".format(self.rlock))
            self.a = self.a + 1
            time.sleep(5)
            # with가 끝나면 자동으로 self.rlock.release()

    def modifyB(self):
        # with으로 자동으로 self.rlock.acquire()
        with self.rlock:
            print("Modyfiying B: RLock Acquired: {}".format(self.rlock._is_owned()))
            print("{}".format(self.rlock))
            self.b = self.b - 1
            time.sleep(5)
            # with가 끝나면 자동으로 self.rlock.release()

    def modifyBoth(self):
        with self.rlock:
            print("RLock acquired, modifying A and B")
            print("{}".format(self.rlock))
            self.modifyA()
            print("{}".format(self.rlock))
            self.modifyB()
            print("{}".format(self.rlock))

        print("{}".format(self.rlock))

workerA = myWorker()
workerA.modifyBoth()