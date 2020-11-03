'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - Condition 프리미티브 사용
 - 이호섭
'''

import threading
import random
import time

## Publisher(threading.Thread)
#  정수를 생성에 정수배열에 넣는 생산자 스레딩 클래스
#  구독자에게 배열에 새 정수가 있음을 알려 소비하게 한다
class Publisher(threading.Thread):
    def __init__(self, integers, condition):
        self.condition = condition          # Condition 프리미티브 변수 객체
        self.integers = integers            # 공유 배열
        threading.Thread.__init__(self)

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()
            print("Condition Acquired by Publisher: {}".format(self.name))

            self.integers.append(integer)
            print("Publisher {} appending to array: {}".format(self.name, integer))

            self.condition.notify()     # 상태가 변했음을 알려준다.
            print("Condition Released by Publisher: {}".format(self.name))
            self.condition.release()

            time.sleep(1)

## Subscriber(threading.Thread)
#  배열에 새로 생성된 정수가 있다면 알림을 받는 구독자 클래스
#  배열에서 정수를 가져와 소비
class Subscriber(threading.Thread):

    def __init__(self, integers, condition):
        self.condition = condition          # Condition 프리미티브 변수 객체
        self.integers = integers            # 공유 배열
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print("Condition Acquired by Consumer: {}".format(self.name))

            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print("{} Popped from list by Consumer: {}".format(integer, self.name))
                    break

                # condition.notify() 알림이 오기 전까지 대기한다.
                print("Condition Wait by {}".format(self.name))
                self.condition.wait()

            print("Consumer {} Releasing Condition".format(self.name))
            self.condition.release()

def main():
    integers = []       # 공유자원 큐
    condition = threading.Condition()

    pub1 = Publisher(integers, condition)
    pub1.start()

    sub1 = Subscriber(integers, condition)
    sub2 = Subscriber(integers, condition)
    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()

if __name__ == '__main__':
    main()