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

pass


str_num =  [0, 1, 2, 3, "apple", "banana"].split()