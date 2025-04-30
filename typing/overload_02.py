from typing import overload

# @typing.overload 같은 경우도 타입 힌트 시스템의 일부이며 
# 하나의 함수가 입력(매개변수) 의 타입에 따라 완전히 다른 타입의
# 결과를 반환하거나 , 여러 종류의 매개변수 조합을 받을 
# 수 있을때 , 타입 검사도구에게 "이 함수는 이렇게도 쓰이고,
# 저렇게도 쓰여" 라고 명확히 알려주고 싶을때 사용 

# overload 데코레이터를 사용해서 오버로드 함수임을 명시
# 오버로드 함수임을 명시하고 나면 본문은
# ... 을 적어 실제 구현부는 다른 곳(보통 바로 밑) 에
# 있음을 명시하는 것을 권장 

# 해당 함수가 오버로드 함수임을 명시함 
# 실제 구현부는 별도로 있고
# 이 경우에는 process 함수의 파라미터가 string 이며
# 리턴값이 string 인 시그니처를 명시하는 것 
@overload
def process(data: str) -> str:
    ...

# 마찬가지로 이 경우는 파라미터 타입이 int 고 리턴 값이
# int 인 시그니처 
@overload
def process(data :int) -> int:
    ...
    
@overload
def process(data: None) -> str:
    ...

def process(data: str | int | None) -> str | int:
    result: str | int

    if isinstance(data, str) or isinstance(data, int):
        result = data * 2
    elif data is None:
        # 파라미터가 None 이면 아래 문자열로
        # 처리할게 없음을 알리고 이는
        # 반환 타입힌트 (str | int) 에도
        # 부합하는 처리임을 참고 . 
        result = "처리할 게 없음"
    else:
        result = f"다음 타입 {type(data)} 은 잘못 되었음"
        
    print(result)
    
    return result

# 데이터 타입이 string 
process("제이스")
process(10)
process(None)