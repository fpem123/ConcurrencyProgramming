'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - list를 확장하여 만든 thread-safe list
 - 이호섭
'''

from threading import Lock

class LockedList(list):

    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(LockedList, self).__init__(*args, **kwargs)

    def remove(self, elem):
        with self._lock:
            super(LockedList, self).remove(elem)

    def insert(self, i, elem):
        with self._lock:
            super(LockedList, self).insert(i, elem)

    def __contains__(self, elem):
        with self._lock:
            super(LockedList, self).__contains__(elem)