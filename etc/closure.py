
# closer 함수를 리턴해주는 함수 
def make_closer(capture_var):
    # 클로저 함수 선언 
    def closer_func(param):
        # 참고로 nonlocal 로 캡처된 변수를 변경할 수도 있음.
        # (Enclosing Space 에 있는 변수에 변경하기 위해 명시)
        
        # 현 함수 (closer_func) 를 감싸는 함수인 
        # make_closer 의 변수인 capture_var 를 
        # 담고 있는 셀(Cell) 객체에 대한 참조가 
        # 현재 함수 객체의 __closure__ 튜플에 저장된다.
        
        # 네임스페이스의 관점에서는 현재 이 closer_func 에 
        # 존재하지 않는 외부 변수인 capture_var 은 
        # 외부 함수의 Enclosing space (LEGB 중 E) 에 존재하는
        # 변수임. (Enclosing space 에 있는 변수를 참조했기때문에
        # capture 한다 , 연결을 유지하기위해)
        print(f"캡처된 변수값 : {capture_var}")
        print(f"로컬 파라미터 변수 : {param}")

    return closer_func

# make_closer 함수는 클로저 함수가 아님 
closer_maker = make_closer
# make_closer 은 클로저 함수를 반환
closer_func = make_closer(capture_var=100)

# 클로저 함수 호출 테스트
closer_func(50)

# 실제 캡처된 변수에 접근하기 

# closer_maker 는 closer 를 반환하는 함수이지
# 클로저 함수가 아님 
if closer_maker.__closure__:
    for i in closer_maker.__closure__:
        print(i.cell_contents)
        print(i)
else:
    print("캡처된 변수가 없음")

# closer_func 는 클로저 함수이고 
# 캡처된 변수가 있으므로 존재 
if closer_func.__closure__:
    # __closure__ 은 캡처된 변수를 담고있는 
    # 셀(Cell) 객체의 튜플임. 그리고 하나의 
    # 셀은 하나의 캡처된 변수에 해당함 
    # 즉 이 __closure__ 튜플을 순회하며
    # 하나하나의 캡처된 변수들을 볼 수 있음.
    for i in closer_func.__closure__:
        print(i.cell_contents)
        print(i)