
"""
데이터 디스크립터와 Non 데이터 디스크립터의 
 구분을 명확히 보여주는 예시

 일단 간단히 정리하자면

 디스크립터 클래스 : __get__, __set__, __delete__ 
 메서드중 하나 이상을 구현 
    -> 데이터 디스크립터 : __set__ , __delete__ 메서드중
        하나 이상을 구현한 디스크립터 
    -> Non 데이터 디스크립터 : __set__ , __delete__ 메서드
        둘 다 구현하지 않은 디스크립터
        즉 , __get__ 메서드만 구현한 디스크립터 
        
이 구분이 왜 중요하냐면, 클래스 속성에 접근할때 
데이터 디스크립터가 실제 일반적인 클래스의 인스턴스 속성값이
저장되는 __dict__ 보다 높은 우선순위를 갖기 때문임.

무슨 의미냐면 , self.a = 10 이라고 했을때
a 가 만약에 데이터 디스크립터라면 __set__ 가 호출이 되고
데이터 디스크립터가 아니라면 a 가 __dict__ 에 저장됨.

이를 증명하는 예제 
"""

class NonDataDescriptor:
    def __get__(self, instance, owner):
        print("NoneDataDescriptor GET")
        return "__get__"

class Descriptor:
    def __get__(self, instance, owner):
        print("Descriptor GET")
        return "__get__"
    
    def __set__(self, instance, value):
      print("Descriptor SET")
        
class MyClass:
    non = NonDataDescriptor()
    non_assignedNew = NonDataDescriptor()
    desc = Descriptor()
    
    def __init__(self):
        # self.속성 에 접근해 초기화를 시도한다
        # 이때 속성이 데이터 디스크립터라면은 
        # __set__ 메서드가 호출이 된다
        
        # non 은 Non 데이터 디스크립터이므로
        # (__set__ 또는 __delete__ 가 없기때문에)
        # __set__ 가 호출되지 않는다
        
        # 즉 non_assignedNew 는 
        # Non 데이터 디스크립터에 할당 시도를 하게 되면
        # __set__ 이 호출되지 않으므로 
        # self.non_assignedNew = 1 은
        # self.__dict__ 에 저장이 된다.
        # 이 말은, 1 이란 정수값이 
        # non_assignedNew 에 저장된다라는 의미
        
        # 그러니까 그냥 non_assignedNew 는
        # 정수임.
        self.non_assignedNew = 1
        
        # desc 는 데이터 디스크립터이므로 
        # __set__ 메서드가 호출이 된다.
        
        # 데이터 디스크립터이므로 __set__ 이 호출됐다.
        # 근데 __set__ 은 없고 __delete__ 만 있어도
        # 데이터 디스크립터인데 이 경우는 어떻게 되냐? 
        # 
        self.desc = 1

m = MyClass()

print(f"Non 데이터 디스크립터 (할당 시도 X), __get__ 호출 : {m.non} ({type(m.non)})")
print(f"그냥 정수 1 인 int 속성에 접근 : {m.non_assignedNew} ({type(m.non_assignedNew)})")
print(f"데이터 디스크립터, __get__ 호출 : {m.desc} ({type(m.desc)})")
