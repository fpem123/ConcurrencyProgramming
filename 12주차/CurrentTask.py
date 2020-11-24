'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - current_task() 사용하기
 - 이호섭
 - loop 에 의해 현재 실행중인 Task 객체를 반환
   실행중인 Task 가 없으면 None 을 반환
'''

import asyncio


async def myCoroutine():
    print("My Coroutine")


async def main():
    current = asyncio.Task.current_task()
    # asyncio.current_task(loop=None) -> 3.7 이상부턴 이거 사용
    print(current)


loop = asyncio.get_event_loop()

try:
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.run_until_complete(main())
finally:
    loop.close()