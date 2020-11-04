'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - Pdb 대화형 실행 예
 - 이호섭
'''

import time
from urllib.request import Request, urlopen
import ssl


##  class Timer
#   시간을 측정한다
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed = self.end - self.start


def myFunction():
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE

    with Timer() as t:
        import pdb
        # 중단점 생성
        pdb.set_trace()
        req = Request('https://tutorialedge.net', headers={'User-Agent':'Mozilla/5.0'})
        response = urlopen(req, context=myssl)

    print("Elapsed Time: {} seconds".format(t.elapsed))


myFunction()