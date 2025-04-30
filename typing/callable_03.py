
# Callable : 호출 가능한 타입 (e.g 함수)
# Any : 타입에 제한이 없음을 의미 
from typing import (
    Callable, 
    Any, 
)

def noParam():
    print("noParam")

# 'c 는 호출 가능한 객체를 보관하는 변수며
# 여기서는 인자가 없고 반환 값이 없거나 None 을 명시적으로
# 반환하는 호출 객체를 의미' (반환안하면 암시적으로 
# None 이 리턴됨)
c: Callable[[], None] = noParam
c()

def oneParam_returnNone(number: int):
    print(number)

# 'c 는 *인자가 int 하나이며 리턴 타입이 None인* 
# 호출 가능한 객체를 보관하는 변수다'
c: Callable[[int], None] = oneParam_returnNone
c(10)

def twoParams_returnStr(number: int, name: str) -> str:
    print(f"{number} , {name}")
    return "twoParams_returnStr"

c: Callable[[int, str], str] = twoParams_returnStr
c(11, "HIHI")

def manyParams_return_any(n1,n2,str1,str2,n3,str3) -> Any:
    if n1 == 0:
        print("1")
        return 1
    elif n2 == 1:
        print("2")
        return "아무거나~~"
    else:
        print("3")
        return 0.55

# 'c는 인자의 타입 / 개수 제한이 없으며 리턴
# 리턴 타입도 제한이 없다 (Any) '
c: Callable[..., Any] = manyParams_return_any
c(1,2,3,4,5,6)