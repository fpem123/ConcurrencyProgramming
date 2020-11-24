'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 9장 이벤트 기반 프로그래밍
 - 호스트 이름을 IP 주소로 변환하기
 - 이호섭
'''

import gevent
from gevent import socket


def main():
    urls = ['www.google.com', 'www.python.org', 'www.naver.com', 'www.kangwon.ac.kr']
    # Greenlet 생성
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=2)
    print([job.value for job in jobs])


if __name__ == '__main__':
    main()