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