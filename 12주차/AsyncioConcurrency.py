'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트기반 프로그래밍
 - 과제 5번
 - 이호섭
 - asyncio 기반 파이썬 동시성 프로그램
'''

import asyncio
import time


# 리스트를 입력받아 리스트의 평균을 구하고
# 2초간 sleep 하는 method
async def average(a):
    result = sum(a) / len(a)
    time.sleep(2)

    return result


# average() 코루틴을 호출해 결과를 출력하는 method
async def printAvg(a):
    result = await average(a)

    print('Average for {nums} is {avg}'.format(nums=a, avg=result))


def main():

    nums = [10, 50, 40, 100, 80]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(printAvg(nums))
    loop.close()


if __name__ == '__main__':
    main()