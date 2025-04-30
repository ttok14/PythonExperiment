
# Descriptor
# 디스크립터는 클래스 함수중 
# 특별한 함수인 __get__ , __set__ , __delete__ 중
# 하나 이상을 구현한 클래스를 디스크립터라고함 . 

# 디스크립터 클래스는 해당 객체를 , 또 다른 객체의
# 속성에 대해 get / set / delete 을 대신하여 
# 처리할 수 있는 로직을 실행할 수 있는 클래스임 .

# 또한 디스크립터의 함수에서 자신을 사용하는
# 타 객체 인스턴스에 대한 접근이 중요하기에
# 파라미터로 자신을 사용하는 타 인스턴스 문맥에
# 맞게 주로 들어온다는 것을 염두하면 이해쉽게감.

class MyDescriptor:
    # type 을 받아서 현재 descriptor 가 
    # 취급할 데이터의 타입을 보관 
    # name 은 해당 데이터의 변수명을 위해 멤버로 선언 
    def __init__(self, type):
        self.type = type
        self.name = None

    # __set_name__ 은 디스크립터 인스턴스가 소유자
    # 클래스에(owner class) 할당될때 어떤 이름의 
    # 변수로 할당되었는지를 디스크립터 자신에게 알려주기
    # 위해 자동으로 호출되는 특수 메서드 . 
    
    # 즉 이 경우에 , DescriptorOwner 클래스에서
    # value01 을 할당할때 해당 디스크립터 인스턴스로
    # 한번 호출되고 (이때 name 이 value01 으로)
    # value02 을 할당할때 마찬가지로 또 호출됨.
    # (이때는 name 이 value02)
    def __set_name__(self, owner, name):
        self.name = name
    
    # 디스크립터의 값을 읽어들이려 할때
    # 자동으로 이 함수가 호출되며
    # instance 에는 해당 디스크립터를 소유하는 
    # 클래스의 인스턴스가 넘어오고 owner 에는 
    # 디스크립터를 소유하고 있는 클래스 타입이 들어온다
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # __dict__ 는 모든 클래스에 내부적으로
        # 존재하는 딕셔너리.
        # 이 딕셔너리에는 해당 클래스의 모든 속성들이
        # 들어가게되는데 이때 
        #   - key : 변수명 
        #   - value : 값 
        # 이 들어가게 된다. (함수또한)
        # 이로인해 클래스의 속성에 접근하는데
        # 제너릭하게 접근할 수 있는 특징이 있다 
        return instance.__dict__.get(self.name)

    # 소유자 클래스의 인스턴스를 통해 속성에 값을
    # 할당하려고 할 때 instance 에는 해당 디스크립터 
    # 변수를 소유하는 클래스의 인스턴스가 들어온다.
    
    # 참고로 , 클래스를 통해 바로 접근하는 경우는 
    # 이 함수가 호출되지 않음
    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"다음 타입만 가능해요. {self.type.__name__}, {type(value).__name__} 는 안돼요~")
        
        instance.__dict__[self.name] = value
        
class DescriptorOwner:
    value01 = MyDescriptor(str)
    value02 = MyDescriptor(int)
    
    def __init__(self):
        # 1. 인스턴스(self)의 'value01' 속성에 값을 할당하려고 시도합니다.
        # 2. 파이썬은 먼저 이 인스턴스의 클래스(DescriptorOwner)에 'value01'이라는 이름의
        #    속성이 있는지 확인합니다.
        # 3. 확인 결과, MyDescriptor 인스턴스가 클래스 속성으로 존재하며, 이 디스크립터는
        #    __set__ 메서드(데이터 디스크립터)를 가지고 있습니다.
        # 4. 따라서, 파이썬은 인스턴스(self)의 __dict__에 직접 값을 할당하는 대신,
        #    클래스에 정의된 MyDescriptor 인스턴스의 __set__ 메서드를 호출합니다.
        # 5. 내부적으로 다음과 같은 호출이 일어납니다:
        #    DescriptorOwner.value01.__set__(self, "I am Jayce")
        #    - 첫 번째 인자(디스크립터의 self): 클래스에 정의된 MyDescriptor 인스턴스
        #    - 두 번째 인자(instance): 값을 할당받는 인스턴스 (여기서는 __init__의 self)
        #    - 세 번째 인자(value): 할당되는 값 ("I am Jayce")
        # 6. MyDescriptor의 __set__ 메서드는 전달받은 값("I am Jayce")의 타입을 확인하고,
        #    문제가 없으면 instance 인자(여기서는 __init__의 self)의 __dict__에
        #    'value01'이라는 키(self.name)로 값을 저장합니다. (instance.__dict__['value01'] = "I am Jayce")
        self.value01 = "I am Jayce"
        self.value02 = 1000

inst = DescriptorOwner()

# 아래같이 작성하게 된다면 
# 단순히 DescriptorOwner 의 value01 을 100 으로 덮어씀 
#       -> 더이상 디스크립터가 아니게 된다. 
# DescriptorOwner.value01 = 100

# 클래스로 직접 접근 
print(DescriptorOwner.value01)
# 해당 디스크립터를 소유하는 별도 인스턴스로 접근 
print(inst.value01)
print(inst.value02)
