'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - Class Decorator 함수 구현 예
 - 이호섭
'''

from threading import Lock

# decorator maker
def lock_class(methodnames, lockfactory):
    # 클래스 메소드들을 decorating 하는 decorator lambda 함수
    return lambda cls: make_threadsafe(cls, methodnames, lockfactory)

# 메소드에 lock 메커니즘을 추가하여 반환
def lock_method(method):
    if getattr(method, '__is_locked', False):
        raise TypeError("Method %r is already locked!"% method)

    def locked_method(self, *arg, **kwargs):
        with self._lock:
            return method(self, *arg, **kwargs)

    locked_method.__name__ = '%s(%s)'%('lock_method', method.__name__)
    locked_method.__is_locked = True

    return locked_method

def make_threadsafe(cls, methodnames, lockfactory):
    init = cls.__init__

    def newinit(self, *arg, **kwarg):
        init(self, *arg, **kwarg)
        self._lock = lockfactory()

    cls.__init__ = newinit

    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)

    return cls

@lock_class(['add', 'remove'], Lock)
class ClassDecoratorLockedSet(set):
    @lock_method
    def lockedMethod(self):
        print("This section of our code would be thread safe")
        pass
