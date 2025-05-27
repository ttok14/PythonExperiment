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
        self.name = None # 속성 이름은 __set_name__을 통해 설정됨

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
            # 클래스 자체를 통해 접근하는 경우 디스크립터 자신을 반환
            return self

        # getattr을 사용하여 인스턴스에서 속성 값을 가져옴.
        # 속성이 존재하지 않으면 None을 반환하도록 default 값을 설정.
        return getattr(instance, self.name, None)

    # 소유자 클래스의 인스턴스를 통해 속성에 값을
    # 할당하려고 할 때 instance 에는 해당 디스크립터
    # 변수를 소유하는 클래스의 인스턴스가 들어온다.

    # 참고로 , 클래스를 통해 바로 접근하는 경우는
    # 이 함수가 호출되지 않음
    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"다음 타입만 가능해요. {self.type.__name__}, {type(value).__name__} 는 안돼요~")

        # setattr을 사용하여 인스턴스에 속성 값을 할당.
        setattr(instance, self.name, value)

    # 소유자 클래스의 인스턴스를 통해 속성을 삭제하려고 할 때 호출됩니다.
    def __delete__(self, instance):
        print(f"'{self.name}' 속성을 인스턴스에서 삭제합니다.")
        # delattr을 사용하여 인스턴스에서 속성을 삭제.
        delattr(instance, self.name)

class DescriptorOwner:
    value01 = MyDescriptor(str)
    value02 = MyDescriptor(int)

    def __init__(self):
        # 1. 인스턴스(self)의 'value01' 속성에 값을 할당하려고 시도합니다.
        # 2. 파이썬은 먼저 이 인스턴스의 클래스(DescriptorOwner)에 'value01'이라는 이름의
        #    속성이 있는지 확인합니다.
        # 3. 확인 결과, MyDescriptor 인스턴스가 클래스 속성으로 존재하며, 이 디스크립터는
        #    __set__ 메서드(데이터 디스크립터)를 가지고 있습니다.
        # 4. 따라서, 파이썬은 인스턴스에 직접 값을 할당하는 대신,
        #    클래스에 정의된 MyDescriptor 인스턴스의 __set__ 메서드를 호출합니다.
        # 5. 내부적으로 다음과 같은 호출이 일어납니다:
        #    DescriptorOwner.value01.__set__(self, "I am Jayce")
        #    - 첫 번째 인자(디스크립터의 self): 클래스에 정의된 MyDescriptor 인스턴스
        #    - 두 번째 인자(instance): 값을 할당받는 인스턴스 (여기서는 __init__의 self)
        #    - 세 번째 인자(value): 할당되는 값 ("I am Jayce")
        # 6. MyDescriptor의 __set__ 메서드는 전달받은 값("I am Jayce")의 타입을 확인하고,
        #    문제가 없으면 instance 인자(여기서는 __init__의 self)에
        #    self.name (여기서는 'value01')으로 값을 저장합니다. (setattr(self, 'value01', "I am Jayce")가 호출됨)
        self.value01 = "I am Jayce"
        self.value02 = 1000

inst = DescriptorOwner()

# 클래스로 직접 접근 (디스크립터 객체 반환)
print(f"클래스 접근 (DescriptorOwner.value01): {DescriptorOwner.value01}")

# 인스턴스를 통해 디스크립터의 __get__ 호출
print(f"인스턴스 접근 (inst.value01): {inst.value01}")
print(f"인스턴스 접근 (inst.value02): {inst.value02}")

# 값 변경 시도 (디스크립터의 __set__ 호출)
inst.value01 = "Hello Python"
print(f"변경된 inst.value01: {inst.value01}")

try:
    inst.value02 = "Not an int" # 타입이 맞지 않아 TypeError 발생
except TypeError as e:
    print(f"에러 발생: {e}")

print("\n--- delattr 테스트 ---")
print(f"삭제 전 inst.value01: {inst.value01}")
# 속성 삭제 (디스크립터의 __delete__ 호출)
del inst.value01
# 삭제 후 __get__은 None을 반환 (getattr의 default 값)
print(f"삭제 후 inst.value01: {inst.value01}")

# 삭제된 속성에 다시 값 할당 (디스크립터의 __set__ 호출)
inst.value01 = "다시 할당된 Jayce"
print(f"재할당 후 inst.value01: {inst.value01}")

# 존재하지 않는 속성을 가져오려고 시도 (getattr의 default 값인 None 반환)
# print(f"inst.value02 삭제 전: {inst.value02}")
# del inst.value02
# print(f"inst.value02 삭제 후: {inst.value02}") # None
# inst.value02 = 2000
# print(f"inst.value02 재할당 후: {inst.value02}")