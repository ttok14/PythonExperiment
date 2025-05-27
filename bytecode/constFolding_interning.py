
import dis

# 파이썬이 컴파일 시점에 계산할 수 있는 값들은
# 상수 폴딩을 통해 인터닝 처리된다.
# 상수 폴딩은 컴파일 시점에 계산된 값을
# 런타임 시점에 재사용할 수 있도록 하는 최적화 기법이다.
# 인터닝은 동일한 값에 대해 메모리상에
# 하나의 객체만 생성하여 재사용하는 기법이다.

# 6000 을 var 변수에 할당한다.
# 이때 6000 은 파이썬이 컴파일 시점에
# 계산할 수 있으므로 상수 폴딩을 이용해서
# 인터닝 처리된다.

# 즉 이 6000 은 인터닝된다.
# (이전에 인터닝된 6000 이란 값이 있다면 그것을
# 재사용한다. 그렇지 않다면 새로 할당하여 내부적으로
# 보관한다.)
var = 6000
print(id(var))
# 위 시점에서 이미 6000 이란 값은 
# 인터닝되어 메모리상에 존재한다.
# 따라서 아래의 6000 도 동일한 객체를 참조한다.
print(id(6000))
# 10 * 20 * 30 은 6000 이므로 
# 위와 동일한 객체를 참조한다. (컴파일 시점에 알수있음)
print(id(10 * 20 * 30)) 
# 10 * 20 * var_thrity 는
# 컴파일 시점에 알 수 없는 값이므로
# 인터닝되지 않는다.
# 따라서 위에 있는 6000 의 주소와는
# 다른 주소를 참조한다.
var_thrity = 30
print(id(10 * 20 * var_thrity))

def calc_seconds_literal():    
    return 6000 # 이미 계산된 값

def calc_multiply_expression():
    return 10 * 20 * 30 # 컴파일 시점에 계산될 표현식

def calc_noInterning_expression():
    var_thirty = 30
    return 10 * 20 * var_thirty # 컴파일 시점에 계산될 표현식

# 상수 폴딩 관련해서 
# 인터닝 처리를 확인하기 위해
# dis 모듈을 이용해 바이트 코드를
# 확인

print("--- 리터럴 값 사용 ---")
dis.dis(calc_seconds_literal)

print("--- 곱하기 연산 -> 인터닝 ----")
dis.dis(calc_multiply_expression)

print("--- 인터닝 처리 발생하지 않음 ----")
dis.dis(calc_noInterning_expression)