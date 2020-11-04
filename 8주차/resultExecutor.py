'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - map() 함수를 활용한 결과 처리하기
 - 이호섭
'''

import time
import random
from concurrent.futures import ThreadPoolExecutor

values = [2, 3, 4, 5, 6, 7, 8]


def mutiplyByTwo(n):
    time.sleep(random.randint(1, 2))
    return 2 * n


def done(n):
    print("Done: {}".format(n))


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(mutiplyByTwo, values)

        for result in results:
            done(result)


if __name__ == '__main__':
    main()