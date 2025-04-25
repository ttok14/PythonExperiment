
# class C:
#     def AA(self, text):
#         print(text)
        
#         def wrapper(func):
#             print(text)
#             func()
#         return wrapper

# cc = C()

# @cc.AA("TEXT")
# def D():
#     print("DD")
    
# D()

# quit()


#------------------------------------#

# 데코레이터를 배우기 전에 파이썬이 어떻게 코드를
# 읽어서 함수를 실행하는지를 간략하게 이해할 필요가 있겠음 . 

# 파이썬은 위에서 아래로 코드를 읽어나가다
# 다음 줄을 만나는 순간 say_hello 함수를 메모리에
# 할당하고 주소를 저장해서 
# say_hello() 라는 구문을 만나면 해당 함수가 호출시키도록함 .

def say_hello():
    print("Say Hello")

say_hello()

# 즉 위는 사실 
# say_hello = 함수생성
# say_hello 함수 실행
# 의 과정을 거침.

#-------------------------------------#

# 그럼 이전 예제들에서 구현했던 것을 
# 데코레이터란 것을 사용해서 구현해보도록 하겠음 .

# 데코레이터를 사용하면 say_hello() 의 함수를
# 재구현하지 않고도 뒤에 "함수 끝!" 문자열을 출력할 수가 있게됨 .

# 먼저 데코레이터 함수를 구현해보자 

# 데코레이터로 사용할 아래 함수를 살펴보면은 

# 1. 파라미터로는 func 라는 함수를 받는다
def decorator(func):
    # 2. 함수안에서 wrapper 란 함수를 새로 생성한다 
    def wrapper():
        # 3. wrapper 함수는 현재 decorator 함수의 파라미터로 
        #    들어온 func 함수를 호출하고 
        func()
        # 4. "함수 끝!" 이라는 문자열을 출력하는 함수이다 
        print("함수 끝!")
        
    return wrapper

def f1():
    print("f1")
    
def f2():
    print("f2")

# decorator 함수에서 생성해서 반환해준 
# 함수는 각각 다른 함수가 된다. 
f1_ex = decorator(f1)
f2_ex = decorator(f2)

# 다른 결과가 출력된다 
f1_ex()
f2_ex()

#------------------------#

# 데코레이터 함수를 이용하면 이전 예제에서 본 것을 
# 훨씬 손쉽게 할수있음.
# 일단 보자 .
        
# 이전 예제와 똑같은 데코레이터 함수 
def decorator(func):
    def wrapper():
        func()
        print("함수 끝!")
        
    return wrapper

# 이전 예제에서의 f1 함수위에 @decorator 가 추가됐음
# 함수 정의부 위에 골뱅이 @ 을 붙이면 무슨일이 벌어질까? 
@decorator
def f1():
    print("f1")

# 일단 실행해본다.

# 결과는 예상대로
# "
# f1
# 함수 끝!
# "
# 으로 나온다

# 무슨 일이 벌어진거냐? 

# 1. 파이썬이 위에서 아래로 코드를 읽어나간다
# 2. @decorator 를 읽어들인다
# 3. 파이썬은 @ 즉 데코레이터를 발견한다
# 4. 파이썬은 f1 의 데코레이터 함수인 decorator 를 호출하는데
#       이때 자기 자신인 f1 을 호출한다. 
#       즉 decorator(f1) 을 호출하고 그 결과값 함수를 f1 에 대입한다.
# 5. 즉 f1 = decorator(f1) 가 된다. 이때 decorator 의 파라미터로
#       f1 이 넘어갔기 때문에 이 시점에 생성된 decorator 안의 wrapper 함수안에서의
#       func() 는 f1 이 된다 . 
# 6. 이제 f1 을 호출하게 되면 f1 함수의 구현부에 있는 내용이 아닌 decorator 의 wrapper 함수가
#       호출이 된다.
f1()
