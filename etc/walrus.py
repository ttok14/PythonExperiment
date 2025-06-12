
# Walrus 문법 

myAge = 17
broAgeGap = 5
adultAge = 20

# Walrus 기본 문법 

# myAge + broAgeGap 한 것을 broAge
if (broAge := myAge + broAgeGap) >= adultAge:
    print(f"형제는 어른이다 : {broAge}")
else:
    print(f"형제는 미성년자다 : {broAge}")
    
# 스코프 확인
print(broAge)
    
if (broAge := myAge + broAgeGap) >= adultAge and (broAge := 30):
    print(f"형제는 어른이다 : {broAge}")
else:
    print(f"형제는 미성년자다 : {broAge}")

# 스코프 확인 
print(broAge)

#--------------------------------#

# 테스트할 리스트
data = ["start", "process", "end"]

# 1. data의 길이를 n에 할당하고, n이 2 이상인지 확인
#    -> AND
# 2. data의 첫 항목을 first에 할당하고, first가 'start'인지 확인

if (n := len(data)) >= 2 and (first := data[0]) == "start":
    print(f"조건 만족: 리스트에는 {n}개의 항목이 있고, '{first}'로 시작합니다.")
else:
    print("조건을 만족하지 않습니다.")

#--------------------------------#

myData = [1, 2, 3, 4, 5, 6]
it = iter(myData)

while (n := next(it, None)) is not None:
    print(n)