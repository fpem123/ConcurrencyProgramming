'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - all_task() 사용하기
 - 이호섭
 - 아직 끝나지 않은 Task 객체의 집합을 반환
'''

import asyncio


async def myCoroutine():
    print("My Coroutine")


async def main():
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()

try:
    # Task 3개 등록
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())

    #pending = asyncio.Task.all_tasks()
    pending = asyncio.all_tasks(loop)
    print(pending)
    loop.run_until_complete(main())
finally:
    loop.close()