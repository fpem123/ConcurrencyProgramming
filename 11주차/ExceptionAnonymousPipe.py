'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - os.pipe()로 자식 프로세스의 예외 처리하기
 - 이호섭
 - 프로세스간 통신수단인 파이프를 이용해
   자식 프로세스에서 부모프로세스로 예외를 전달
 - 윈도우에선 실행이 되지 않는다!
   Linux/Unix 에선 가능
'''

import os, sys
import multiprocessing

##
#   name: ChildProcess(multiprocessing.Process)
#   use:  ChildProcess(pipein=쓰기 파이프)
#   role: 익명 파이프에 예외를 작성
#   info: Custom Process
class ChildProcess(multiprocessing.Process):

    def __init__(self, pipin):
        super(ChildProcess, self).__init__()
        self.pipein = pipin


    def run(self):
        try:
            raise Exception("This broke stuff")
        except:
            # exc_info() 매소드를 이용해 예외의 정보를 가져옴
            except_type, except_class, tb = sys.exc_info()

            self.pipein = os.fdopen(self.pipein, 'w')
            # 익명 파이프에 taceback 정보를 작성
            self.pipein.write(str(tb))
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
    print("Exception: {}".format(pipeContent))


if __name__ == '__main__':
    main()