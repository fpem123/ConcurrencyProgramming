'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - os.pipe() 사용하기
 - 이호섭
 - 프로세스간 통신을 위해 익명 파이프 생성
   익명 파이프는 FIFO 구조이다.
   단방향 통신이며 쌍방향(duplex)을 위해선 2개의 파이프를 만들어야함
   os가 종료되면 제거됨
 - 윈도우에선 실행이 되지 않는다!
   Linux/Unix 에선 가능
'''

import os, sys
import multiprocessing

##
#   name: ChildProcess(multiprocessing.Process)
#   use:  ChildProcess(pipein=쓰기 파이프)
#   role: 익명 파이프에 무언가를 작성
#   info: Custom Process
class ChildProcess(multiprocessing.Process):

    def __init__(self, pipin):
        super(ChildProcess, self).__init__()
        self.pipein = pipin


    def run(self):
        print("Attempting to pipein to pipe")
        # 파이프를 쓰기전용으로 파일 오픈, 윈도우 운영체제는 여기서 에러가 뜬다.
        self.pipein = os.fdopen(self.pipein, 'w')
        self.pipein.write("My Name is Hoseop")
        # 파일 오픈 작업을 close
        self.pipein.close()


def main():
    pipeout, pipein = os.pipe()  # 수신 송신

    child = ChildProcess(pipein)
    child.start()
    child.join()

    # 파이프를 close
    os.close(pipein)
    pipeout = os.fdopen(pipeout)

    pipeContent = pipeout.read()
    print("Pipe: {}".format(pipeContent))


if __name__ == '__main__':
    main()