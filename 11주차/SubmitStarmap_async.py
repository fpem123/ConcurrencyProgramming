'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - starmap() 메소드 사용하기
 - 이호섭
 - multiprocessing.Pool 의 starmap()를 이용해 process pool 에 작업 전달하기.
   튜플이 함수들에게 인수로 전달.
   starmap을 병렬적으로 수행 가능
'''


from multiprocessing import Pool
import time


def myTask(x, y):
    time.sleep(x/2)

    return y * 2


def main():
    with Pool(4) as p:
        print(p.starmap_async(myTask, [(4, 3), (2, 1)]).get())


if __name__ == '__main__':
    main()