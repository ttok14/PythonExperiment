import dis

# 튜플이 상수화 되어 LOAD_CONST opcode 로 상수만 다루게끔 최적화 
print("— 상수만 있는 튜플 —")
dis.dis("x = (1, 2, 3, 4)")

# BUILD_LIST 와 BUILD_TUPLE opcode 가 사용됨
print("\n— 리스트 포함 튜플 —")
dis.dis("x = ([1, 2], 3, 4)")

# 컴파일에 알 수 없는 변수는 LOAD_NAME 으로 런타임에 가져오게끔
# 최종적으로 BUILD_TUPLE 사용됨 
print("\n— 변수 포함 튜플 —")
code = """
y = 0
x = (1, 2, 3, y)
"""
dis.dis(code)