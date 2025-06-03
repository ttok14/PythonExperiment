import sys

# --- 1. 빌트인 네임스페이스 (Built-in Namespace) ---
# 파이썬 인터프리터가 시작될 때 로드되는 내장 함수, 상수, 예외 등의 이름들입니다.

# print 나 list 나 int 등을 별도 임포트없이 사용가능한 이유가 
# 파이썬이 프로그램 시작과 동시에 내부적으로 builtIn 네임스페이스를 로드하기 때문 

print("--- 1. 빌트인 네임스페이스 (예시) ---")
built_in_names = list(dir(__builtins__))
print(f"빌트인 네임스페이스의 총 이름 개수: {len(built_in_names)}")
print(f"일부 빌트인 이름 (처음 5개): {built_in_names[:5]}")
print(f"일부 빌트인 이름 (마지막 5개): {built_in_names[-5:]}\n")


# --- 2. 글로벌 (모듈) 네임스페이스 (Global/Module Namespace) ---
# 현재 실행 중인 모듈의 최상위 수준에서 정의된 변수, 함수, 클래스 등의 이름들입니다.
module_level_variable = "이것은 모듈 수준 변수입니다 (글로벌 네임스페이스)"

def module_level_function():
    pass

class ModuleLevelClass:
    pass

print("--- 2. 글로벌 (모듈) 네임스페이스 (현재 모듈) ---")
# globals()는 현재 모듈의 글로벌 네임스페이스 딕셔너리를 반환합니다.
global_names_keys = list(globals().keys())
print(f"모든 글로벌 이름 (처음 10개, 섀도잉되지 않은 경우 빌트인 포함 가능): {global_names_keys[:10]}...")
# 사용자가 이 모듈에서 직접 정의한 주요 이름들 확인
print(f"'module_level_variable'이 globals에 있습니까? {'module_level_variable' in global_names_keys}")
print(f"'module_level_function'이 globals에 있습니까? {'module_level_function' in global_names_keys}")
print(f"'ModuleLevelClass'가 globals에 있습니까? {'ModuleLevelClass' in global_names_keys}\n")


# --- 3. 클래스 네임스페이스 (Class Namespace) ---
# 클래스 정의 내부에 있는 클래스 변수, 메서드 등의 이름들입니다.
class MyCustomClass:
    class_variable = "이것은 클래스 변수입니다"
    _internal_class_var = "내부 사용 목적"

    def __init__(self, name):
        self.name = name # 이것은 인스턴스 네임스페이스에 저장됩니다.

    def instance_method(self):
        return f"{self.name}의 메서드"

    @classmethod
    def class_method_example(cls):
        return "이것은 클래스 메서드입니다"

    @staticmethod
    def static_method_example():
        return "이것은 정적 메서드입니다"

print("--- 3. 클래스 네임스페이스 (MyCustomClass) ---")
# 클래스 객체의 __dict__는 해당 클래스가 직접 정의한 속성들을 보여줍니다.
class_namespace_keys = list(MyCustomClass.__dict__.keys())
print(f"MyCustomClass.__dict__.keys(): {class_namespace_keys}")
# dir(MyCustomClass)는 상속된 멤버를 포함하여 더 많은 이름을 보여줄 수 있습니다.
# print(f"dir(MyCustomClass) (처음 10개): {dir(MyCustomClass)[:10]}...\n")
print()

# --- 4. 인스턴스 네임스페이스 (Instance Namespace) ---
# 클래스의 각 인스턴스가 가지는 고유한 속성들의 이름입니다.
my_instance = MyCustomClass("내인스턴스객체")
my_instance.another_attribute = "동적으로 추가된 속성"

print("--- 4. 인스턴스 네임스페이스 (my_instance) ---")
# 인스턴스 객체의 __dict__는 해당 인스턴스에만 속하는 속성들을 보여줍니다.
if hasattr(my_instance, '__dict__'):
    instance_namespace_keys = list(my_instance.__dict__.keys())
    print(f"my_instance.__dict__.keys(): {instance_namespace_keys}")
else:
    # __slots__를 사용하고 __dict__를 명시적으로 포함하지 않으면 없을 수 있습니다.
    print("my_instance는 __dict__ 속성을 가지고 있지 않습니다.")

# dir(my_instance)는 인스턴스 속성, 클래스 속성, 상속된 속성 등을 모두 보여줍니다.
# print(f"dir(my_instance) (처음 10개): {dir(my_instance)[:10]}...\n")
print()

# --- 5. 로컬 (함수) 네임스페이스 (Local/Function Namespace) ---
# 함수가 호출될 때 생성되며, 함수 내의 지역 변수와 매개변수 이름들을 포함합니다.
def example_function_scope(param_a, param_b="기본값"):
    local_variable_x = 100
    local_variable_y = "안녕"

    print("--- 5. 로컬 (함수) 네임스페이스 (example_function_scope 내부) ---")
    # locals()는 현재 (함수) 스코프의 로컬 네임스페이스 딕셔너리를 반환합니다.
    local_namespace_keys = list(locals().keys())
    print(f"locals().keys(): {local_namespace_keys}")
    # dir()을 인자 없이 호출하면 현재 로컬 스코프의 이름들을 리스트로 반환합니다.
    # print(f"함수 내부 dir(): {dir()}")
    print("-" * 20)

example_function_scope("인자1", param_b="인자2")
