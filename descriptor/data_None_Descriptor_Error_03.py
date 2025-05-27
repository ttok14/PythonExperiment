
"""
    *02.py 먼저 참고*

    - 이 예제는 데이터 디스크립터일때 초기화시 __set__ 이 호출되는
       예시를 보여줌. 
    
    - 데이터 디스크립터라면 초기화시 __set__() 가 호출된다.
    - 이 예제는 데이터 디스크립터이지만 __delet__ 만 구현하여
        __set__ 이 없는 상태에서의 초기화 동작을 했을때
        에러가 나는 예시임. 
        
    - !!! 핵심은 , Descriptor 클래스의 __delet__ 마저 없다면
        더이상 데이터 디스크립터가 아니기 때문에
        초기화시 __set__() 이 호출되지 않아 
        에러가 발생하지 않게된다. !!!!
        
    - 실행시 'AttributeError: __set__' 에러가 발생한다.
        즉 데이터 디스크립터기 때문에 __set__ 을 호출했는데
        __set__ 메서드가 없어서 발생하는 런타임 에러다 .
        
        -> __delete__ 를 없애면 Non 데이터 디스크립터가 되어
            에러가 발생하지 않게된다. 
"""
class Descriptor:
    def __get__(self, instance, owner):
        pass
    
    # 이 __delete__ 때문에 데이터 디스크립터 클래스가 된다.
    # 때문에 초기화때 __set__ 이 호출된다. 
    # 이 __delete__ 가 없으면 Non 데이터 디스크립터가 되어
    # 에러가 발생하지 않는다. 
    def __delete__(self, instance):
        pass
        
class MyClass:
    desc = Descriptor()
    
    def __init__(self):
        self.desc = "아무거나 할당해보자"

m = MyClass()