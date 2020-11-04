'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - decorator 함수를 활용한 벤치마킹
 - 이호섭
'''

import random
import timeit
import time


# decorator
def timethis(func):
    # wrapper
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        # 벤치마킹 함수 실행
        value = func(*args, **kwargs)
        runtime = timeit.default_timer() - start_time

        print("Function {} took {} seconds to run".format(func.__name__, runtime))

        return value

    return function_timer


@timethis
def long_runner():
    for x in range(3):
        sleep_time = random.choice(range(1, 3))
        time.sleep(sleep_time)

if __name__ == '__main__':
    long_runner()
