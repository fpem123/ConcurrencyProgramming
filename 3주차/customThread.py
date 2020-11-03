'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 사용자 정의 스래드 클래스
 - 이호섭
'''

from threading import Thread

# Thread를 상속받아 만들어진 사용자 정의 스래드 클래스
class myWorkerThread(Thread):
    i = 0
    # 생성자
    def __init__(self, i):
        self.i = i
        print("Hello World")
        Thread.__init__(self)   # 필수 호출
    # run() is start()
    def run(self):
        print("Thread {} is now running".format(i))

myThread = []

for i in range(10):
    myThread.append(myWorkerThread(i))
    print("Create my Thread Object")
    myThread[i].start()
    print("Started my thread")

for i in range(10):
    myThread[i].join()
    print("My Thread finished")