'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 8장 멀티프로세싱
 - Listener 와 Client 클래스, Client 클래스
 - 이호섭
 - 프로세스간 통신으로 큐나 파이프 대신
   multiprocessing.connection 모듈에서 제공하는
   Listener 와 Client 클래스 사용
   고수준 메시지 기반의 API
   socket or named pip 를 다룰 수 있음

 - Cookbook: https://docs.python.org/3.3/library/multiprocessing.html#modul

 - Terminal 에서 ListenerClass.py 와 함께 실행
'''

from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'secret password') as conn:
    print(conn.recv())
    print(conn.recv_bytes())

    arr = array('i', [0, 0, 0, 0, 0])

    print(conn.recv_bytes_into(arr))
    print(arr)