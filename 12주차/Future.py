'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - Future 객체 사용하기
 - 이호섭
 - asyncio.Future 객체는 concurrent.futures.Future 객체와 개념적으론 거의 동일
   구현상 약간의 차이가 존재
'''

import asyncio


async def myFuture(future):
    await asyncio.sleep(1)
    # future 객체의 결과 설정
    future.set_result("My Future Has Completed")


async def main():
    future = asyncio.Future()
    # future.result()를 사용하기 전에 ensure_future()가 완료되어야 함 => await 필요
    await asyncio.ensure_future(myFuture(future))
    # 이게 ensure_future 보다 먼저 실행되면 에러!
    print(future.result())


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()