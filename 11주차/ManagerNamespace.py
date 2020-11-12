'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - Manager와 Namespaces
 - 이호섭
 - 프로세스간 통신으로 multiprocessing 의 Manager 를 사용
   Manager 는 쓰기 가능한 Namespace 속성을 가지고 있으며
   프로세스간 속성들을 공유해야 할 경우 유용하게 활용
'''


import multiprocessing as mp


def myProcess(ns):
    print(ns.x)
    print("ns.x was changed")
    ns.x = 2


def main():
    manager = mp.Manager()
    ns = manager.Namespace()
    ns.x = 1

    print(ns)

    process = mp.Process(target=myProcess, args=(ns,))
    process.start()
    process.join()

    print(ns)


if __name__ == '__main__':
    main()

