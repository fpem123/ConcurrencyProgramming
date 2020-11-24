'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - asyncio 를 사용한 이벤트 기반 프로그램 코드
 - 이호섭
 - asyncio 모듈이 제공하는 API들로 코루틴과 메소드를 생성
'''

import asyncio


# 코루틴 정의
async def myCoroutine():
    print("Simple Event Loop Example")


def main():
    # 이벤트 루프 생성
    loop = asyncio.get_event_loop()
    # myCoroutine 메서드를 Task로 등록 후 끝날 때까지 루프
    loop.run_until_complete(myCoroutine())
    # 루프 종료
    loop.close()


if __name__ == '__main__':
    main()