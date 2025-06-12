import copy

# 1. 원본 리스트 준비
list_original = [[1, 2], [3, 4]]

# 2. 깊은 복사 수행
list_deep = copy.deepcopy(list_original)

# 3. id()로 메모리 주소 확인
# 바깥 리스트의 id도 다르고...
print(f"원본 바깥 id: {id(list_original)}")
print(f"깊은 복사 바깥 id: {id(list_deep)}")

# 내부 리스트의 id도 완전히 다름!
print(f"원본 내부 id: {id(list_original[0])}")
print(f"깊은 복사 내부 id: {id(list_deep[0])}")

# 4. 복사본의 내부 리스트 값을 변경
list_deep[0][0] = 99

# 5. 원본 리스트 확인 -> 원본은 전혀 영향을 받지 않음!
print(f"변경 후 깊은 복사본: {list_deep}")
print(f"변경 후 원본: {list_original}")