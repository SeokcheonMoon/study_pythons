## 나오는 값 처리

def add() :
    first = 5
    second = 4
    sum = first + second
    return sum # --------------------------------------------------- 상수 대신 변수사용!

# num_sum = 0 

num_sum = add()
print("add return 결과 : {}".format(num_sum))

# 두 수를 곱해서 결과 return

def multiply() : 
    num_first = 4
    num_second = 5
    result = num_first * num_second
    return result

num_multiply = multiply()
print("num_multiply return value : {}".format(num_multiply))


# --------------------------------------------------------------------------------------------

# list_fruits = ["melon", "apple", "banana", "cherry"]
# ##index로 값 가져오기
# list_fruits[0] # 이거 하나 자체가 변수가 되는것임.(단일변수) (1차원) (행 차원)



def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits

fruits=return_list()
print("{}".format(fruits))

#return은 한가지 값만 나온다!