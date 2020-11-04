'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - Executor 객체 shutdown 하기
 - 이호섭
'''

import time
from concurrent.futures import ThreadPoolExecutor


def someTask(n):
    print("Executing Task {}".format(n))
    time.sleep(n)
    print("Task {} Finished Executing".format(n))


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(someTask, (1))
        task2 = executor.submit(someTask, (2))
        # executor shutdown
        print(executor.shutdown(wait=True))
        # executor가 shutdown 되어 여기부턴 런타임에러 발생
        task3 = executor.submit(someTask, (3))
        task4 = executor.submit(someTask, (4))


if __name__ == '__main__':
    main()