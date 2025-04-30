
# 코드에 타입 힌트(Type hint) 를 추가하는 것을
# 돕기 위해서 만들어진 모듈

# 타입 힌트란 변수 , 함수의 매개변수, 반환값 등이
# 어떤 타입을 가질것으로 기대되는지 명시하는 것 
import typing 


# 인사하기 함수
def greet(
    # 이름을 파라미터로 받는데
    # 문자열로 받거나 | None 으로 받는다
    # 다만 파라미터가 명시되지 않은 경우 
    # 디폴트 값을 "친구" 로 한다 
    # (코드 모양세는 마치 None 이면 "친구" 로 넘어올것 처럼)
    # 생겨먹었지만 str | None 과 = "친구" 는 별개임.
    # str | None 은 '문자열 또는 None 타입' 을 의미
    # = "친구" 는 디폴트값 
    name: str | None = "친구", 
    age: int | None = None):
    
    who_to_greet = name if name is not None else "친구"
    msg = f"안녕, {who_to_greet}"
    
    if age is not None:
        msg += f"{age}살이구나!"
        
    print(msg)
    
greet(name="영희", age=14)
greet(name="철수")
greet(age=15)

# 둘다 명시를 안했기에 둘다 디폴트값 
greet()

# name 에 none 을 넣어줬기에
# 디폴트값 "친구" 로 들어감
greet(name=None, age=16)