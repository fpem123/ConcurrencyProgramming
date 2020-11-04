'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - 소수 결정 프로그램의 실행 방식 속도 비교
 - 이호섭
'''

import timeit
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math

PRIMES = [
    112272535095293, 112582705942171,
    112272535095293, 115280095190773,
    115797848077099, 112272535095293,
    115280095190773, 115797848077099,
    112272535095293, 115280095190773,
    115797848077099, 112272535095293,
    115280095190773, 115797848077099,
    1099726899285419]

# 아리스토테네스의 체를 이용한 소수 판별 메소드
# cpu bound job
def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    t1 = timeit.default_timer()
    # ProcessPoolExecutor 방식
    with ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

    print("{} Seconds Needed for ProcessPoolExecutor\n".format(timeit.default_timer() - t1))

    t2 = timeit.default_timer()
    # ThreadPoolExecutor 방식
    with ThreadPoolExecutor(max_workers=3) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

    print("{} Seconds Needed for ThreadPoolExecutor\n".format(timeit.default_timer() - t1))

    t3 = timeit.default_timer()
    # 단일 스레드 방식
    for number in PRIMES:
        isPrime = is_prime(number)
        print("{} is prime: {}".format(number, isPrime))

    print("{} Seconds Needed for single threaded execution\n".format(timeit.default_timer() - t1))

if __name__ == '__main__':
    main()