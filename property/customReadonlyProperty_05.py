
# 읽기 전용 프로퍼티 디스크립터 클래스
class CustomReadonlyProperty:
    
    # 생성자에서 실제 get 시 호출할 메서드를 받음 
    def __init__(self, fget):
        self.fget = fget
    
    # 현 디스크립터를 생성한 속성의 이름을 저장 
    def __set_name__(self, owner, name):
        self.prop_name = name
    
    # 디스크립터의 __get__
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # 실제로 반환할 값은 
        # fget 으로부터 즉 외부에서 가져옴 
        return self.fget(instance)
    
    # read-Only 속성이므로 __set__ 는 
    # 에러로 간주
    def __set__(self, instance, value):
        raise AttributeError(f"This is read-only property | {self.prop_name}")

class Person:    
    def __init__(self, age):
        self._age = age
    
    # 디스크립터로 부터 호출될 함수 
    def get_age(self):
        return self._age
    
    # CustomReadonlyProperty 디스크립터를 사용하여
    # age 속성을 읽기 전용으로 정의
    age = CustomReadonlyProperty(get_age)
    
p = Person(30)
print(p.age)

try:
    # 에러 발생 (읽기 전용인데 쓰기 시도)
    p.age = 50
except AttributeError as e:
    print(e)

