'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - asyncio 의 디버그 모드 사용하기
 - 이호섭
 - asyncio 모듈은 디버깅을 위한 디버그 모드 제공
'''

import asyncio
import logging
import time

# 디버그 레벨 설정
logging.basicConfig(level=logging.DEBUG)


async def myWorker():
    # 로깅 메시지
    logging.info("My Worker Coroutine Hit")
    time.sleep(1)


async def main():
    # 로깅 메시지
    logging.debug("My Main Function Hit")
    await asyncio.wait([myWorker()])


loop = asyncio.get_event_loop()
loop.set_debug(True)    # 이벤트 루프 객체에 debug mode 설정

try:
    loop.run_until_complete(main())
finally:
    loop.close()