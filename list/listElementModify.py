# 리스트 생성
myList = [1, 2 ,3]

# 요소 추가 (append)
myList.append(100)
print(myList)

# 요소 중간 삽입 (insert)
myList.insert(1, 150)
print(myList)

# 합치기 (extend)
anotherList = ["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째", "일곱번째"]
extended = myList.extend(anotherList)

# 요소 삭제 
del anotherList[2]

# 매칭 조건 충족하는 첫 번째 요소 삭제
anotherList.remove("네번째")
print(anotherList)

# 요소 삭제 후 반환 (pop)
print(anotherList.pop(1))