
# 튜플 언패킹 (튜플 언패킹) 기능 소개 

# 튜플 언패킹이란 시퀀스를 (튜플 리스트 등..)
# 현재 요소값들을 컴마(,) 로 나누어진
# 변수에 할당할 수 있게 해준다

# 언패킹은 내부적으로 iterator 를 next() 하며 동작함. 참고 

# * 주의 : 변수의 개수와 시퀀스의 개수 일치  **

my_tuple = (10, 20)

x, y = my_tuple
print(f"x : {x} , y : {y}")

my_list = ["A", "B", "C", "D"]
one, two, three, four = my_list
print(f"{one} , {two} , {three} , {four}")

#-------------------------------------#

# 튜플을 요소로 갖는 리스트 
pairs = [(1, 'one'), (2, 'two')]

# 리스트[튜플] 를 언패킹
one, two = pairs

# 튜플, 튜플로 언패킹됨
print(f"1. {one[0]} | {one[1]}")
print(f"2. {two[0]} | {two[1]}")

# 반복문을 순회하는 요소(iterator) 의 
# 시퀀스일때 for 뒤에 있는 있는
# 변수의 개수와 현재 시퀀스에 있는 요소의
# 개수가 같다면 자동으로 언패킹을 적용하여
# 변수에 값을 할당해줌 
for number, name in pairs:
    print(f"{number} is {name}")
        
#--------------------------------------#

# Dictionary 에서 view 언팩킹

dict_words = {
    1: "One",
    2: "Two",
    3: "Three"
}

# items() 는 dict_items[_KT, _VT] 을 반환 
# items() 의 각 요소는 튜플로서 존재
items = dict_words.items()

# items 에 대한 iterator 가 내부적으로 
# next() 를 진행하며 값을 순회 
# (items 에서 요소는 참고로 튜플)
for num, eng in items:
    print(f"(dic items() for) | num : {num} , eng : {eng}")

# iterator 새로 ! 생성     
itemIter = iter(items)

# 처음부터 순회, for 문 동작 방식 직접 구현 
print(f"item : {next(itemIter)}")
print(f"item : {next(itemIter)}")

# 언팩킹 발생 . 
# items() 의 각 요소가 튜플이기에 
# 좌변 변수 2 개로 언팩킹 성공
num, eng = next(itemIter)
print(f"num : {num} , eng : {eng}")
    
#-----------------------------#

# Generator 함수로 튜플 반환 테스트해서 
# 언팩킹 테스트 

def getTuple():
    yield (1, 2)
    yield (3, 4)

it = getTuple()
print(next(it))

# 총 5 개의 요소를 가지는 튜플을 생성
my_iterable = iter((10, 20, 30 ,40, 50)) # 이터레이터가 각 값을 순차적으로 반환
# !!!! 여기서 하나 패스 !!!!
next(my_iterable)

# 언팩킹 발생 ! 
# ** 내부적으로 iterator 를
# next() 로 이동하며 채우기때문에 
# 이 전에 한번 패스된 값은 들어가지 않고
# [1] 부터 즉 20 부터 들어감 ! 중요함.
a, b, c, d = my_iterable

# 20
print(f"a: {a}")
# 30
print(f"b: {b}")
# 40
print(f"c: {c}")
# 50
print(f"d: {d}")

# 그리하여 이런게 가능하다 . 
c, d = [30, 40]

print(c)
print(d)

for i,j in getTuple():
    print(f"{i} , {j}")
    