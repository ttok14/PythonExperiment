myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 요소가 리스트에 포함돼있는지 체크
matching = 5
print(f"{matching} 가 리스트에 존재? : {matching in myList}")
matching = 2
print(f"{matching} 가 리스트에 존재? : {matching in myList}")
matching = 7
print(f"{matching} 가 *안* 존재? : {matching not in myList}")

# 요소의 인덱스 찾기 (index)
print(f"6 의 인덱스는 ? {myList.index(6)}")