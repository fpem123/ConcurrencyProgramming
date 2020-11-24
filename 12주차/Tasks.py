'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - Task 생성하기
 - 이호섭
 - Task 는 Future 와 유사한 객체
   루프 내에서 스케줄링 되어 CPU 를 할당받아 실행 가능
'''


import asyncio
import time


async def myTask(n):
    time.sleep(1)
    print("Processing {}".format(n))


async def myGenerator():
    # 5개의 Task 생성
    for i in range(5):
        asyncio.ensure_future(myTask(i))

    print("Completed Tasks")
    # awaitable 객체의 실행이 완료될 때까지 실행을 중단.
    # awaitable: coroutine, Task, Future
    await asyncio.sleep(2)


def main():
    loop = asyncio.get_event_loop()
    # myGenerator Task 생성
    loop.run_until_complete(myGenerator())
    loop.close()


if __name__ == '__main__':
    main()