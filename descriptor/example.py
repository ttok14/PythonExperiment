
# Descriptor 를 응용해서 만든 
# PySide6 의 시그널 이벤트 처리 방식 시뮬레이션

# 타입 힌트의 평가 시점을 뒤로 미루고 내부적으로 
# 문자열로 저장하게 만드는 미래 호환성 기능
from __future__ import annotations

# overload : overload 데코레이터를 사용하기 위함
# Callable : 타입힌트로 호출가능한 객체를 명시하기 위함
# Dict : 딕셔너리 dict 를 선언할때 [Key,Value] 타입을 
#   명확히 명시해주기 위해서 사용 
# Any : 어떤 타입이던 가능하다라는 타입 힌트 
from typing import overload, Callable, Dict, Any

# PySide 시그널 자체 또는 시그널 디스크립터를 의미하는 클래스
# (이벤트 발생했음을 알리는)
class Signal:
    def __init__(self):
        # name 에 자신이 선언된 변수명을
        # 보관하기 위해 추가
        self.name = None
    
    # 이 함수는 특수 함수로, 디스크립터가 할당될때
    # 자신이 선언된 변수명을 name 파라미터로 
    # 넘어옴. 이를 내부에 저장 
    def __set_name__(self, owner, name):
        self.name = name
    
    # 오버로드 함수로서 인자와 리턴 타입만을 명시
    # 이 오버로드는 클래스 변수가 아닌 
    # 실제 객체 인스턴스에 의해 호출될때 호출
    # (instance 가 실제 해당 디스크립터가 호출된
    # 객체의 인스턴스가 들어감)
    # + __get__ 이 있기에 디스크립터 클래스. 
    # 리턴 타입은 SignalInstance 임 . 
    @overload
    def __get__(self, instance: SimulatedQAbstractButton, owner) -> SignalInstance:
        ...

    # instance 가 None 이고 반환값이 Signal 인 
    # 조합인 경우. 디스크립터는 자기 자신을 반환 
    @overload
    def __get__(self, instance: None, owner) -> Signal:
        ...

    # 실제 __get__ 의 구현부         
    def __get__(self, instance, owner):
        # instance 가 None 인 경우는 디스크립터
        # 자기 자신을 리턴 
        if instance is None:
            return self
        
        result = None

        # instance 에 접근해서 __dict__ 즉 내부 속성(멤버 변수)
        # 등을 담아놓는 딕셔너리에 접근해서
        # _signal_instances 라는 이름의 키로 가져온다
        # 없다면 생성해서 가져온다. 사실상 멤버변수를 가져오거나
        # 생성해서 가져오는 코드임  
        signalDict:Dict[str, SignalInstance] = instance.__dict__.setdefault(f'_signal_instances', {})
        
        # 가져온 dictionary 안에 self.name 즉 
        # 디스크립터로 선언된 자신의 변수 이름
        # (__set_name__ 에서 받은) 의 키가 있는지
        # 검사한다. 있으면 그대로 가져온다 
        if self.name in signalDict:
            result = signalDict[self.name]
        # 없다면 새로 생성해서 넣어준다
        # 생성된 SignalInstance 에는 실제로 
        # 이벤트 함수들이 연결되고 호출될 수 있는 메커니즘이 있음 
        # 그렇기에 객체 인스턴스별로 이벤트 관리가 가능 ! 
        else: 
            result = SignalInstance()
            signalDict[self.name] = result
                    
        return result

# 실제 이벤트를 사용하는 객체가 자신만의 시그널
# 관리를 위해 가지고 있기 위한 객체
class SignalInstance:
    def __init__(self):
        # 현재 시그널이 발동될때 호출되는 
        # 콜백 함수 리스트. Callable 은 
        # '호출 가능한' 객체를 의미하고 
        # [... , Any] 에서 ... 는 
        # 함수 인자의 타입 제한 X / 개수 제한 X 을 의미
        # Any 는 반환 타입의 제한 없음을 의미하는 타입힌트 
        # 아무튼 리스트를 멤버변수에 할당함 
        self.callback: list[Callable[... , Any]] = []
    
    # 함수를 연결함 , 내부 callback 에 추가 
    def connect(self, func):
        if func is None:
            print("Function cannot be None!")
            return
            
        self.callback.append(func)
    
    def disconnect(self, func):
        self.callback.remove(func)
    
    # 콜백 함수 호출에 인자 제한을 두지 않았기에
    # *args 로 받음 (튜플로 들어옴)    
    def emit(self, *args):
        # 혹시나 콜백 함수 실행 중간에 원본 
        # 리스트에 변경이 가해지면 예기치 않은
        # 동작이 발생할 수 있기때문에 
        # 원본 카피해서 루프돌음 
        for t in self.callback.copy():
            t(*args)

# pyside 의 QPushButton 의 부모 클래스를 모방 
class SimulatedQAbstractButton:
    clicked = Signal()    

# QPushButton 모방
class SimulatedQPushButton(SimulatedQAbstractButton):
    def __init__(self):
        super().__init__()
        
    # 클릭을 시뮬레이션 하기 위한 함수
    def doClick(self):
        # emit 함수로 이벤트 트리깅함 
        self.clicked.emit(True)
        
btn = SimulatedQPushButton()

def onClicked(trueOrFalse):
    print("Btn Clicked!")
    print(trueOrFalse)
    
# 클릭 시뮬레이션!
# 함수 연결 
# btn.clicked.connect(lambda checked: print(f"Btn Clicked! {checked}"))
btn.clicked.connect(onClicked)
# 클릭 시뮬레이션 
btn.doClick()