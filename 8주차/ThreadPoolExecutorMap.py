'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - ThreadPoolExecutor 객체와 map() 함수
 - 이호섭
'''

from concurrent.futures import ThreadPoolExecutor

values = [2, 3, 4, 5, 6, 7, 8]

def multiplyByTwo(n):
    return 2 * n


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiplyByTwo, values)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()