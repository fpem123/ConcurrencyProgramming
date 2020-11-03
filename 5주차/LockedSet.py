'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - set 을 확장하여 만든 thread-safe set
 - http://stackoverflow.com/a/13618333/2903188
 - 이호섭
'''

from threading import Lock

##  class LockedSet(set)
#   set 을 상속받아 thread-safe 를 보장하는 set 을 만드는 클래스
#   add(), remove(), in operator 에 대해 thread-safe 를 주입한다.
class LockedSet(set):
    def __init__(self, *args, **kwargs):
        # Lock 메커니즘 추가
        self._lock = Lock()
        # 나머지는 그대로
        super(LockedSet, self).__init__(*args, **kwargs)

    # thread-safe 'add()'
    def add(self, elem):
        with self._lock:
            super(LockedSet, self).add(elem)

    # thread-safe 'remove()'
    def remove(self, elem):
        with self._lock:
            super(LockedSet, self).remove(elem)

    # thread-safe 'in operator'
    def __contains__(self, elem):
        with self._lock:
            super(LockedSet, self).__contains__(elem)

