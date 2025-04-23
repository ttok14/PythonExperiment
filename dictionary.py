"""
    - 순서 (Python 3.7+): 파이썬 3.7 버전부터는 딕셔너리에 데이터를
        넣은 순서가 그대로 유지됩니다. 
        (그 이전 버전에서는 순서가 보장되지 않았어요.
        C#의 Dictionary도 기본적으로는 순서를 보장하지 
        않는 것과 비슷했죠.)
"""

# 빈 Dictionary 생성
empty_dict = {}  # 빈 딕셔너리
empty_dict02 = dict()  # 빈 딕셔너리

# Dictionary 에 데이터 넣기
dict_words = {
    "사랑": "love",
    "행복": "happiness",
    "슬픔": "sadness",
    "기쁨": "joy"
}

# 모든 키 조회
print(dict_words)

# 주의 : 없는 키를 조회하면 KeyError 발생
print(dict_words["기쁨"])

# 값 수정
dict_words["기쁨"] = "new_joy"

print(dict_words["기쁨"])

# 값 추가
dict_words["고통"] = "pain"

print(dict_words["고통"])

# 값 제거
del dict_words["고통"]
popped = dict_words.pop("기쁨")
print("popped : ", popped)

# 순회 
for key in dict_words:
    print(f"{key} , {dict_words[key]}")
    
# 키 존재 체크 
if "슬픔" in dict_words:
    print("슬픔 존재")
else: 
    print("슬픔 없음")
    
#--- 타입 힌트 부여---#
dict_words: dict[int, str] = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
}

# 타입 힌트로 str 의 upper() 메소드 자동 완성
# dict_words[2] 는 str 타입으로 인식됨
print(dict_words[2].upper())
#------------------#

# 모든 키 조회
print(dict_words.keys())

# 모든 값 조회
print(dict_words.values())

# Dictionary 복사 
copied = dict_words.copy()
dict_words[2] = "new_two"

print(f"Bef : {dict_words.values()}")
print(f"Aft : {copied.values()}")

class Person:
    def __init__(self, name):
        self.name = name

# C# 과 같이 클래스는 인스턴스라서 dictionary 를 copy 해도 
# 원본 인스턴스는 그대로라 원본이 바뀌면 복사본도 바뀜 테스트
dict_people = {
    "사람1": Person("제이스"),
    "사람2": Person("제드")
}

# 카피 
dict_people_copied = dict_people.copy()

# 원본 수정 
dict_people["사람1"].name = "new_제이스"

# 복사본도 수정됐음을 확인
print(dict_people_copied["사람1"].name)

## deepcopy 위함 (copy.deepcopy())
import copy 

# Shallow Copy 가 아닌 Deep Copy 로 원본 Person 인스턴스가 아닌
# 새로운 Person 인스턴스를 생성합니다.
dict_people_copied = copy.deepcopy(dict_people)

dict_people["사람2"].name = "new_제드2"

print("Ori 사람2 : " + dict_people["사람2"].name)
print("Copied 사람2: " + dict_people_copied["사람2"].name) 

# 튜플 형태로 반환 (키, 값)
dict_country = {
    "한국": "Korea",
    "미국": "USA",
    "일본": "Japan",
}
    
tuples = dict_country.items()
print(tuples)

# 값 가져옴 , 없으면 None 리턴 (C# 에서 TryGetValue())
t = dict_country.get("한국", "None")
print(t)