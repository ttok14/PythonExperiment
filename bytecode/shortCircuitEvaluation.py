import dis

def and_example(a, b):
    return a and b

def or_example(a, b):
    return a or b

print("\n--- and_example 바이트코드 ---")
dis.dis(and_example)
# 출력에서 POP_JUMP_FORWARD_IF_FALSE (또는 유사한) 명령어를 찾아보세요.

print("\n--- or_example 바이트코드 ---")
dis.dis(or_example)
# 출력에서 POP_JUMP_FORWARD_IF_TRUE (또는 유사한) 명령어를 찾아보세요.