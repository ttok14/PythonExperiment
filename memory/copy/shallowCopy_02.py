# 1. 원본 리스트 준비
list_original = [[1, 2], [3, 4]]

# 2. 얕은 복사 수행
list_shallow = list_original.copy()

# 3. id()로 메모리 주소 확인
# 바깥 리스트의 id는 다르지만...
print(f"원본 바깥 id: {id(list_original)}")
print(f"얕은 복사 바깥 id: {id(list_shallow)}")

# 내부 리스트의 id는 동일함!
print(f"원본 내부 id: {id(list_original[0])}")
print(f"얕은 복사 내부 id: {id(list_shallow[0])}")

# 4. 복사본의 내부 리스트 값을 변경
list_shallow[0][0] = 99

# 5. 원본 리스트 확인 -> 내부 객체는 공유하므로 원본까지 함께 변경됨!
print(f"변경 후 얕은 복사본: {list_shallow}")
print(f"변경 후 원본: {list_original}")