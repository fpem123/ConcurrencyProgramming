'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 7장 실행자와 Pool
 - 컬러 사진을 흑백 사진으로 변환
 - 이호섭
'''

from PIL import Image
from concurrent.futures import ProcessPoolExecutor

image_file = Image.open("Images/spaceFrog.png")
image_file = image_file.convert('1')
image_file.save('results/result.png')

