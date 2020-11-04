'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - ThreadPoolExecutor 객체 사용하기
 - 이호섭
'''

from concurrent.futures import ThreadPoolExecutor
import threading

def task():
    print("Executing our task")
    result = 0

    for i in range(10):
        result += i

    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))


def main():
    # 3개의 작업자 스레드를 가진 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=3)
    # 2개의 작업자에게 task 배정
    task1 = executor.submit(task)
    task2 = executor.submit(task)

if __name__ == '__main__':
    main()