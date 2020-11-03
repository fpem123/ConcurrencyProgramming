'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - Queue 가 빌 때까지 계속 추출
 - 이호섭
'''

import threading
import queue
import time

def mySubscriber(queue):
    time.sleep(1)

    while not queue.empty():
        item = queue.get()

        if item is None:
            break

        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()

myQueue = queue.Queue()

for i in range(5):
    myQueue.put(i)

print("Queue Populated")

thread = threading.Thread(target=mySubscriber, args=(myQueue,))
thread.start()

print("Not Progressing Till Queue is Empty")
myQueue.join()
print("Queue is now empty")