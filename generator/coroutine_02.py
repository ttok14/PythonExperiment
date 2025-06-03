
def greet_coroutine():
    print("안녕하세요! 저는 코루틴입니다.")
    print("이름을 알려주시면 인사해드릴게요.")
    try:
        while True:
            name = yield  # 외부로부터 이름을 받습니다.
            if name is None: # None이 오면 종료
                print("안녕히 가세요!")
                break
            print(f"반갑습니다, {name}님!")
    except GeneratorExit: # close() 호출 시 발생
        print("코루틴이 외부에서 종료되었습니다.")

# 코루틴 사용
greeter = greet_coroutine()

# 1. 코루틴 프라이밍 (최초의 yield까지 실행)
next(greeter) # 또는 greeter.send(None)
# 출력:
# 안녕하세요! 저는 코루틴입니다.
# 이름을 알려주시면 인사해드릴게요.

# 2. 값 보내기
greeter.send("철수")
# 출력: 반갑습니다, 철수님!

greeter.send("영희")
# 출력: 반갑습니다, 영희님!

# 3. 코루틴 종료 (None을 보내거나 close() 호출)
greeter.send(None) # 또는 greeter.close()
# 출력: 안녕히 가세요!