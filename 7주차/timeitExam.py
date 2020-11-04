'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - 코드에서 timeit 모듈 사용하기 1
 - 이호섭
'''

import timeit
import time


def func1():
    print("Function 1 Executing")
    time.sleep(5)
    print("Function 1 complete")


def func2():
    print("Function 2 Executing")
    time.sleep(6)
    print("Function 2 complete")


start_time = timeit.default_timer()
func1()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
func2()
print(timeit.default_timer() - start_time)