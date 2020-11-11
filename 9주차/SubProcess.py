'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - 서브 프로세스 생성 및 실행
 - 이호섭
 - 멀티프로세싱을 이용하면 파이썬의 GIL 제약을 극복할 수 있다!
'''

import multiprocessing


def myProcess():
    print("Currently Executing Child Process")
    print("This process has it's own instance of the GIL")



def main():
    print("Executing Main Process")
    print("Creating Child Process")

    myPrcs = multiprocessing.Process(target=myProcess, args=())
    myPrcs.start()
    myPrcs.join()

    print("Child Process has terminated, terminating main process")


if __name__ == '__main__':
    main()