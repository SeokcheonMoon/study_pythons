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


# --------------------------------------------------------------------------------------------#return은 한가지 값만 나온다!

# list_fruits = ["melon", "apple", "banana", "cherry"]
# ##index로 값 가져오기
# list_fruits[0] # 이거 하나 자체가 변수가 되는것임.(단일변수) (1차원) (행 차원)



def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits

fruits=return_list()
print("{}".format(fruits))

# list_fruits = ["melon", "apple", "banana", "cherry"]
# ##index로 값 가져오기
# list_fruits[0]

# list 중에 index로 값 return
def return_listbyindex() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    #index로 값 가져오기
    return list_fruits[0] # 단일 변수로 여김 1차원(행)

print("return_listbyindex() return result : {}".format(return_listbyindex()))

# --------------------------------------------------------------------------------------------------------------------------

# my_score = 79
# if my_score >= 90 :
#     print("{}은 90점 이상이므로 A입니다.".format(my_score))
# elif my_score > 80 :
#     print("{}은 80점 초과이므로 B입니다.".format(my_score))
# else :
#     print("{}은 80점 이하이므로 F입니다.".format(my_score))

##반복 print 작업을 줄이기 위한 function 만들기

def return_grade() :
    my_score = 90
    my_grade = ""
    if my_score >= 90 :
        my_grade = "A"
    elif my_score > 80 :
        my_grade = "B"
    else :
        my_grade = "C"
    return my_grade

str_grade = return_grade()
print("당신의 학점은 {} 입니다".format(str_grade))