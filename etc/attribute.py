
# 파이썬에서 속성(attribute)은 객체가 가지고있는 *변수*나 *함수* 를 의미함
# ! C# 에서의 Attribute 와는 다른 개념임 ! 

class parentClass:
    def parentFunction():
        pass

class myClass(parentClass):
    def __init__(self):
        self.member01 = 10
        self.member02 = 30
        
    def function01(self):
        pass
    
c = myClass()

# 있는 속성 
hasMember01 = hasattr(c, "member01")
# 있는 속성 
hasFunction01 = hasattr(c, "function01")
# 없는 속성
hasABCD = hasattr(c, "ABCD")

# 있는 속성 (부모 클래스의 함수)
hasParentFunction = hasattr(c, "parentFunction")

print(f"hasMember01 : {hasMember01}")
print(f"hasFunction01 : {hasFunction01}")
print(f"hasABCD : {hasABCD}")
print(f"hasParentFunction : {hasParentFunction}")