'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 1장 시작하기
 - 데이터 센터 파이썬 코드
 - 이호섭
'''


from rx import Observable, Observer

class temperatureObserver(Observer):

    def on_next(self, x):
        print("Temperature isL %s degrees centigrade"%x)

        if x > 6:
            print("Warning: Temperate is Exceeding Recommended Limit")
        if x == 9:
            print("DataCenter is shutting down. Temperature is too high")


    def on_error(self, e):
        print("Error: %s"%e)


    def on_completed(self):
        print("All Temps Read")


# 가상의 온도 값을 생성
xs = Observable.from_iterable(range(10))

# 해당 온도 값을 전달
d = xs.subscribe(temperatureObserver())