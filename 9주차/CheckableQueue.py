'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - Web Crawler 성능 올리기
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