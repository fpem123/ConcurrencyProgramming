'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 4장 스레드간 동기화
 - 티켓 판매 프로그램
 - 이호섭
'''

import threading
import time
import random

## TicketSeller(threading.Thread)
#  티켓 판매 스레딩 클래스
class TicketSeller(threading.Thread):
    ticketsSold = 0    # 티켓 판매 수량

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print("Ticket Seller Started Work")

    def run(self):
        global ticketAvailable      # 셀러들이 공유할 공유자원
        running = True

        while running:
            # 셀러들에게 랜덤 딜레이를 준다.
            # 제거시 하나의 셀러가 모든 티켓을 팔아버린다.
            self.randomDelay()

            # 크리티컬 섹션에 들어가기 전에 acquire를 해야 한다,
            self.sem.acquire()

            # 공유자원의 값을 조정하는 크리티컬 섹션
            if ticketAvailable <= 0:
                running = False
            else:
                self.ticketsSold += 1
                ticketAvailable -= 1
                print("{} Sole One ({} left)".format(self.getName(), ticketAvailable))

            # 크리티컬 섹션 조작 완료
            self.sem.release()
        print("Ticket Seller {} Sold {} tickets in total".format(self.getName(), self.ticketsSold))

    def randomDelay(self):
        time.sleep(random.randint(0, 3))


# 세마포어 카운터의 기본값은 1
semaphore = threading.Semaphore()
# 공유 변수, 판매할 티켓의 양
ticketAvailable = 100

sellers = []
for i in range(4):
    seller = TicketSeller(semaphore)
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()