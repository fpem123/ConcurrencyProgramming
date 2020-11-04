'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - 코드에서 timeit 모듈 사용하기 2
 - 이호섭
'''

import timeit
import time


def func1():
    print("Function 1 Executing")
    time.sleep(3)
    print("Function 1 complete")


def func2():
    print("Function 2 Executing")
    time.sleep(2)
    print("Function 2 complete")


t1 = timeit.Timer("func1()", setup="from __main__ import func1")
times = t1.repeat(repeat=2, number=1)

for t in times:
    print("{} seconds".format(t))


t2 = timeit.Timer("func2()", setup="from __main__ import func2")
times = t2.repeat(repeat=3, number=1)

for t in times:
    print("{} seconds".format(t))