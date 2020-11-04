'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - ProcessPoolExecutor 객체 사용하기
 - 이호섭
'''

from concurrent.futures import ProcessPoolExecutor
import os
import time


def task():
    time.sleep(1)
    print("Executing our Task on Process {}".format(os.getpid()))


def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()