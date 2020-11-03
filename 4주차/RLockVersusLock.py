'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - RLock과 기존 Lock 프리미티브 비교
 - 이호섭
'''

import threading
import time

# 교착 상태를 유발하는 Lock 프리미티브 클래스
class myWorker():

    def __init__(self):
        self.a = 1
        self.b = 2
        # RLock 대신 Lock 사용
        self.lock = threading.Lock()

    def modifyA(self):
        with self.lock:
            print("{}".format(self.lock))
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.lock:
            print("{}".format(self.lock))
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.lock:
            print("RLock acquired, modifying A and B")
            print("{}".format(self.lock))
            self.modifyA()
            print("{}".format(self.lock))
            self.modifyB()
            print("{}".format(self.lock))

        print("{}".format(self.lock))


# modifyA 와 modifyB의 with문을 제거하면 정상동작, 단일 스레드
class myWorker2():

    def __init__(self):
        self.a = 1
        self.b = 2
        # RLock 대신 Lock 사용
        self.lock = threading.Lock()

    def modifyA(self):
        print("{}".format(self.lock))
        self.a = self.a + 1
        time.sleep(5)

    def modifyB(self):
        print("{}".format(self.lock))
        self.b = self.b - 1
        time.sleep(5)

    def modifyBoth(self):
        with self.lock:
            print("RLock acquired, modifying A and B")
            print("{}".format(self.lock))
            self.modifyA()
            print("{}".format(self.lock))
            self.modifyB()
            print("{}".format(self.lock))

        print("{}".format(self.lock))

#workerA = myWorker()
workerA = myWorker2()
workerA.modifyBoth()