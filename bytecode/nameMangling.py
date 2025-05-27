class MyClass:
    def __init__(self):
        self.__super_secret = 1

    def __do_something(self):
        print("비밀 작업중")
        return "비밀 작업 성공"

obj = MyClass()

# 출력 결과에서 '_MyClass__super_secret' 와 '_MyClass__do_something' 확인
# 이는 이름 맹글링(name mangling)으로 인해 클래스 외부에서 접근할 수 없도록 처리됨
# 하지만 파이썬에서 이름 맹글링은 
# *** 단순히 이름을 변경시켜서 접근을 어렵게 만드는것 뿐 *** 
# 완전히 숨기지는 않음 이는 파이썬의 철학중 하나인 "We are all consenting adults here" 에 기반함
print(dir(obj))

# 이름 맹글링된 속성에 여전히 접근이 가능함
print(obj._MyClass__super_secret)
print(obj._MyClass__do_something())