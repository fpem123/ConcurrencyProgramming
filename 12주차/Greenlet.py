'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - Greenlet 서브클래스 정의하기
 - 이호섭
 - gevent 네트워크 라이브러리는 코루틴 상단에 위치, 이벤트 기반 파이썬 네트워크 애플리케이션 개발에 사용
   분산 프로그램 구현에 사용
   설치: pip install gevent
 - greenlet: gevent 프레임워크의 핵심
   C 언어로 작성된 매우 가벼운 coroutine, 협동적으로 스케줄링 가능
   스레드와 유사한 객체를 제공, 멀티스레드 실행의 오버헤드 없이 동시성 실행을 할 수 있도록 함
'''

import gevent
from gevent import Greenlet


# Greenlet 의 서브 클래스 정의
class MyNoopGreenlet(Greenlet):

    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds

    # start() 메소드 호출시 실행
    def _run(self):
        print("My Greenlet executing")
        gevent.sleep(self.seconds)

    def __str__(self):
        return 'MyNoopGreenlet(%s)' % self.seconds


# Greenlet의 서브 클래스 객체 생성 (의사 스레드)
g = MyNoopGreenlet(4)
g.start()
g.join()
print(g)
print(g.dead)