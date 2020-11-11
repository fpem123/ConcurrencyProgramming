'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - 자식 프로세스 종료하기
 - 이호섭
 - terminate() 를 이용해 프로세스를 종료할 수 있다
   자원의 낭비를 막기 위함!
'''

import multiprocessing as mp
import time


def myProcess():
    current_prc = mp.current_process()
    print("Child Process PID: {}".format(current_prc.pid))
    time.sleep(20)


def main():
    current_prc = mp.current_process()
    print("Main Process PID: {}".format(current_prc.pid))

    myPrc = mp.Process(target=myProcess)
    myPrc.start()
    time.sleep(5)
    print("My Process has terminated, terminating main thread")

    print("Terminating Child Process")
    # 자식 프로세스 종료하기
    myPrc.terminate()
    print("Child Process Successfully terminated")


if __name__ == '__main__':
    main()