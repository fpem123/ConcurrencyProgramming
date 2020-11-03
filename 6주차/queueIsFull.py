'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - Queue 가 full 이 될 때까지 계속 삽입
 - 이호섭
'''

import threading
import queue
import time

def myPublisher(queue):
    while not queue.full():
        queue.put(1)
        print("{} Appended 1 to queue: {}\n".format(threading.current_thread(), queue.qsize()))
        time.sleep(1)

myQueue = queue.Queue(maxsize=10)

threads = []

for i in range(4):
    thread = threading.Thread(target=myPublisher, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()