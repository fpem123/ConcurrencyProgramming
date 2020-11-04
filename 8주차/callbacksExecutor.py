'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - 콜백 함수 사용하기
 - 이호섭
'''

from concurrent.futures import ThreadPoolExecutor


def task(n):
    print("Processing {}".format(n))


def taskDone(fn):

    if fn.cancelled():
        print("Our {} Future has been cancelled".format(fn.arg))
    elif fn.done():
        print("Our Task has completed")


def secondTaskDone(fn):
    print("I didn't think this would work")


def main():
    print("Starting ThreadPoolExecutor")

    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, (2))
        # callback 함수 등록
        future.add_done_callback(taskDone)
        future.add_done_callback(secondTaskDone)

    print("All tasks complete")

if __name__ == '__main__':
    main()