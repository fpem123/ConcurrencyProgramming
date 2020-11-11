'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - map() 메소드 사용하기
 - 이호섭
 - multiprocessing.Pool 의 map()를 이용해 process pool 에 작업 전달하기.
   iterable 객체를 매핑시킴
   apply() 처럼 결과가 올 때까지 block됨
'''

from multiprocessing import Pool
import time


def myTask(n):
    time.sleep(n/2)
    return n * 2


def main():
    print("mapping array to pool")

    with Pool(4) as p:
        print(p.map(myTask, [4, 3, 2, 1]))


if __name__ == '__main__':
    main()
