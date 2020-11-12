'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - PyCSP 에서 멀티프로세스 실행하기
 - 이호섭
 - 순차적인 프로세스 통신
   다수의 병행 모델이 어떻게 상호작용하는지 표현
   병행 프로세스간 메시지 전송매체로 주로 channel 을 이용
   Clojure Golang Go 의 주요 기반 기술
   
 - CSP 라이브러리
   표준 파이썬 모듈만 사용하여 분산 통신 모델을 제공
   2006년에 개발이 시작되어 드물게 신버전을 release함 == 라이브러리가 안정화
   데코레이터를 사용해 멀티프로세스 기반 파이썬 APP 을 구현하는 새로운 개념 제시
   
 - install 필요: python -m pip install pycsp
'''

from pycsp.parallel import *
import time


# 데코레이터를 이용해 함수를 프로세스로 만든다!
@process
def process1():
    time.sleep(1)
    print("process1 exiting")


@process
def process2():
    time.sleep(2)
    print("process2 exiting")


# block
Parallel(process1(), process2())
print("program terminating")