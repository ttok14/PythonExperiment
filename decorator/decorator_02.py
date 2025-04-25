
#------------------------------------#

def say_hello():
    print("Say Hello")
    
# 위 say_hello 함수 실행이 끝나고 
# "함수 끝!" 이라는 문자를 출력하고 싶다고 하자

# 방법 1.---------------------------------#
def say_hello_newVersion_01():
    say_hello()
    print("함수 끝!")

say_hello_newVersion_01()

# 방법 2.------------------------------------#
def say_hello_newVersion_02(func):
    func()
    print("함수 끝!")

say_hello_newVersion_02(say_hello)
#------------------------------------------#

# 방법 3.------------------------------------#
# 데코레이터를 사용해서 구현하기 (decorator_03.py)