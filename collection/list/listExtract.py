myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 일부를 잘라서 새로운 리스트 반환 
# ([x:y] : 인덱스 x 부터 y - 1 인덱스까지)
# [1] 부터 [3] 의 전까지 , 즉 [1] 과 [2] 가 포함됨
sliced = myList[1:3]
print(f"Sliced {sliced}")

# [0] 에서 [2] 까지 (3 - 1)
sliced = myList[:3]
print(sliced)

# 전체 복사 
sliced = myList[:]
print(sliced)