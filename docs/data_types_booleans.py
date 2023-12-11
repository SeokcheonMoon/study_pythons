bool_flag = True
pass
bool_flag = False
type(bool_flag)
# <class 'bool'>

# 문자 판단 (==:같음기호)(!=:다름기호)
str_name = "seokcheon MOON" #변수를 a로 정의
str_name == "seokcheon MOON" #변수가 a가 맞나요
# True                            #네
str_name == "seokcheonMOON" #변수가 b가 맞나요
# False                           #아니요
str_name != "seokcheonMOON" #변수가 b와 다르나요
# True                            #네

# 숫자에 대한 판단 (변수 + 부등호 + 기준값)
# 컴퓨터 입장
# True = Yes = 1, False = No = 0

5 == 4
num_first = 5
num_first == 4
# False
num_first != 4
# True

num_first > 4 #초과
# True
num_first >= 4 #이상
# True

# 90점 이상 : A, 80점 초과 : B, 나머지는 F
myscore = 90
myscore >= 90
True
myscore = 89

myscore >= 90
False
myscore > 80
True
myscore = 80
myscore > 80
False
pass

# myscore > 80
# False
# myscore >= 75
# True
# myscore <= 85
# True
# myscore >= 75 and myscore <= 85
# True
# myscore >= 75 and myscore< 80
# False

#논리 연산자 (True False 에 대한 결과 연산자)
# and : 1 and 1 = 1, 나머지는 0이다.
# or : 0 or 0 -> 0, 나머지는 1
# not : 반대로 변환 


########################################################################################


# 부등호 사용시 결과는 True or False
# data type : boolean
# 인간의 말로 예,아니오 를 판단의 근거로 함.
# 50점 이상부터 60점 이하는 C학점이다. -> 긍정도 부정도 아님.
# 컴퓨터는 상태를 확인할때 논리 연산자를 사용함 (True, False)
# 현재 값이 75점 이상부터 85점 이하는 C학점이다.

pass