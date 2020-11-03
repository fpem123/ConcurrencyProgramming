'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - FIFO Queue 사용
 - 이호섭
'''

import threading
import queue
import random
import time

# 스레드에게 주어질 Work
# queue = FIFO Queue
def mySubscriber(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()
        time.sleep(1)

# LifoQueue 생성, Stack
myQueue = queue.LifoQueue()

for i in range(10):
    myQueue.put(i)

print("Queue Populated")

threads = []

for i in range(2):
    thread = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Queue is empty")