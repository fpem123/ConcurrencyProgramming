'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - set에 대한 Decorator 메소드 정의 예
 - 이호섭
'''

from threading import Lock

# decorator 메소드
def locked_method(method):
    # wrapper 메소드
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return newmethod


##  DecoratorLockedSet(set)
#   set 을 상속받아 thread-safe 를 보장하는 set 을 만드는 클래스
#   add(), remove(), in operator 에 대해
#   Decorator 를 사용하여 thread-safe 를 주입한다.
class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(DecoratorLockedSet, self).__init__(*args, **kwargs)

    # thread-safe 'add()'
    @locked_method
    def add(self, elem):
        return super(DecoratorLockedSet, self).add(elem)

    # thread_safe 'remove()'
    @locked_method
    def remove(self, elem):
        return super(DecoratorLockedSet, self).remove(elem)

    # thread-safe 'in operator'
    @locked_method
    def __contains__(self, elem):
        return super(DecoratorLockedSet, self).__contains__(elem)