'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - thread-safe 자료구조를 이용한 Web Crawler
 - REFERENCE: https://github.com/elliotforbes/python-crawler
 - 이호섭
'''

import queue


class CheckableQueue(queue.Queue):

    def __contains__(self, item):
        with self.mutex:
            return item in self.queue


    def __len__(self):
        return len(self.queue)