'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - Timer 컨텍스트 관리자 객체 사용하기
 - 이호섭
'''

from week7.Timer import Timer
from urllib.request import Request, urlopen
import ssl


def myFunction():
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE

    with Timer(verbos=True) as t:
        req = Request('https://tutorialedge.net', headers={'User-Agent':'Mozilla/5.0'})
        response = urlopen(req, context=myssl)

    print("Elapsed Time: {} seconds".format(t.elapsed))


myFunction()