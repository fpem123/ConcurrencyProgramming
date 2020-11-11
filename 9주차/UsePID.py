'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - PID를 사용하여 프로세스 식별하기
 - 이호섭
 - process identifier == PID
   PID는 실행할 때마다 바뀐다!
'''


import multiprocessing as mp
import time


def childTask():
    # current_process()에 pid가 있다.
    print("Child Process with PID: {}".format(mp.current_process().pid))
    time.sleep(3)
    print(("Child process terminating"))


def main():
    print("Main process PID: {}".format(mp.current_process().pid))
    myProcess = mp.Process(target=childTask)
    myProcess.start()
    myProcess.join()


if __name__ == '__main__':
    main()