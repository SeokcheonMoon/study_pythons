# 기본 if elif else 구문
if True :
    pass
elif True:
    pass
else :
    pass

    #문자 비교
str_name = "seokcheon MOON"
    
    # 질문형식(condition) = 변수 + 부등호 + 기준값
    #문자에 대해 긍정으로 질문
if str_name == "seokcheon MOON" :
    pass
    print("name is {}.".format(str_name))
    
#문자에 대해 부정으로 질문
if str_name != "seokcheon MOON" :
    pass
    print("name is not {}.".format(str_name))
#if - else
#num_first >= 4 가 True 이면 : 큼, False 이면 : 작음
num_first = 5
if num_first > 4 :
    pass
    print("{}는 4보다 크다".format(num_first))
else : 
    pass
    print("{}는 4보다 작다".format(num_first))
print("End program!")

num_first = 5
if num_first > 6 :
    pass
    print("{}는 4보다 크다".format(num_first))
else : 
    pass
    print("{}는 4보다 작다".format(num_first))
print("End program!")

# if elif else 구문
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지는 F
my_score = 79

if my_score >= 90 :
    pass
    print("{}은 90점 이상이므로 A입니다.".format(my_score))
elif my_score > 80 :
    pass 
    print("{}은 80점 초과이므로 B입니다.".format(my_score))
else :
    pass
    print("{}은 80점 이하이므로 F입니다.".format(my_score))
print("End program")