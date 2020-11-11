'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - Process의 서브 클래스로 프로세스 생성하기
 - 이호섭
 - threading.Thread 클래스의 서브 클래스를 정의하는 것 처럼
   process 도 서브 클래스 정의가 가능하다!
'''

import multiprocessing as mp
import os


class MyProcess(mp.Process):

    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print("Child Process PID: {}".format(mp.current_process().pid))


def main():
    print("Main process PID: {}".format(mp.current_process().pid))
    myPrc = MyProcess()
    myPrc.start()
    myPrc.join()

    processes = []

    for i in range(os.cpu_count()):
        prc = MyProcess()
        processes.append(prc)
        prc.start()

    for prc in processes:
        prc.join()


if __name__ == '__main__':
    main()