'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - Manager와 Namespaces
 - 이호섭
 - 프로세스간 통신으로 multiprocessing 의 Manager 를 사용
   멀티스레드 프로그램의 동기화 프리미티브인 큐를 멀티프로세스에서 사용
   Manager 객체로 큐를 공유할 수 있다.
'''

import multiprocessing as mp
#import queue


def myTask(queue):
    value = queue.get()
    print("Process {} Popped {} from th shared"
          "Queue".format(mp.current_process().pid, value))
    queue.task_done()


def main():
    m = mp.Manager()
    sharedQueue = m.Queue()
    sharedQueue.put(2)
    sharedQueue.put(3)
    sharedQueue.put(4)

    process1 = mp.Process(target=myTask, args=(sharedQueue,))
    process1.start()

    process2 = mp.Process(target=myTask, args=(sharedQueue,))
    process2.start()

    process3 = mp.Process(target=myTask, args=(sharedQueue,))
    process3.start()

    process1.join()
    process2.join()
    process3.join()


if __name__ == '__main__':
    main()
