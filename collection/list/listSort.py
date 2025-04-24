# 기본 리스트 
myList = [5,2,9,7]

# (빌트인 함수) 정렬된 새 리스트 반환 
#   => 원본 리스트는 변경되지 않음
#   => 기본적으로 오름차순 정렬 (1,2,3 ..)
newSortedList = sorted(myList)
print(newSortedList)

# 마찬가지로 기본 오름차순 정렬 
myList.sort()
print(myList)

#-----------------------#
myList = ["AAAAA", "AAA", "A", "AAAAAAAA"]

# 정렬 기준을 len() 즉 각 요소의 len(요소) 로 했을때
# 반환된 값, 즉 예로 문자열이면 문자의 개수 , 리스트면 
# 리스트 요소의 개수가 됨 . 이를 기준으로 오름차순 정렬
myList.sort(key=len)
print(myList)

class Person:
    def __init__(self, age):
        self.age = age
    
    # 일반 사용자가 알아볼 수 있게끔 (pretty print 개념)
    def __str__(self):
        return str(self.age)
    
    # 개발자 위주의 데이터 확인이나 디버깅을 위한 용도
    def __repr__(self): 
        return str(self.age)
    
people = [Person(10), Person(30), Person(5), Person(15)]

youngToOld = sorted(people, key=lambda p: p.age)
print(youngToOld)

# x , y
positions = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

# x 좌표를 기준으로 정렬
positions.sort(key=lambda p: p[0])
# y 좌표를 기준으로 정렬
positions.sort(key=lambda p: p[1])

#--------------------------------------#

fruits = ["banana", "APPLE", "KIWI", "pear", "Grape"]

# 대소문자 상관없이 알파벳 순으로 정렬 
fruits.sort(key = lambda fruit: fruit.lower())
print(f"알파벳 순서 정렬 (오름차순) : {fruits}")

# 알파벳 역순으로 정렬 (내림차순)
fruits.sort(key = lambda fruit: fruit.lower(), reverse=True)
print(f"알파벳 역 순서 정렬 (내림차순) : {fruits}")

# 값이 동일한 경우 정렬 기준을 추가로 할 수 있음. 클래스로 예시 추가 
class Student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score

    # 객체를 보기 좋게 출력하기 위한 __repr__ 메소드 (옵션)
    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade}, score={self.score})"

# 학생 데이터 리스트
students = [
    Student('Alice', 3, 85),
    Student('Bob', 1, 90),
    Student('Charlie', 3, 95),
    Student('David', 2, 90),
    Student('Eve', 1, 80),
]

# 정렬: 1순위 grade (오름차순), 2순위 score (내림차순), 3순위 name 길이 (오름차순)

# *** key 함수는 각 student 객체를 받아서 (grade, -score) 튜플을 반환 ***

# score에 -를 붙인 이유: 숫자의 경우 부호를 바꾸면 정렬 순서가 반대로 됨 (내림차순 효과)
# 등급도 같고 점수도 같으면 이름의 길이로 정렬 
sorted_students = sorted(students, key=lambda s: (s.grade, -s.score, len(s.name)))

print("정렬된 학생 리스트:")

for student in sorted_students:
    print(student)