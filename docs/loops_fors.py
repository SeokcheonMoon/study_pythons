# for 기본 문법

for x in [] : 
    pass

# 얼마만큼 반복할지에 대한 값들을 알려줌.
numeric = 0 # 기본적으로 변수에는 하나의 값이 정의.
numerics = [0, 1, 2, 3, 4] # 변수 정의를 한꺼번에 묶음으로 지정할때 사용 # 리스트라는 의미 # 5가지 총알이 들어간 탄창이라고 생각하면됨.
# for 문은 리스트와 쌍이다.
# for 순서있는값 in 리스트변수 : 
#     pass
for number in numerics : 
    pass
    print(number)

# x는 변수, x는 for 내에서만 쓸수 있음.
list_fruits = ["apple", "melon", "banana", "cherry"]
for x in ["apple", "melon", "banana", "cherry"] :  # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name: {}!".format(x))

# 응용 (x는 str_fruits로, list 는 list_fruits로 변경)
list_fruits = ["apple", "melon", "banana", "cherry"]
for str_fruits in list_fruits :  # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name: {}!".format(str_fruits))

numerics = [0, 1, 2, 3, 4] 
for number in numerics : 
    pass
    print("Number : {}.".format(number+2))
print("End program!")
