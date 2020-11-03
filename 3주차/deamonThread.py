'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 3장 스레드 라이프
 - 데몬 스레드 사용
 - 이호섭
'''

import threading
import time

def standardThread():
    print("Starting my Standard Thread")
    time.sleep(5)
    print("Ending my standard Thread")

def daemonThread():
    print("Starting my Daemon Thread")
    while True:
        print("Sending Out Heartbeat Signal")
        time.sleep(2)

if __name__ == '__main__':
    standardThread = threading.Thread(target=standardThread())
    daemonThread = threading.Thread(target=daemonThread())
    daemonThread.setDaemon(True)

    daemonThread.start()
    standardThread.start()