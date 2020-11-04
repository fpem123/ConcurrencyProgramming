'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - Web Crawler 성능 올리기
 - REFERENCE: https://github.com/elliotforbes/python-crawler
 - 이호섭
'''

import threading
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from week9.crawler import *
from week9.CheckableQueue import *
import csv

THREAD_COUNT = 4
linksToCrawl = CheckableQueue()


def run(url):
    try:
        result = Crawler.crawl(threading.current_thread(), url, linksToCrawl)
        linksToCrawl.task_done()

        return result

    except:
        raise Exception("Exception thrown with link: {}".format(url))


def appendToCSV(result):
    print("{} Appending result to CSV File: {}".format(threading.current_thread(), result))

    with open('results.csv', 'a') as csvfile:
        resultwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        resultwriter.writerow(result)

def main():
    url = input("Website\n >>")
    Crawler(url)
    linksToCrawl.put(url)

    while not linksToCrawl.empty():
        with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
            url = linksToCrawl.get()
            futures = []

            if url is not None:
                future = executor.submit(run, url)
                futures.append(future)

            for future in as_completed(futures):
                try:
                    if future.result() != None:
                        appendToCSV(future.result())
                except:
                    print(future.exception())

    print("Total Links Crawled: {}".format(len(Crawler.crawledLinks)))
    print("Total Errors: {}".format(len(Crawler.errorLinks)))


if __name__ == '__main__':
    main()