'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - run_forever() 사용하기
 - 이호섭
 - stop()이 호출될 때까지 루프를 계속 실행하는 run_forever()로 이벤트 로프 생성
'''


import asyncio


# 어노테이션으로 코루틴 만들기,
# 곧 사라질 기능이라 사용하면 warning
# @asyncio.coroutine
# def hello_word():
async def hello_world():        # << 신버전
    # 코루틴 block, 다른 Task 가 실행되는 걸 허용함.
    await asyncio.sleep(1)
    print('Hello World')
    # 자신을 Task 로 재귀 등록
    asyncio.ensure_future(hello_world())


async def good_evenig():
    await asyncio.sleep(1)
    print('Good Evening')
    asyncio.ensure_future(good_evenig())


print('step: asyncio.get_event_loop()')
loop = asyncio.get_event_loop()

try:
    print('step: loop.run_forever()')
    asyncio.ensure_future(hello_world())
    asyncio.ensure_future(good_evenig())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print('step: loop.close()')
    loop.close()