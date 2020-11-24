'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - asyncio 모듈의 Lock 사용하기
 - 이호섭
 - asyncio 모듈의 Lock 프리미티브는 threading 모듈의 표준 lock 과 기능적으로 거의 동일
   Critical section 을 특정 시점에 하나의 coroutine 만이 실행되도록 lock 을 걸 수 있는 프리미티브
'''

import asyncio
import time


async def myWorker(name, lock):
    # lock.acquire
    # with await lock: # 구버전
    async with lock:
        print(lock)
        # 대충 위험 영역
        print("{} myWorker has attained lock, modifying variable".format(name))
        time.sleep(2)
    # lock.release()
    print(lock)
    print("{} myWorker has released the lock".format(name))


async def main(loop):
    # asyncio 의 Lock 객체 생성
    lock = asyncio.Lock()
    await asyncio.wait([myWorker('A', lock), myWorker('B', lock)])


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(loop))
finally:
    loop.close()