'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - map() 메소드 사용하기
 - 이호섭
 - multiprocessing.Pool 의 map_async()를 이용해 process pool 에 작업 전달하기.
   iterable 객체를 매핑시킴
   작업을 병렬로 처리
'''

from multiprocessing import Pool
import time


def myTask(n):
    time.sleep(n/2)
    return n * 2


def main():
    print("mapping asynchronously array to pool")

    with Pool(4) as p:
        # 어싱크로노스 함수들은 get()을 이용해야만 값을 꺼내올 수 있다.
        print(p.map_async(myTask, [4, 3, 2, 1]).get())


if __name__ == '__main__':
    main()
