# https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 문제 설명
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.
# 입출력 예 #2

# "BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.

def solution(my_string, letter):
    list_my_string = list(my_string)

    list_answer = []
    for x in range(0,len(list_my_string)) : 

        if list_my_string[x] != letter:
            list_answer.append(list_my_string[x])
    answer = "".join(list_answer)
    return answer

# mystring = "abcdef"
# letter = "f"

# list_mystring = list(mystring)

# list_answer = []
# for x in range(0,len(list_mystring)) : 
    
#     if list_mystring[x] != letter:
#         list_answer.append(list_mystring[x])
# answer = "".join(list_answer)
# print(answer)