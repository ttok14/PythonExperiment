

"""
    선행 지식 - Decorator , Descriptor
"""


# 가장 기본적인 형태의 프로퍼티 사용 예제

class Person:    
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age
        
    def del_age(self):
        del self._age

    # 위에서 정의한 get/set/delete 메서드들을 
    # property 에 연결하고 나면은 
    # 접근할때 함수가 아닌 속성처럼 사용 가능 
    
    # 하지만 이 방식은 연결성이 떨어져 
    # 결과적으로 가독성이 떨어짐 
    # 게다가 이름의 반복적인 타이핑으로 
    # 코드가 길어지며 실수할 가능성도 높아짐
    # 그리고 실제 프로퍼티 인스턴스를 생성하는
    # 다음 코드도 실제 프로퍼티 함수들의 뒤에 
    # 있어야 함, 이런 제약도 가독성을 떨어뜨리는
    # 요인임 . 느낌도 안좋음 뒤에있다보니
    
    # 아무튼 프로퍼티를 이런식으로도 사용 할  있 다. 
    age = property(get_age, set_age, del_age)

p = Person(30)

# get
print(p.age)

# set
p.age = 35

# delete
del p.age

