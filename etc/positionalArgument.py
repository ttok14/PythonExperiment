    
# 파이썬에서 함수의 인자에 슬래시(/) 는 해당 함수에
# 파라미터를 넘기는 쪽에서 
# ! 해당 슬래시를 기준으로 왼쪽에 있는 모든 인자들 ! 은
# 순서대로 , 키워드(keyword argument) 지정없이 
# 넘겨야함을 강제함.

# 슬래시(/) 왼쪽에 있는 integer, string 은 키워드 지정없이
# 값을 넘겨야함 
def positionalDefTest(integer, string, /, holy):
    print(integer)
    print(string)
    print(holy)
    
def nonPositionalDefTest(integer, string):
    print(integer)
    print(string)
    
# holy 는 슬래시(/) 의 오른쪽에 있는 인자이기에 
# 키워드 지정이 가능함 
positionalDefTest(10, "십", holy=999)
nonPositionalDefTest(10, "HIHI")
nonPositionalDefTest(10, string="HIHI")

# 에러 -> 인자를 넘길때 기본적으로 키워드 인자가 위치 인자의
#       왼쪽에 위치할 수 없음. 모호함 등의 이유로 문법에 어긋남
# nonPositionalDefTest(integer=10, "HIHI")