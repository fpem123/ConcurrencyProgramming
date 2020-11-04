'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - line_profiler의 kernprof의 @profile 사용
 - 이호섭

kernprof 사용법
 >> pip install line_profiler ## 에러남!!!!
 >> python -m kernprof -l line_profilerExam.py
'''

import random
import time

@profile
def slowFunction():
    time.sleep(random.randint(1, 5))
    print("Slow Function Executed")


def fastFunction():
    print("Fast Function Executed")


def main():
    slowFunction()
    fastFunction()


if __name__ == '__main__':
    main()
