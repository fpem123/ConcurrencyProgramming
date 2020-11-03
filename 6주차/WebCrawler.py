'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - thread-safe 자료구조를 이용한 Web Crawler
 - 이호섭
'''

from urllib.request import Request, urlopen
from urllib.parse import urlparse, urljoin
import urllib.error as URLError
import time
import threading
import queue
from bs4 import BeautifulSoup as bs
import ssl

##  class Crawler(threading.Thread)
#   웹을 크롤링하는 클래스
class Crawler(threading.Thread):

    def __init__(self, baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock):
        threading.Thread.__init__(self)
        print("Web Crawler Worker Started: {}".format(threading.current_thread()))
        self.linksToCrawl = linksToCrawl    # crawing할 링크를 저장하는 Queue
        self.haveVisited = haveVisited      # 이미 방문한 링크를 저장하는 리스트
        self.baseUrl = baseUrl              # 방문 링크주소를 구성하는 base URL
        self.urlLock = urlLock              # 쿠에 사용할 동기화 프리미티브
        self.errorLinks = errorLinks        # 에러를 유발한 링크를 저장하는 리스트

    # https를 크롤할 수 있는 context 생성
    def run(self):
        # 요청메시지 생성
        myssl = ssl.create_default_context()
        myssl.check_hostname = False
        myssl.verify_mode = ssl.CERT_NONE

        # 크롤링
        while True:
            self.urlLock.acquire()
            print("Queue Size: {}".format(self.linksToCrawl.qsize()))
            link = self.linksToCrawl.get()
            self.urlLock.release()

            if link is None:
                break

            if link in self.haveVisited:
                print("Already Visited: {}".format(link))
                break

            # 크롤링
            try:
                # urljoin: url을 결합
                link = urljoin(self.baseUrl, link)
                req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(req, context=myssl)

                print("Url {} Crawled with Status: {}".format(response.geturl(), response.getcode()))

                # 페이지에 있는 링크 추출
                soup = bs(response.read(), "html.parser")

                for atag in soup.find_all('a'):
                    if (atag.get('href') not in self.haveVisited) and (urlparse(link).netloc == 'tutorialedge.net'):
                        self.linksToCrawl.put(atag.get('href'))
                    else:
                        print("{} already visited or not part of website".format(atag.get('href')))

                print("adding {} to crawled list".format(link))
                self.haveVisited.append(link)
            except URLError as e:
                print("URL {} threw this error when trying to parse: {}".format(link, e.reson))
                self.errorLinks.append(link)
            finally:
                self.linksToCrawl.task_done()

def main():
    print("Starting our Web Crawler")
    baseUrl = input("Website:\n >> ")
    numberOfThreads = input("Num Threads:\n >> ")

    linkToCrawl = queue.Queue()
    urlLock = threading.Lock()
    linkToCrawl.put(baseUrl)
    haveVisited = []
    crawlers = []
    errorLinks = []

    for i in range(int(numberOfThreads)):
        crawler = Crawler(baseUrl, linkToCrawl, haveVisited, errorLinks, urlLock)
        crawler.start()
        crawlers.append(crawler)

    for crawler in crawlers:
        crawler.join()

    print("Total Number of Pages Visited: {}".format(len(haveVisited)))
    print("Total Number of Pages with Error: {}".format(len(errorLinks)))

if __name__ == '__main__':
    main()