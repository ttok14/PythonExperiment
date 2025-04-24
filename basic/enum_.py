
from enum import Enum, auto, IntEnum, Flag
import enum

# 파이썬에서는 Enum 사용을 위해선
# Enum 클래스를 상속받음
class Color(Enum):
    # auto() 는 직전 요소 숫자값 +1 을 더한 값으로 리턴
    # 여기선 직전 요소가 없으니 , 1 로 초기화됨
    RED = auto() # 1
    GREEN = auto() # 2 
    # 수동 설정
    BLUE = 10 # 10 
    # 직전 요소인 BLUE 의 값 10 .  
    # 즉 10 + 1 = 11 => 즉 11 이 auto() 로 설정됨
    BROWN = auto() # 11
    # 문자열 가능 
    PINK = "PINK"
    # 직전 요소가 숫자가 아닌
    # 문자열이기 때문에 auto() 카운팅에서 무시
    # 즉 숫자값인 BROWN 의 영향을 받아 
    # PURPLE 은 12
    PURPLE = auto() # 12 

# 조회 
print(Color.RED)
print(Color.BROWN.name)
print(Color.BLUE.value)
print(Color.BROWN.value)
print(Color.PINK.value)

for c in Color:
    print(f"{c.name} = {c.value}")
    
# 정수항 비교가 가능하게 하기 위해서는
# enum.IntEnum 활용 가능 
class ErrorCode(IntEnum):
    SUCCESS = 0
    NETWORK_ERROR = 404

# if ErrorCode.NETWORK_ERROR == 404:
   
#------------------------------------------#
# 비트 플래그 방식으로도 사용이 가능
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    
myPermission = Permission.READ | Permission.WRITE
print(f"My Permission : {myPermission}")

if Permission.READ in myPermission:
    print("user has the read permission")
else:
    print("user does not have the read permission")

#-------------------------------------------#