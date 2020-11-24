'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - asyncio.Task.cancel() 사용하기
 - 이호섭
 - 특정 Task 를 취소하기
'''


import asyncio


async def myCoroutine():
    print("My Coroutine")


async def main():
    current = asyncio.current_task(loop=None)
    print(current)


loop = asyncio.get_event_loop()

try:
    task1 = loop.create_task(myCoroutine())
    task2 = loop.create_task(myCoroutine())
    task3 = loop.create_task(myCoroutine())

    #3번 작업을 취소
    task3.cancel()

    loop.run_until_complete(main())
finally:
    loop.close()