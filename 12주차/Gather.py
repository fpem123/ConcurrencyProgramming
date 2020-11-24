'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - gather() 사용하기
 - 이호섭
 - aws iterable 에 있는 awaitable 객체들을 병행적으로 실행
   awaitable 객체가 coroutine 이면, 자동적으로 Task 객체로 스케줄링
   반환 값의 순서는 aws 의 awaitable 순서와 일치
'''

import asyncio


async def factorial(name, num):
    f = 1

    for i in range(2, num + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({num}) = {f}")

    return f


async def main():
    res = await asyncio.gather(factorial("A", 2), factorial("B", 3), factorial("C", 4))
    print("Result from gather(): {}".format(res))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()