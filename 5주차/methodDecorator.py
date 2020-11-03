'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - 일반적인 메소드 데코레이터 예
 - 이호섭
'''

# decorator 메소드
def uppercase_decortor(func):
    # wrapper() 메소드
    def wrapper():
        str = func()
        make_uppercase = str.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

# 데코레이터 메소드 호출
decorate = uppercase_decortor(say_hi)
print(decorate())

# @ 기호를 이용한 데코레이터 메소드 호출
@uppercase_decortor
def say_hi2():
    return 'hello there'

print(say_hi2())