'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - imap() 메소드 사용하기
 - 이호섭
 - multiprocessing.Pool 의 imap()를 이용해 process pool 에 작업 전달하기.
   iterable 객체를 매핑시킴, 결과를 iterator 객체로 반환
   작업을 병렬로 처리
'''


from multiprocessing import Pool
import time


def myTask(n):
    time.sleep(n + 2)
    return n + 2


def main():
    print("i-mapping array to pool")

    with Pool(4) as p:
        for it in p.imap(myTask, [1, 3, 2, 1]):
            print(it)


if __name__ == '__main__':
    main()