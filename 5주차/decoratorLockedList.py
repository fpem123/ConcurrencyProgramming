'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - Decorator 를 사용해 만든 thread-safe list
 - 이호섭
'''

from threading import Lock
import threading
import time

def locked_method(method):
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)

    return newmethod

class DecoratorLockedList(list):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(DecoratorLockedList, self).__init__(*args, **kwargs)

    @locked_method
    def remove(self, elem):
        return super(DecoratorLockedList, self).remove(elem)

    @locked_method
    def insert(self, i, elem):
        return super(DecoratorLockedList, self).insert(i, elem)

    @locked_method
    def __contains__(self, elem):
        return super(DecoratorLockedList, self).__contains__(elem)

class myThread(threading.Thread):
    def __init__(self, barrier):
        threading.Thread.__init__(self)
        self.barrier = barrier

    def run(self):
        global myList

        t_ident = self.getName()

        myList.append(t_ident)
        print("Thread {} is append Name {}".format(threading.current_thread(), t_ident))

        time.sleep(1)

        myList.remove(t_ident)
        print("{}: My Name is removed".format(threading.current_thread()))

threads = []
barrier = threading.Barrier(4)
myList = DecoratorLockedList()

for i in range(4):
    thread = myThread(barrier)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(myList)