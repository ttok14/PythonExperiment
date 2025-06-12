# 1. 원본 리스트 준비
list_original = [[1, 2], [3, 4]]

# 2. 단순 할당
list_assigned = list_original

# 3. id()로 메모리 주소 확인 -> 완전히 동일함
print(f"원본 id: {id(list_original)}")
print(f"할당본 id: {id(list_assigned)}")

# 4. 할당된 리스트의 내부 값을 변경
list_assigned[0][0] = 99

# 5. 원본 리스트 확인 -> 원본까지 함께 변경됨!
print(f"변경 후 할당본: {list_assigned}")
print(f"변경 후 원본: {list_original}")