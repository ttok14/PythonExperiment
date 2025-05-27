
""" 
- AI 의 핵심 설명 

self.age = age (예: p.age = 30) 실행 시 내부 동작:

파이썬은 p.age = 30과 같은 속성 할당 구문을 만나면, 가장 먼저 **p의 클래스(Person)**를 확인합니다.
Person 클래스에 age라는 이름의 속성이 있는지 찾습니다.
찾았습니다! Person.age는 Descriptor의 인스턴스입니다.
이제 파이썬은 이 Person.age (즉, Descriptor 인스턴스)가 데이터 디스크립터인지 확인합니다. 
데이터 디스크립터란 __set__ 메서드나 __delete__ 메서드 중 하나 이상을 가지고 있는 디스크립터를 말합니다.
사용자님의 Descriptor 클래스는 __set__ 메서드를 가지고 있으므로, Person.age는 데이터 디스크립터입니다.
매우 중요한 규칙: 할당 대상 객체의 클래스에 있는 속성이 
!!!!
데이터 디스크립터일 경우, 이 디스크립터의 
__set__ 메서드가 일반적인 인스턴스 딕셔너리(p.__dict__)에 값을 직접 할당하는 것보다 우선권을 가집니다.
    => 바이트코드 disassemble 하면 보일거같은데 (?)
!!!!
따라서, p.age = 30은 p.__dict__['age'] = 30으로 처리되는 대신, Person.age 디스크립터의 __set__ 메서드를 호출합니다.
호출되는 형태는 다음과 같습니다: Descriptor.__set__(Person.age, p, 30) 여기서 각 인자는 다음과 같습니다:
첫 번째 인자 (self에 해당): Person.age (즉, Descriptor 클래스의 인스턴스 자체)
두 번째 인자 (instance에 해당): p (즉, Person 클래스의 인스턴스)
세 번째 인자 (value에 해당): 30 (할당하려는 값)
Descriptor의 __set__ 메서드 내부에서는 setattr(instance, self._private_name, value)가 실행되므로,
결국 setattr(p, "_age", 30)이 호출되어 p.__dict__['_age'] = 30와 같이 실제 데이터는 _age라는 
이름으로 인스턴스 p의 __dict__에 저장됩니다.
self.height = height (예: p.height = 180)도 동일한 원리로 Person.height 디스크립터의 __set__ 
메서드를 호출하여 p.__dict__['_height'] = 180이 됩니다.
"""


# Descriptor 클래스 , 조건은 
# __get__, __set__, __delete__ 메서드들
# 중 하나 이상을 구현해야함 
class Descriptor:
    
    # __set_name__ 메서드는
    # Descriptor 클래스가 소유자 클래스에
    # 속성으로 설정될 때 호출됨
    # owner 에는 소유자 클래스가 들어오고
    # public_name 에는 소유자 클래스에서 
    # 선언된 Descriptor 속성의 이름이 들어옴 (변수명)
    
    def __set_name__(self, owner, public_name):
        self.public_name = public_name
        
        # 언더스코어를 prefix 로 둔 
        # private_name 이란 속성 이름으로
        # 실제 데이터를 인스턴스에 저장하기 
        # 위한 내부 속성 이름을 만들기 위함
        self._private_name = f"_{public_name}"
        
    def __get__(self, instance, owner):
        # instance 에는 Descriptor 를 소유한
        # 클래스의 실제 인스턴스가 들어옴 
        # 인스턴스가 None 이란 것은
        # 소유자 클래스에 직접 접근했다는 의미
        if instance is None:
            return self
        
        # getattr 함수로 해당 인스턴스의 
        # _priavte_name 속성 값을 가져와서 리턴 
        return getattr(instance, self._private_name, None)
    
    # setattr 함수로 인스턴스의 속성에 값을 설정 
    def __set__(self, instance, value):
        setattr(instance, self._private_name, value)
    
    # delattr 함수로 인스턴스의 속성 삭제 
    def __delete__(self, instance):
        if hasattr(instance, self._private_name):
            delattr(instance, self._private_name)

class Person: 
    # 마치 static 변수처럼 
    # 클래스 속성으로서 메모리에 
    # 하나만 존재함 
    age = Descriptor()
    height = Descriptor()
    
    def __init__(self, age, height):
        self.age = age
        self.height = height

p = Person(age = 30, height = 180)

# get
print(p.age)

# set 
p.age = 35

# delete
del p.age

# set
p.height = 175

# get
print(p.height)