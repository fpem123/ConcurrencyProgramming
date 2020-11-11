'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - maxtasksperchild 사용하기
 - 이호섭
 - multiprocessing.Pool 을 생성할 때, maxtasksperchild 에 숫자를 줌
   프로세스는 maxtasksperchild 수의 값만큼의 작업을 하고나면 제거되고 새로운 프로세스가 생성됨
   Pool의 원 목적과는 반대되는 행위이지만,
   프로세스가 자원을 반납하지 않고 계속 점유하는 위험을 방지해 줄 수 있음!
'''


from multiprocessing import Pool
import time
import os


def myTask(x, y):
    print("{} Executed my task".format(os.getpid()))

    return y * 2


def main():
    # 풀에 1개의 프로세스 생성, 일을 2개 수행하면 프로세스 재생산
    with Pool(processes=1, maxtasksperchild=2) as p:
        print(p.starmap_async(myTask, [(4, 3), (2, 1), (3, 2), (5, 1)]).get())
        print(p.starmap_async(myTask, [(4, 3), (2, 1), (3, 2), (2, 3)]).get())


if __name__ == '__main__':
    main()