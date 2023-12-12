# list 사용 이유: 값들의 모임을 쉽게 전달

# 숫자 5개 값의 list
list_numerics = [0, 1, 2, 3, 4] 

# 문자 3개 값의 list
list_fruits = ["apple", "banana", "cherry"]

# 숫자와 문자가 섞인 list ===========================================> 가능은 하나 쓰지는 맙시다.
list_mix = [0, 1, 2, 3, "apple", "banana"]


# 단어에 len() 쓰면 글자수 확인
len("cherry")
6

# list에 쓰면 list 안에 있는 목록의 갯수 확인
len(list_mix)
6

# for 문 활용 후 다시 오기

# index (색인, 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]
##index로 값 가져오기
list_fruits[0] # 이거 하나 자체가 변수가 되는것임.(단일변수) (1차원) (행 차원)
'melon'
list_fruits[3] # list_fruits의 네번째 것을 값으로 함.
'cherry'

## error 발생
# list_fruits[5]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range

# list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"] # ==========> 원시적인 방법임. class상태임.
tuple_fruits = ("melon", "apple", "banana", "cherry") # tuple은 변화 X
list_fruits_constructor = list(("melon", "apple", "banana", "cherry")) # ==========> list초기화?                                        # list()는 자체가 class가 됨.

# list에 무언가를 추가할때 쓰는 방법임.
list_fruits_primitive.append("strawberry")  
list_fruits_constructor.append("watermelon")

# list에 있는 무언가를 없애는 방법.(2가지)
## 해당하는 언어 전부를 모두 삭제
list_fruits_primitive.remove("apple") 
list_fruits_constructor.remove("watermelon")
## list에 있는것을 모두 삭제
list_fruits_primitive.clear()

pass