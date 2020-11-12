'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - 파일에 로깅하기
 - 이호섭
 - 문제를 확일할 때 작동상황을 보여주는 정보 Logging
   잘 만들어진 로깅 시스템은 장기간에 걸쳐 App 의 동작을 이해할 수 있는 좋은 수단!
 - Cookbook: https://docs.python.org/3/howto/logging-cookbook.html
'''

import logging
from multiprocessing import Pool
import time

# 로깅 방법 설정
# filename=log 파일, level=로깅수준(critical, error, warning, info, debug, notset
# format=출력방식, (프로세스 이름, 로깅시간, 로깅수준, 메시지)
logging.basicConfig(filename='myapp.log', level=logging.INFO,
                    format='%(processName)-10s %(asctime)s %(levelname)s %(message)s')


def myTask(n):
    # 로깅될 %(message)
    logging.info("{} being processed".format(n))
    logging.info("Final Result: {}".format(n*2))
    time.sleep(n)

    return n * 2


def main():
    with Pool(4) as p:
        p.map(myTask, [2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()