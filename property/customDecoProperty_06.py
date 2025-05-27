
from typing import Callable, Any

# @customDecoProperty 데코레이터를 사용해서
# @property 와 유사한 기능을 하는 데코레이터 커스텀 구현 
class customDecoProperty:
    # 생성자로 get, set, delete 를 받는데
    # 중요한 것은 첫 번째 인자는 fget 인점임 
    # 이 부분이 중요한 이유는 @customDecoProperty 라고
    # 정의할 때 아래 __init__ 메서드가 호출되면서
    # fget 인자에 해당하는 메서드가 자동으로 넘어오기 때문임
    # 첫 번째 위치에 있으므로 이 @customDecoProeprty 데코를
    # get 메서드에 적용해야함 
    def __init__(self,
        fget: Callable[[Any],Any] | None = None,
        fset: Callable[[Any, Any], None] | None = None,
        fdel: Callable[[Any], None] | None = None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
    
    # getter 는 @customDecoProperty 데코레이터를 
    # 생성하는 순간 이미 내부의 _fget 속성에 연결됐으므로
    # setter 는 아래 함수를 데코레이터로 사용해서
    # _fset 속성에 연결 
    def setter(self, fset: Callable[[Any, Any], None]):
        self._fset = fset
        
        # 꼭 self 를 리턴해서 
        # 메서드 체이닝이 가능케함 
        return self
    
    # setter 와 마찬가지로 deleter 도 연결 
    def deleter(self, fdel: Callable[[Any], None]):
        self._fdel = fdel
        
        # 꼭 self 를 리턴해서
        # 메서드 체이닝이 가능케함
        return self
    
    # 실제로 디스크립터 메서드들 적용 
    def __get__(self, instance, owner):
        return self._fget(instance)
    
    def __set__(self, instance, value):
        self._fset(instance, value)
    
    def __delete__(self, instance):
        self._fdel(instance)
    
class Person:
    def __init__(self, age):
        self._age = age
    
    # @customDecoProperty 데코레이터를 사용해서
    # 프로퍼티를 정의함 . 
    # 이때 내부적으로 일어나는 일은 
    # 아래 age 함수가 customDecoProperty 의 
    # 인스턴스를 가리키게 되고 내부의
    # get 메서드에 연결이 됨
    # 즉, age = customDecoProperty(fget=age)
    # 가 되는 것임. 내부에 age 함수가 넘어가서 fget 에 연결되고
    # age 는 customDecoProperty 의 인스턴스를 가리키게 되는것 
    @customDecoProperty
    def age(self):
        return self._age
    
    # age 는 이제 customDecoProperty 의 인스턴스임
    # 그렇기 때문에 setter 함수를 데코레이터로 이용해서
    # set 을 위한 age 함수를 연결 
    # setter 의 반환값은 self 이므로 
    # age = age.setter(age) 와 같음 
    # 여기서 좌항의 age 는 setter 에서 반환된
    # customDecoProperty 의 인스턴스를 가리키게 됨
    # 즉 줄곧 같은 디스크립터의 인스턴스임
    # 가운데 age.setter 에서 age 는 
    # 위에 get 에서 새로 정의된 age 임 . 즉 저것도
    # customDecoProperty 의 인스턴스임
    # setter(age) 여기서 인자 age 는 
    # 아래 정의된 실제로 setter 역할을 하는
    # age 함수임 
    
    # 참고로 get set deleter 메서드들의 이름은
    # 반드시 동일할 필요는 없지만 전부 
    # 같은 customDecoProperty 의 인스턴스를 가리키므로
    # 이름을 다르게하면 실제로 똑같은 
    # customDecoProperty 의 인스턴스를 가리키는
    # 이름만 다른 디스크립터가 됨 
    # 즉 관례적으로 같은 이름으로 사용함 
    # 서로 다른 이름의 같은 디스크립터를 가리키는 것을 확인하려면
    # 함수 이름만 다르게 해서 클래스_이름.__dict__ 를 출력하면
    # 확인 가능. (같은 주소의 customDecoProperty 객체를
    # 가리키는걸 볼 수있음)
    @age.setter
    def age(self, value):
        self._age = value
    
    # deleter 도 setter 와 마찬가지 맥락
    @age.deleter
    def age(self):
        del self._age

p = Person(30)
print(p.age)
p.age = 35
print(p.age)
del p.age

# 다음 코드로 실제로 Person 클래스안에
# customDecoProperty 의 인스턴스를 볼 수 있음
# 또한 , setter 와 deleter 의 메서드 이름을
# 변경하면 별도의 이름으로 동일한 객체의
# customDecoProperty 인스턴스를
# 가리키고 있는것 또한 볼 수 있음을 참고 . 
# print(Person.__dict__)