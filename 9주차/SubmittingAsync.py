'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - apply_async() 메소드 사용하기
 - 이호섭
 - apply_async() 를 이용해 process pool 에 작업 전달하기.
   apply_async() 매소드는 병렬적으로 작동한다. 병렬로 처리하고 싶을 떄 사용!
   callback 과 error_callback 을 이용해 콜백과 에러콜백을 등록할 수 있다.
'''

from multiprocessing import Pool
import time
import os


def myCallback(n):
    print("I got a {}!".format(n))


def myTask(n):
    print("Task processed by Process".format(os.getpid()))

    return n * 2


def main():
    print("apply_async")

    with Pool(4) as p:
        tasks = []

        for i in range(4):
            task = p.apply_async(func=myTask, args=(i,), callback=myCallback)
            # 어싱크의 결과는 get()으로 값을 꺼내와야 한다!
            print("Result: {}".format(task.get()))


if __name__ == '__main__':
    main()
