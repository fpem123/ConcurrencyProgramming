'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - 데몬 프로세스 정의하고 실행하기
 - 이호섭
 - 스레드의 데몬 스레드와 거의 동일한 패턴
   데몬 프로세스는 자식 프로세스를 생성할 수 없다!
'''


import multiprocessing
import time


def daemonProcess():
    print("Starting my Daemon Process")
    print("Daemon process started: {}".format(multiprocessing.current_process()))
    time.sleep(3)
    print("Daemon process terminating")


def main():
    print("Main preocess: {}".format(multiprocessing.current_process()))
    myProcess = multiprocessing.Process(target=daemonProcess)
    myProcess.daemon = True     # myProcess를 데몬으로 만든다
    myProcess.start()

    print("We can carry on as per usual and our daemon will continue to execute")
    time.sleep(11)


if __name__ == '__main__':
    main()
