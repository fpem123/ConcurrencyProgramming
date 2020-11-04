'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 2장 병렬화
 - 웹 크롤링
 - 이호섭
'''


import urllib.request
import time
from bs4 import BeautifulSoup


t0 = time.time()
req = urllib.request.urlopen('http://www.example.com')
t1 = time.time()
print("Total Time to Fetch Page: {} seconds".format(t1 - t0))

soup = BeautifulSoup(req.read(), "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

t2 = time.time()

print("Total Execution Time: {} seconds".format(t2 - t1))