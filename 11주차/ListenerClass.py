'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - Listener 와 Client 클래스, Listener 클래스
 - 이호섭
 - 프로세스간 통신으로 큐나 파이프 대신
   multiprocessing.connection 모듈에서 제공하는
   Listener 와 Client 클래스 사용
   고수준 메시지 기반의 API
   socket or named pip 를 다룰 수 있음

 - Cookbook: https://docs.python.org/3.3/library/multiprocessing.html#modul
   
 - Terminal 에서 ClientClass.py 와 함께 실행
'''

from multiprocessing.connection import Listener
from array import array

# 로컬호스트의 6000번 포트 사용
address = ('localhost', 6000)   # AF_INET


# authkey 가 일치한 주소만 허용하여 address 에 연결
with Listener(address, authkey=b'secret password') as listener:
    with listener.accept() as conn:
        print('connection accepted from', listener.last_accepted)

        conn.send([2.25, None, 'junk', float])
        conn.send_bytes(b'hello')
        conn.send_bytes(array('i', [42, 1729]))
