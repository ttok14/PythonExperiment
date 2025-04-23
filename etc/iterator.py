
# Iterable 과 Iterator

# * Iterable 은 반복이 가능한 객체 의미
#   -> for i in range(10) 에서 range(10) 이
#      iterable 인 것임. 
# * 기술적으로는 Iterable 객체는 내부에 __iter__()
#      메서드를 구현하고 있음. (list 도 내부에 __iter__() 구현)

myList = [1,2,3,4,5]

# myList 의 type 은 list 임 
print(type(myList))

# iterable 은 아래와 같이 for 에서
# in 뒤에 사용될 수 있음 
for i in myList:
    print(i)

#---------------------------------#
  
# Iterator 은 실제로 iterable 객체 내에서
# 값에 실제적으로 접근하는 객체 . 
# 즉 실제적으로 list 인 경우는 list 의 요소에
# 접근하는 원리가 내부적으론 iterator 가 리스트를
# 순회하는 것임 . (함수면 yield 반환 순서)

# 실제 요소 순회를 위해 
# myList 의 iterator 객체 생성
myListIter = iter(myList)

# 타입 확인하면 list_iterator 가 나옴 
print(type(myListIter))

# 실제 값에 접근하기 

# !* 실제로 __next__() 함수로 접근할 일은
# 없다고 보면 됨. (예외적인 디버깅이나 로우 레벨 작업 등 제외하고)
# 예시를 들기 위해 예외적으로 호출함.

# __next__() 로 iterator 가 다음 요소(함수면 다음 yield 반환문)
# 까지 실행하여 반환 
print(myListIter.__next__())
print(myListIter.__next__())
print(myListIter.__next__())
print(myListIter.__next__())
print(myListIter.__next__())

# 위 코드는 결국 아래와 같다.
# 아래 코드는 iterable 인 list 를 
# for 로 순회하는데, 내부적으로는 iter(myList)
# 로 해서 .__next__() 로 순회한다 
for i in myList:
    print(i)
    
#---------------------------------------------#

# yield 로 반환하는 함수는 Generator 함수라고함 .
# Generator 예제도 확인할것