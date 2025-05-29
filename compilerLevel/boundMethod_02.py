

"""
파이썬의 함수 호출 원리 (디스크립터의 맥락에서)
  1. 일반 함수 (클래스 인스턴스에 속해있지 않은 함수)
    - type() 찍어보면 function 임 
    - 참고로 function 에는 __get__ 이 있어 디스크립터지만
        클래스 밖에 있기 때문에 디스크립터로 동작하지 않음.
        즉 바로 해당 function 객체의 __call__ 이 호출되는 원리로 함수 호출
  2. 클래스 인스턴스 함수 호출 (클래스 함수이고 인스턴스로 접근해서 호출)
    - type() 찍어보면 method 임, 여기서 method 는 바운드 메소드임 (bound method)
        즉 클래스 인스턴스에 bound (묶인) 된 메소드라는 의미.
    - 인스턴스의 함수에 접근하는 순간 , 예를들어 a.B() 라 하면
        클래스내에 있는 함수는 디스크립터 프로토콜을 충족해서 
        __get__ 이 호출됨. __get__ 이 호출될때 여기에 내부적으로 
        실제 클래스의 인스턴스와 실제 호출할 함수 (ClassName.함수 로 접근가능) 
        를 같이 넘겨서 바운드 메소드를 만들어냄 . 
    - 만들어진 바운드 메소드는 호출하는 객체도 알고 함수도 알기에 () 로 호출시 
        내부적으로 알아서 self 에 해당하는 부분에 객체 인스턴스를 넘겨줄 수 가 있음. 
"""

# 아래 예제는 실제로 클래스 인스턴스의 함수를 호출하는거를 
# 흉내내는 코드 

# 바운드 메소드 역할할 클래스 
class BoundMethodEmulator:
    # 바운드 메소드는 실제 실행해야할 함수와 
    # 자신이 바운드된(묶인) 객체 자체를 가짐
    def __init__(self, ori_func, instance):
        self._ori_func = ori_func
        self._instance = instance
        
    # 함수 호출 부분. 실제로는 그냥 클래스 함수를 호출하는 것과 동일
    def __call__(self, *args, **kwds):
        # ! self 를 직접 넣어줌. 여기서 _ori_func 는 
        # 클래스 인스턴스에 바운드된 메소드가 아닌 순수 function 인 상태 !
        # print(type(self._ori_func))
        self._ori_func(self._instance, *args, **kwds)

# 일반 함수 (function) 시뮬레이션용 클래스 
class FunctionEmulator:
    def __init__(self, ori_func):
        self._ori_func = ori_func
    
    # 디스크립터 프로토콜에 맞춰서 구현 
    def __get__(self, instance, owner):
        # 속성처럼 접근하면 실제 객체 인스턴스에 바운드시킨 
        # 바운드 메소드를 만들어 리턴함 
        return BoundMethodEmulator(self._ori_func, instance)

# 클래스 시뮬레이션용 
class ClassEmulator:
    # 실제 함수 
    def RealFunction(self, param1 = None, param2 = None):
        print("나는 이걸 호출할거야!!")
        print(f"파라미터01 : {param1}")
        print(f"파라미터02 : {param2}")
    
    # 디스크립터로 사용하기 위해 (function 은 __get__ 가지고있는 디스크립터이며
    # 클래스 내 함수로 사용될때 실제로 호출되어 실제 객체 인스턴스 바운드해서 리턴)
    desc = FunctionEmulator(RealFunction)

c = ClassEmulator()

# c.desc 은 FunctionEmulator 의 __get__ 호출로 이어지고
# 이는 __call__ 을 구현하는 BoundMethodEmulator 인스턴스의 리턴으로 이어짐
# 그래서 바로 호출이 가능 . 
c.desc("파라미터1 갑니다잉", "2 갑니다잉")