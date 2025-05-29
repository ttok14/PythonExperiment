# --- 언패킹 (Unpacking) ---

# 파이썬에서 컬렉션(collection)이나 이터러블(iterable) 객체
# 안에 있는 여러 개의 값들을 "풀어서" 개별적인 변수에 할당하거나,
# 함수의 인자로 직접 전달할 수 있도록 하는 기능을 의미합니다.
# (참고: 언패킹은 내부적으로 이터레이터를 next() 하며 동작하며,
#  변수 할당 시 보통 좌변 변수의 개수와 우변 요소의 개수가 일치해야 합니다.)

# -------------------------------------#
# 1. 변수에 직접 언패킹 (다양한 이터러블)
# -------------------------------------#
print("## 1. 변수에 직접 언패킹 ##")

# 튜플 언패킹
point = (10, 20)
x, y = point
print(f"튜플 -> x: {x}, y: {y}") # 출력: 튜플 -> x: 10, y: 20

# 리스트 언패킹
colors = ["빨강", "초록", "파랑"]
r, g, b = colors
print(f"리스트 -> R: {r}, G: {g}, B: {b}") # 출력: 리스트 -> R: 빨강, G: 초록, B: 파랑

# 문자열 언패킹 (문자열도 시퀀스)
initials = "KSM"
first, second, third = initials
print(f"문자열 -> 첫째: {first}, 둘째: {second}, 셋째: {third}") # 출력: 문자열 -> 첫째: K, 둘째: S, 셋째: M

# for문과 함께 사용되는 언패킹 (리스트 안의 튜플)
pairs = [(1, '사과'), (2, '바나나')]
print("for문과 언패킹:")
for number, fruit in pairs:
    print(f"  번호: {number}, 과일: {fruit}")
# 출력:
#   번호: 1, 과일: 사과
#   번호: 2, 과일: 바나나

# 딕셔너리 .items() 결과 언패킹 (for문)
user_info_dict = {'이름': '김개발', '나이': 30}
print("딕셔너리 .items() 언패킹 (for문):")
for key, value in user_info_dict.items(): # .items()는 (키, 값) 튜플의 시퀀스를 반환
    print(f"  {key}: {value}")
# 출력:
#   이름: 김개발
#   나이: 30

# 제너레이터 언패킹
def simple_counter(limit):
    # print(f"  (제너레이터: 0부터 {limit-1}까지 생성)")
    for i in range(limit):
        yield i

gen_instance = simple_counter(3) # 제너레이터 객체 생성
val_a, val_b, val_c = gen_instance # 제너레이터가 생성하는 값을 순서대로 언패킹
print(f"제너레이터 -> val_a: {val_a}, val_b: {val_b}, val_c: {val_c}") # 출력: 제너레이터 -> val_a: 0, val_b: 1, val_c: 2
print("-" * 30)


# ----------------------------------------------------#
# 2. 함수 인자 언패킹: * (애스터리스크) 사용 - 위치 인자
# ----------------------------------------------------#
print("## 2. 함수 인자 언패킹: * (위치 인자) ##")

def display_elements(e1, e2, e3):
    print(f"요소1: {e1}, 요소2: {e2}, 요소3: {e3}")

elements_list = ['물', '불', '흙']
display_elements(*elements_list) # 리스트의 각 요소가 e1, e2, e3로 전달
# 출력: 요소1: 물, 요소2: 불, 요소3: 흙

elements_gen = simple_counter(3) # 새 제너레이터 (0, 1, 2 생성)
display_elements(*elements_gen) # 제너레이터의 각 요소가 e1, e2, e3로 전달
# 출력: 요소1: 0, 요소2: 1, 요소3: 2
print("-" * 30)


# -------------------------------------------------------------#
# 3. 함수 인자 언패킹: ** (더블 애스터리스크) 사용 - 키워드 인자
# -------------------------------------------------------------#
print("## 3. 함수 인자 언패킹: ** (키워드 인자) ##")

def print_server_config(host, port, timeout=30, **details): # **details로 나머지 키워드 인자 받음
    print(f"Host: {host}, Port: {port}, Timeout: {timeout}")
    if details:
        print("  추가 설정:")
        for key, value in details.items():
            print(f"    {key}: {value}")

config_map = {'host': 'example.com', 'port': 8080, 'retry': 3, 'user': 'batch'}
# config_map의 키-값 쌍이 host, port 및 details로 전달
# 'retry', 'user'는 **details로 수집됨
print_server_config(**config_map)
# 출력:
# Host: example.com, Port: 8080, Timeout: 30
#   추가 설정:
#     retry: 3
#     user: batch

# 일부는 직접 전달, 일부는 딕셔너리 언패킹
print_server_config(host='another.com', **{'port': 9000, 'protocol': 'https'})
# 출력:
# Host: another.com, Port: 9000, Timeout: 30
#   추가 설정:
#     protocol: https
print("-" * 30)


# -------------------------------------------------------------#
# 4. 함수 정의 시 임의의 인자 수집: *args 와 **kwargs
# (위 print_server_config 함수의 **details가 **kwargs 예시임)
# -------------------------------------------------------------#
print("## 4. 함수 정의 시 임의의 인자 수집: *args, **kwargs ##")

def log_processor(*records, **metadata): # records는 위치 인자들을 튜플로, metadata는 키워드 인자들을 딕셔너리로 받음
    print("처리할 레코드 (*args):")
    for record in records:
        print(f"  - {record}")
    print("메타데이터 (**kwargs):")
    for key, value in metadata.items():
        print(f"  - {key}: {value}")

log_processor("INFO: 시작", "WARN: 리소스 부족", timestamp="2025-05-29", server_id="SRV01")

# 출력:
# 처리할 레코드 (*args):
#   - INFO: 시작
#   - WARN: 리소스 부족
# 메타데이터 (**kwargs):
#   - timestamp: 2025-05-29
#   - server_id: SRV01
print("-" * 30)


# ----------------------------------------------------#
# 5. 컬렉션 병합: * 와 ** 사용
# ----------------------------------------------------#
print("## 5. 컬렉션 병합: * 와 ** 사용 ##")

# 리스트 및 튜플 병합 (*)
primary_colors = ['빨강', '노랑']
secondary_colors = ('파랑', '초록')
all_colors_list = [*primary_colors, '검정', *secondary_colors]
print(f"병합된 색상 리스트: {all_colors_list}") # ['빨강', '노랑', '검정', '파랑', '초록']

# 딕셔너리 병합 (**)
base_options = {'font': 'Arial', 'size': 12}
user_options = {'size': 14, 'color': 'blue'} # 'size' 키가 겹침
final_options = {**base_options, **user_options, 'bold': True} # user_options의 'size'가 우선
print(f"병합된 옵션 딕셔너리: {final_options}") # {'font': 'Arial', 'size': 14, 'color': 'blue', 'bold': True}