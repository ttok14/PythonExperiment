
# 함수 인자로 * 와 ** 가 사용되는 경우엔 
# 임의의 개수의 위치 인자(Positional argument) 와
# 임의의 개수의 키워드 인자(Keyword argument)를 
# 받을때 사용됨 

# * 을 붙이는 경우는 (관례적으로 * 하나는 args)
# * 튜플로서 묶여들어옴 *
def myFunction_args(arg1, *args):
    print(f"필수 인자 (arg1) : {arg1}")
    print(f"나머지 위치 인자들 (*args 튜플) : {args}")
    print(f"*args 의 타입 {type(args)}")
    
    if args:
        print("args 인자들")
        
        # enumerate 는 list 나 tuple 같은 iterable 자료형을 받아 
        # 각 요소를 튜플로 재구성함 (인덱스 , 요소의 값)
        # 구성된 enumerate 객체를 반환해주는데 이 객체도 역시
        # iterable 하기에 for 문 순회가 가능 .
        # 새로 구성된 각 요소는 튜플(인덱스, 기존 요소) 이기에 unpacking 을
        # 적용해 아래와 같이 순회가 가능.
        for i, v in enumerate(args):
            print(f"index : {i} , value : {v}")

myFunction_args(100, "a", "b", "c")

myFunction_args(200, "a", 999, "c")

# 언패킹 활용
numberList = [1, 2, 3]
myFunction_args("STAR", *numberList)

#----------------------------------------------------------------------#

print("#----------------------------------------------------------------#")

# * 을 2개 붙이는 경우 관례적으로 kwargs(keyword arguments) 란 
# 매개변수명을 사용함 . 
# 키워드 인자는 country="korea" 와 같이 넘기는 인자를 의미 

# ** 로 넘어온 인자는 모든 키워드 인자들을 !! 하나의 Dictionary !! 로
# 묶어서 받게됨 ( key 는 키워드 인자의 이름(문자열), 값에는 전달한 값 )
# 어떤 종류의 키워드 인자가 얼마나 전달될지 모를때 유용함 
def myFunction_kwargs(**kwargs):
    if kwargs:
        print("키워드 인자들 !:")
        
        for key, value in kwargs.items():
            print(f"Key : {key} , Value : {value} ")

myFunction_kwargs(name="Jayce", age=100, country="korea")

print("#----------------------------------------------------------------#")

# 여러 인자가 같이 있는 경우 다음과 같이 순서를 지켜줘야함
# 일반 위치 인자 -> *args (임의 위치 인자) -> (일반 키워드 인자 또는 키워드 전용 인자) -> **kwargs (임의 키워드 인자)
def myFunction_combined(arg1, arg2, *args, arg3 = "defaultValue", **kwargs):
    print(arg1)
    print(arg2)
    print(arg3)
    
    for i, v in enumerate(args):
        print(f"i {i}, v {v}")
        
    for k, v in kwargs.items():
        print(f"key : {k}, value : {v}")

myTuple = (9,8,7)
myFunction_combined("첫번째인자", 999, 1, "호호", myTuple, arg3="NewValue!", name="jayce", age=30)