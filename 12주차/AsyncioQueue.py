'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - asyncio.Queue 사용하기
 - 이호섭
 - asyncio.Queue 구현은 표준 queue.Queue 구현과 거의 동일
'''


import asyncio
import random
import time


# 뉴스 Producer 코루틴
async def newsProducer(myQueue):
    while True:
        # Queue 사용 대기
        await myQueue.put(random.randint(1, 5))
        # Consumer 가 꺼내갈 수 있도록 대기
        await asyncio.sleep(1)


# 뉴스 Consumer 코루틴
async def newsConsumer(myQueue):
    while True:
        # Queue 사용 대기
        article = await myQueue.get()
        print("News Reader Consumed News Article {}".format(article))


# Queue 객체 생성
myQueue = asyncio.Queue()

loop = asyncio.get_event_loop()

loop.create_task(newsProducer(myQueue))
loop.create_task(newsConsumer(myQueue))

try:
    loop.run_forever()
finally:
    loop.close()