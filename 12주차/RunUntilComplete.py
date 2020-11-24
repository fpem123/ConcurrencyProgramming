'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - run_until_complete() 사용하기
 - 이호섭
 - Future 객체가 완료될 때까지 실행을 지속하는 run_until_complete() 사용하기
'''


import asyncio
import time


async def myWork():
    print('Starting Work')
    time.sleep(5)
    print('Ending Work')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myWork())
    # 루프를 중단시킴
    loop.stop()
    print('Loop Stopped')
    # 종료되어 있는 루프를 닫고 콜백을 정리
    loop.close()
    print(loop.is_closed())


if __name__ == '__main__':
    main()