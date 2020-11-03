'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - 인수를 전달받는 일반적인 Decorator 예
 - 이호섭
'''

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the funtion call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"

@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0} {1} {2}".format(function_arg1, function_arg2, function_arg3))


decorated_function_with_arguments(pandas, "Science", "Tools")