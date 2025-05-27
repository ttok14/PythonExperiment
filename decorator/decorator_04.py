
# 함수의 데코레이터로 사용할 클래스
class DecoClass:
    # 원본 함수를 인자로 받아 보관
    def __init__(self, func):
        self._func = func
    
    # 클래스의 인스턴스를 Callable 로 
    # 만들어주는 메서드. 즉
    # 클래스 인스턴스 자체를 함수처럼 
    # 호출하면 실행됨
    def __call__(self, *args, **kwds):
        print(f"__call__ | {args}{kwds}")
        self._func()
        
    def doWork(self, func):
        def wrapper():
            print("Wrapper executed!")
            func()
            
        return wrapper

# 데코레이터에 클래스를 선언
# 이렇게 되면 function 에 
# DecoClass 의 인스턴스가 할당된다
# 즉, function = DecoClass(function) 과 같음 
# 신박한 문법이지만 .. 맞음 
@DecoClass
def function01():
    print("Function01 executed!")

# 위에서 function 은 DecoClass 의
# 인스턴스가 되었음. 이제 .doWork 를 하면
# function02 = DecoClass.doWork(function02) 와 같아짐 
@function01.doWork
def function02():
    print("Function02 executed!")

# function01 은 현재 
# DecoClass 의 인스턴스이기 때문에
# 호출하면 DecoClass 의 __call__ 메서드가 실행됨
function01(1,2,3, {"key01":"jayce", "key02":"elise"})    

# function02 는 DecoClass.doWork 에서 
# 반환했던 내부 wrapper 가 실행됨 
function02()