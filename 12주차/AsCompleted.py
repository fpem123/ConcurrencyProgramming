'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - as_completed() 사용하기
 - 이호섭
 - aws(awaitables)의 awaitable 객체들을 병행적으로 실행시키고
   coroutine 들의 iterator 를 반환
'''

import asyncio


async def myWorker(number):
    return number * 2


async def main(coros):
    # aws 집합들을 동시에 수행
    for coro in asyncio.as_completed(coros):
        # 먼저 도착한 순서대로 출력된다.
        print(await coro)

coros = [myWorker(i) for i in range(5)]

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(coros))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
