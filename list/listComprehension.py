
# 기존의 리스트나 다른 순회 가능한 (Iterable)
# 객체 (e.g 튜플, 문자열, range(n) 등) 을 기반으로 하여 
# 간결하고 읽기 쉬운 방식으로 
# * 새로운 리스트를 만드는 방법 * 이다 

# 이미 존재하는 정수 리스트 
numberList = [1,2,3,4,5]

# 위 정수 리스트를 순회하며 새로운 리스트를 생성해서
# doubleNubmerComprehension 에 넣는다

# n * 2 : 이 값을 append 한다 (C# 의 linq 선 Select(t => t) 같은 느낌)
# for n : 순회하는데 접근 변수를 n 로 설정
# in numberList : 순회대상객체(Iterable) 지정 , 여기선 list.
doubleNumberComprehension = [n * 2 for n in numberList]

print(doubleNumberComprehension)

# 조건을 추가하는 것도 가능함 .

# 조건이 1 을 초과 && 4 미만의 조건에 맞는 숫자만 (if n > 1 and n < 4)
# 골라서 x2 하여 (n * 2) append 한 list 를 반환
filtered = [n * 2 for n in numberList if n > 1 and n < 4]

print(filtered)

#--------------------------------------------#

sentence = "Hello World"

# 소문자만 뽑아내서 대문자로 바꾸어 출력하기 
upper = [char.upper() for char in sentence if char.islower()]
print(upper)