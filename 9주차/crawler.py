'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - Web Crawler 성능 옾이기
 - 이호섭
'''

from urllib.request import Request, urlopen
from urllib.parse import urlparse, urljoin
import urllib.error as URLError
from bs4 import BeautifulSoup as BS
import ssl


#   웹을 크롤링하는 클래스
class Crawler:

    base_url = ''
    # 요청메시지 생성
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE

    # queue가 아닌 set 자료구조 사용
    crawledLinks = set()
    errorLinks = set()

    def __init__(self, baseUrl):
        Crawler.base_url = baseUrl
        Crawler.myssl = ssl.create_default_context()
        Crawler.myssl.check_hostname = False
        Crawler.myssl.verify_mode = ssl.CERT_NONE

    @staticmethod
    def crawl(thread_name, url, linksToCrawl):
        try:
            link = urljoin(Crawler.base_url, url)
            if (urlparse(link).netloc == urlparse(Crawler.base_url).netloc) and (link not in Crawler.crawledLinks):
                request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(request, context=Crawler.myssl)

                Crawler.crawledLinks.add(link)
                print("> URL {} Crawled with Status: {}: {} Crawled In Total".format(response.geturl(), response.getcode(),len(Crawler.crawledLinks)))

                soup = BS(response.read(), "html.parser")
                Crawler.enqueueLinks(soup.find_all('a'), linksToCrawl)

                return url, response.getcode()

        except URLError as e:
            print("URL {} threw this error when trying to parse: {}".format(link, e.reason))
            Crawler.errorLinks.add(link)

            return url, response.getcode()

        except Exception as e:
            Crawler.errorLinks.add(link)

            return url, response.getcode()

    @staticmethod
    def enqueueLinks(links, linksToCrawl):
        for link in links:
            if urljoin(Crawler.base_url, link.get('href')) not in Crawler.crawledLinks:
                if urljoin(Crawler.base_url, link.get('href')) not in linksToCrawl:
                    linksToCrawl.put(link.get('href'))
