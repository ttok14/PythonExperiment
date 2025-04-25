
#------------------------------------------#
# 데코레이터 함수 이해하기

# 일반함수 정의 
def say_hello():
    print("Say Hello")

# 쉽죠 ? "Say Hello" 가 출력된다    
say_hello()

# 변수에 초기화한 다음에 그 변수를 함수처럼 호출하는 것도 가능함
sayHelloFunction = say_hello

# 당연히 마찬가지로 say_hello 가 호출됨
sayHelloFunction()