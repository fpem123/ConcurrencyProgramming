'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - wait() 사용하기
 - 이호섭
 - aws iterable 에 있는 awaitable 객체들을 병행적으로 실행하고
   return_when 에 기술된 조건이 만족될 때까지 블록됨
'''

import asyncio


async def myCoroutine(i):
    print("My coroutine {}".format(i))


loop = asyncio.get_event_loop()

try:
    tasks = []

    for i in range(4):
        tasks.append(myCoroutine(i))

    loop.run_until_complete(asyncio.wait(tasks))
finally:
    loop.close()