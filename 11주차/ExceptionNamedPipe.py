'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - multiprocessing.pipe()로 자식 프로세스의 예외 처리하기
 - 이호섭
 - IPC인 named pipe 로
   자식에서 발생한 예외를 부모 프로세스로 전달
'''

import multiprocessing
import sys


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
        try:
            raise Exception("This broke stuff")
        except:
            except_type, except_class, tb = sys.exc_info()

            # 네임드 파이프에 traceback 정보를 작성
            self.conn.send(str(tb))
            self.conn.close()


def main():
    conn1, conn2 = multiprocessing.Pipe()

    child = ChildProcess(conn2)
    child.start()
    child.join()

    pipContent = conn1.recv()
    print("Exception: {}".format(pipContent))

    conn1.close()


if __name__ == '__main__':
    main()
