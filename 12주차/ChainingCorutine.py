'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - Coroutune 연결하기
 - 이호섭
 - 최대한 성능을 높이기 위해 코루틴 호출을 함께 묶어 사용할 수 있음\
 - 공식 문서: https://cpython-test-docs.readthedocs.io/en/latest/library/asyncio-task.html
'''

import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)

    return x + y


async def print_sum(x, y):
    # 코루틴 연결, No await, result 값을 전달받기 전에 print가 실행되 에러를 유발시킨다.
    # result = compute(x, y)
    # 코루틴 연결, Use await, 에러가 없다
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
