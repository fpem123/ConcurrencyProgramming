'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - Timer 컨텍스트 관리자 정의
 - 이호섭
'''

from timeit import default_timer as dt


class Timer(object):

    def __init__(self, verbos=False):
        self.verbos = verbos
        self.timer = dt

    # with 진입시 자동 호출
    def __enter__(self):
        self.start = dt()
        return self

    # with 탈출시 자동 호출
    def __exit__(self, *args):
        end = dt()
        self.elapsed = end - self.start

        if self.verbos:
            print("Time taken to execute function: {}".format(self.elapsed))
