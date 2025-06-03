
# 제너레이터(Generator) 학습전에 

# 일단 Iterator 와 Iterable 부터 학습 ㄱㄱ 
# 선행학습 필요데스네.

# 밑에 경우에는 tt 가 iterator 가 아닌 iterable 이기 때문에
# next() 를 사용할 수 없다.
# tt = [1,2,3]
# print(next(tt))

# yield 키워드가 붙는 함수는 
# '제너레이터(Generator) 함수'
# 라고 불린다. 
# C# 에서 yield return 이랑 완전히 동일한 개념임.
def GeneratorFunc():
    yield 1
    yield 2
    yield 3

# next 함수에 제너레이터 함수를 넣어주면 
# 실제로 해당 함수를 실행해준다.
# 그리고 첫 번째로 yield 되는 값을 반환함

# 새롭게 생긴 Generator 객체의 첫 번째 yield 출력
# (새로운 generator 객체이기에 yield 가 보존되지 않고
#   다시 처음부터 시작함, 즉 next 는 1 을 반환함)
print(next(GeneratorFunc()))

# 위와 동일
print(next(GeneratorFunc()))

# 위와 동일
print(next(GeneratorFunc()))

#---------------------------------------#
# 제너레이터 객체를 genObj 에 넣어준다
genObj = GeneratorFunc()

# next 가 해당 generator 객체를 실행시켜서
# 다음 yield 문을 만나면 바로 값을 리턴
# 즉 첫 번째로는 1 을 리턴 
print(next(genObj))

# 위에서 next 가 yield 1 까지 실행했으므로
# 다음 next 에서는 yield 2 를 만나게돼서 
# 2 를 리턴 
print(next(genObj))

# 위에서 next 가 yield 2 까지 실행했으므로
# 다음 next 에서는 yield 3 을 만나게돼서
# 3 을 리턴
print(next(genObj))

#--------------------------------------#

import time

def gen_foreach():
    for i in range(3):
        yield i
        time.sleep(1) # 1초 대기
        
for i in gen_foreach():
    print(f"generator 함수로 부터 받은 값 {i}")

# yield 가 있는 generator 함수를 호출하게 되면은 
# Iterable 인 Generator 객체가 반환이 된다.
# (Iterable 이 Generator 보다 상위 개념, Generator 가
# Iterable 인 것이지, Iterable 이 Generator 인 것은 아니다)
# list 같은 iterable 은 요소를 순회하기에
# iterable 이며 , yield 가 있는 generator 함수는 
# yield 반환문이 순회 요소가됨.(즉 __next__() 반환값)

# 리스트와 차이 
#   - 리스트는 메모리에 이미 모든 요소를 전부 할당해놓은 상태
#   - Generator 는 yield 를 만나서 반환을 하는 순간 메모리에 할당됨

# gen_foreach() 는 iterable 임 , 순회를 위해
# iterator 객체를 생성 
gen_iterator = iter(gen_foreach())

print(gen_iterator.__next__())
print(gen_iterator.__next__())
print(gen_iterator.__next__())


#-----------------------------------------#

myList = [1,2,3,4,5,6,7,8,9,10]

# 위 리스트에서 6 보다 큰 값을 Find 테스트

# * 제너레이터 초기화
# def 제너레이터_함수():
#   for n in myList:
#       if n > 6:
#           yield n 과 동일함 ! 
generatorObject = (n for n in myList if n > 6)

# 해당 제너레이터를 next 를 통해 * 실제로 실행 * 
firstGreaterThanSix = next(generatorObject, -1)
print(firstGreaterThanSix)

# 위 식을 간결하게 하면 다음과 같다 
firstGreaterThanSix = next((n for n in myList if n > 6), -1)