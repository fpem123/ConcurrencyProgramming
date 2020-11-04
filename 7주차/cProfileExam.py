'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - cProfile 사용 예제
 - 이호섭

cProfile 사용법
 >> python -m cProfile cProfileExam.py

ncalls:     호출 횟수
tottime:    라인 또는 함수가 실행되는데 걸린 전체 시간
percall:    tottime을 ncalls로 나눈 값
cumtime:    라인 혹은 함수가 실행되는데 소비한 누적 시간
tottime:    cumtime을 ncalls로 나는 값
filename:lineno(function):  실제 측정할 라인 혹은 함수
'''

import collections

doubleEndedQueue = collections.deque('123456')
print("Deque: {}".format(doubleEndedQueue))

doubleEndedQueue.append('1')
print("Deque: {}".format(doubleEndedQueue))

doubleEndedQueue.appendleft('6')
print("Deque: {}".format(doubleEndedQueue))