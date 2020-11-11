'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - imap_unordered() 메소드 사용하기
 - 이호섭
 - multiprocessing.Pool 의 imap_unordered()를 이용해 process pool 에 작업 전달하기.
   iterable 객체를 매핑시킴, 결과를 iterator 객체로 반환
   작업의 반환이 임의의 순서로 반환됨. 보통은 완료 순서
'''


from multiprocessing import Pool
import time


def myTask(n):
    time.sleep(n + 2)
    return n + 2


def main():
    print("i-mapping array to pool")

    with Pool(4) as p:
        for it in p.imap_unordered(myTask, [1, 3, 2, 1]):
            print(it)


if __name__ == '__main__':
    main()