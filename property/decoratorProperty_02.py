
# basicProperty.py 에서의 property 의 단점을 
# 보완하기 위한 프로퍼티 사용법 
# 여기서는 @property 데코레이터 활용

class Person:
    # 내부 멤버변수 선언 
    def __init__(self, age):
        self._age = age
    
    #-------------------------------------------#
    #--- 프로퍼티 선언 ---#
    
    # age 라는 getter 프로퍼티 정의
    @property
    def age(self):
        return self._age
    
    # age 라는 setter 프로퍼티 정의 
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age can not be nagative")
        self._age = age
    
    # age 라는 deleter 프로퍼티 정의 
    @age.deleter
    def age(self):
        del self._age
    #-------------------------------------------#

t = Person(25)

# get 
print(t.age)

# set 
t.age = 30

# delete
del t.age