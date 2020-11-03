'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - join() 메소드 사용
 - 이호섭
'''

import threading
import time

def ourThread(i):
    print("Thread {} Started".format(i))
    time.sleep(i*2)
    print("Thread {} Finished".format(i))

def main():
    thread1 = threading.Thread(target=ourThread, args=(1,))
    thread1.start()

    print("Is thread 1 Finished?")

    thread2 = threading.Thread(target=ourThread, args=(2,))
    thread2.start()
    thread2.join()

    print("Thread2 definitely finished")

if __name__ == '__main__':
    main()