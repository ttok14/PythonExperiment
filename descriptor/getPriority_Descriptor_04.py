
"""
    *이전 예제 먼저 참고*
    
    클래스의 속성에 접근(get) 할때 어떤 우선 순위로
    속성의 접근이 이루어지는지에 대한 예시.
    
    순서는 다음과 같음 
    
    1. 해당 속성이 데이터 디스크립터인경우 (__set__ 또는 __delete__ 구현)
        => __get__ 이 호출된다. (__get__ 이 없다면 자기 자신의 객체)
    2. __dict__ 에 저장된 값을 반환
    3. Non 데이터 디스크립터인 경우 __get__ 이 호출
"""

# 데이터 디스크립터 
class Descriptor:
    def __init__(self, name):
        self.private = f"managed by {name}"
        
    def __get__(self, obj, typ=None):
        return self.private      # 데이터 디스크립터
    
    def __set__(self, obj, value):
        self.private = value     # __set__ 존재 → 데이터 디스크립터

# __get__ 만 구현된 Non 데이터 디스크립터
class NonDataDescriptor:
    def __get__(self, obj, typ=None):
        return "non-data value"  # __get__만 → 비-데이터 디스크립터

class Demo:
    data = Descriptor("data")
    nondata = NonDataDescriptor()
        
d = Demo()

# __dict__ 에 직접 접근해서 값 초기화 
d.__dict__["data"] = "shadow?"
d.__dict__["nondata"] = "shadow!"

# 속성 조회 시도

# data 는 데이터 디스크립터이므로 
# __dict__["data"] 에 shadow? 가 있지만
# __get__ 이 호출된다. 
print(d.data)

# nondata 는 디스크립터이기는 하지만
# Non 데이터 디스크립터이므로
# 속성값 조회시 __dict__ 가 우선 순위가 더 높다
# 즉 위에 shadow! 로 넣은 값이 출력된다 . 
print(d.nondata)

# 정리하자면 

# 인스턴스 속성에 접근할때

# 1. 데이터 디스크립터가 있다면 __get__ 이 호출된다.
# 2. __dict__ 에 저장된 값을 반환 
# 3. Non 데이터 디스크립터가 있다면 __get__ 호출 