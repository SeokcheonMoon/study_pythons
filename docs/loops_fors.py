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

# # 설문 답변 받기

# 문장은 6개인데 답은 3개일때

# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?          index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타    index 1
 
# 당신의 답변 : A 

# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?          index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타       index 3

# 당신의 답변 : D

# 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?    index 4
# A. Python B. Java C. JavaScript D. C++ E. 기타        index 5

# 당신의 답변 : E

###############################################################################################################################################

# 설문 만드는 과정

list_polls = ["1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
            ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
            ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
            ,"3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
            ]

list_statistics = [0,0,0,0,0] # 보기 갯수만큼 0을 넣어줌.

for num_count in [0,2,4] : 
    # str_content= list_polls[num_count]
    # print("{}".format(str_content))
    str_question= list_polls[num_count]
    print("{}".format(str_question))
    str_answer= list_polls[num_count+1]
    print("{}".format(str_answer))

    str_question_result = input("당신의 답변 (A~E를 번호로 입력) : ")
    
    num_question_result =  int(str_question_result)                      # 문자를 숫자로 변환
    index = num_question_result - 1                                              #index의 위치값(사용자의 첫번째 항목은 인덱스의 0번 항목과 같다.)
    list_statistics[index] = list_statistics[index] + 1

    print("---------------------------")
    pass 

print("선호 답항 : {}".format(list_statistics))
print("End program!")