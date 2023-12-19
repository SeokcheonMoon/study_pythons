# function에 들어가는 값들

# 들어가는 값은 여러개, 나오는 값은 하나

def add(first, second) :          #이 줄에 변수
    sum = first + second
    return sum # --------------------------------------------------- 상수 대신 변수사용!

if __name__ == "__main__" :   
    # num_sum = 0
    num_sum = add(5, 4)     # 상수 parameters 사용
    print("add() return 결과 : {}".format(num_sum))
    third = 6
    fourth = 10
    num_sum = add(third, fourth)    # function 부르면 값들만 전달됨
    print("add() return 결과 : {}".format(num_sum))

# ---------------------------------------------------------------------------------
# third = input()
# fourth = input()

# fifth = int(third)
# sixth = int(fourth)

# num_sum = add(fifth,sixth) #----------------------------- #function을 부르면 값들만 전달됨.
# print("add return 결과 : {}".format(num_sum))


# 내 점수를 넣으면 학점이 나오는 function
def return_grade(my_score) :
    my_grade = ""
    if my_score >= 90 :
        my_grade = "A"
    elif my_score > 80 :
        my_grade = "B"
    else :
        my_grade = "C"
    return my_grade

if __name__ == "__main__" :    
    # str_grade = return_grade(99)
    # print("당신의 학점은 {} 입니다".format(str_grade))
    my_score = 88
    str_grade = return_grade(my_score)
    print("당신의 학점 : {}".format(str_grade))