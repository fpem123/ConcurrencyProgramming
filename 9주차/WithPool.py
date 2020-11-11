'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - with로 Pool 객체 사용하기
 - 이호섭
 - 컨텍스트 관리자로 프로세스 풀 제어하기
'''

from multiprocessing import Pool


def task(n):
    print(n)

    return 2*n


def main():
    with Pool(4) as p:
        print(p.map(task, [2, 3, 4]))


if __name__ == '__main__':
    main()