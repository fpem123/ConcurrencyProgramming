'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - 자식 스레드의 예외 처리
 - 이호섭
'''

from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


def isEven(n):
    print("Checking if {} is even".format(n))

    if type(n) != int:
        raise Exception("Value entered is not an integer")

    if n % 2 == 0:
        print("{} is even".format(n))
        return True
    else:
        print("{} is odd".format(n))
        return False


def main():
    try:
        with ThreadPoolExecutor(max_workers=4) as executor:
            task1 = executor.submit(isEven, (2))
            task2 = executor.submit(isEven, (3))
            task3 = executor.submit(isEven, ('t'))

        for future in concurrent.futures.as_completed([task1, task2, task3]):
            print("Result of Task: {}".format(future.result()))

    except Exception as e:
        print("Exception from the child: {}".format(e))

if __name__ == '__main__':
    main()
