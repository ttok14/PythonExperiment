import dis

# 아래와 같은 방법으로 코드를 디스어셈블할 수도 있음
# dis.dis("print('HELLO WORLD')")

# codeObject 는 파이썬 코드가 컴파일된 결과물임 (바이트코드로)
# 바이트코드뿐 아니라 코드 실행에
# 필요한 각종 정보들 (상수, 변수 이름 등) 을 
# 담고있음. 모든 실행가능한 파이썬 코드는
# 내부적으로 이 코드 객체로 표현됨

# compile() 로 소스 코드 문자열을 codeObject 로 
# 직접 컴파일할 수 있음.
codeObject = compile("""
print('HELLO WORLD')
n = 100
n2 = 10*10
n3 = 2000
print(n)
print(n2)
print(n3)
""", "<string>", "exec")

# co_code 는 바이트코드의 실제 바이트열을 의미
# PVM 이 실행할 수 있는 명령어들의 시퀀스 
print(f"실제 바이트코드 : {codeObject.co_code}")

# co_consts 는 코드 객체의 상수들을 의미함
# 예로 위 코드에서는 'HELLO WORLD' 문자열과
# 숫자 100 과 2000 이 상수로 추가됨
# 10*10은 100 이므로 100 이미 있으므로 
# 이미 추가된 100 을 가리키게끔 컴파일됨 (상수 폴딩)
print(f"인터닝된 상수들 (튜플) : {codeObject.co_consts}")

# co_names 는 코드 객체에서 사용된
# 이름(심볼)들의 목록임
# 예로 위에서는 print, n, n2, n3 가 사용됐으므로
# ['print', 'n', 'n2', 'n3'] 가 출력됨
# 그리고 LOAD_NAME, STORE_NAME 등의 NAME 을 
# 사용하는 바이트코드 명령어가 있을때
# 이 co_names 에서 해당 이름을 찾아서 참조함
# (e.g LOAD_NAME   0(print) 면
# 튜플의 0 번째 요소가 print 라는거고 이를 로드하는것)
print(f" {codeObject.co_names}")

# dis 모듈을 이용해서 바이트코드를
# 사람이 읽을 수 있는 형태로 변환
dis.dis(codeObject)