
# 커스텀 디스크립터 프로퍼티 클래스
class CustomProperty:
    def __init__(self, fget= None, fset = None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.fget(instance)
    
    def __set__(self, instance, value):
        self.fset(instance, value)

class Person:
    def __init__(self):
        self._age = 0
    
    # 실제로 외부에서 호출될 getter 메서드
    def get_age(self):
        return self._age

    # 실제로 외부에서 호출될 setter 메서드
    def set_age(self, value):
        self._age = value

    age = CustomProperty(get_age, set_age)

p = Person()
print(p.age)

p.age = 400
print(p.age)