'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - Event 객체를 이용한 자식 스레드 제어법
 - 이호섭
'''

import threading
import time

def myThread(myEvent):
    # myEvent는 이 함수를 종료시키기 위한 Event 객체다.
    while not myEvent.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("my Event has been set")

def main():
    myEvent = threading.Event()
    thread1 = threading.Thread(target=myThread, args=(myEvent,))
    thread1.start()

    print("I will call set after 10 sec")
    time.sleep(10)
    # myEvent를 set 하여 thread1을 종료시킨다.
    myEvent.set()

if __name__ == '__main__':
    main()