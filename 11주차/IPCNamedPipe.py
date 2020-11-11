'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - os.pipe() 사용하기
 - 이호섭
 - 프로세스간 통신을 위해 이름있는 파이프 생성
   이름있는 파이프도 FIFO 구조이다.
   단방향 통신이며 쌍방향(duplex)을 위해선 2개의 파이프를 만들어야함
   프로세스가 종료되면 제거됨
 - 익명 파이프와는 다르게 윈도우에서 실행 가능
'''

import multiprocessing


##
#   name: ChildProcess(multiprocessing.Process)
#   use:  ChildProcess(conn=쓰기 파이프)
#   role: 네임드 파이프에 무언가를 작성
#   info: Custom Process
class ChildProcess(multiprocessing.Process):

    def __init__(self, conn):
        super(ChildProcess, self).__init__()
        self.conn = conn

    def run(self):
        print("Attempting to pipein to pipe")
        self.conn.send("My name is Hoseop")
        # 파이프 close
        self.conn.close()


def main():
    conn1, conn2 = multiprocessing.Pipe()

    child = ChildProcess(conn2)
    child.start()
    child.join()

    pipContent = conn1.recv()
    print("Pipe: {}".format(pipContent))

    conn1.close()


if __name__ == '__main__':
    main()