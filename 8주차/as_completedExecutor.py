'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - as_completed() 메소드 사용하기
 - 이호섭
'''

import time
from urllib.request import Request, urlopen
import urllib.error as URLError
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [
    'http://www.google.com',
    'http://www.naver.com',
    'http://www.acornpub.co.kr',
    'http://www.knu.ac.kr'
]


def checkStatus(url):
    print("Attempting to crawl URL: {}".format(url))
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)

    return response.getcode(), url


def printStatus(statusCode):
    print("URL Crawled with status code: {}".format(statusCode))


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = []

        for url in URLS:
            task = executor.submit(checkStatus, (url))
            tasks.append(task)

        for future in as_completed(tasks):
            printStatus(future.result())


if __name__ == '__main__':
    main()