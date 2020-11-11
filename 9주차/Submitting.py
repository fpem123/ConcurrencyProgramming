'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - apply() 메소드 사용하기
 - 이호섭
 - apply() 를 이용해 process pool 에 작업 전달하기.
   apply 매소드는 결과가 올 때까지 block 된다, 병렬적이지 않음!
'''

from multiprocessing import Pool
import time

def myTask(n):
    time.sleep(n/2)

    return n * 2


def main():
    with Pool(4) as p:
        print(p.apply(myTask, (4,)))
        print(p.apply(myTask, (3,)))
        print(p.apply(myTask, (2,)))
        print(p.apply(myTask, (1,)))


if __name__ == '__main__':
    main()