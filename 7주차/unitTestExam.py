'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 6장 디버깅과 벤치마킹
 - 단위 테스트 예
 - 이호섭
'''

import unittest

def simpleFunction(x):
    return x + 1

##  SimpleFunctionTest(unittest.TestCase)
#   simpleFunction을 테스트하는 클래스
class SimpleFunctionTest(unittest.TestCase):

    # 테스트 시작 전에 실행되는 method
    def setUp(self):
        print("This is run before all of our tests have a chance e to execute")

    # 논리에 맞는 테스트 케이스
    def test_simple_function(self):
        print("Testing that our function works with positive tests")
        self.assertEqual(simpleFunction(2), 3)
        self.assertEqual(simpleFunction(2341234213478923641123), 2341234213478923641124)
        self.assertEqual(simpleFunction(0), 1)

    # 논리에 어긋나는 테스트 케이스
    def test_negative_simple_function(self):
        print("Testing that our function works with negative tests")
        self.assertNotEqual(simpleFunction(2), 4)
        self.assertNotEqual(simpleFunction(0), -1)

    # 테스트 종료 후에 실행되는 method
    def tearDown(self):
        print("This is executed after all of our tests have completed\n")


if __name__ == '__main__':
    unittest.main()