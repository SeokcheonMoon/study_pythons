# https://school.programmers.co.kr/learn/courses/30/lessons/120893

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 소문자는 대문자로 대문자는 소문자로 바꾼 "CCCccc"를 return합니다.
# 입출력 예 #2

# 소문자는 대문자로 대문자는 소문자로 바꾼 "ABcDeFGHij"를 return합니다.

def solution(my_string):
    list_answer = []
    list_string = list(my_string)
    pass
    for x in range(len(list_string)):
        if list_string[x].islower() == True :
            list_answer.append(list_string[x].upper())
        elif list_string[x].isupper() == True :
            list_answer.append(list_string[x].lower())
    answer = "".join(list_answer)
    return answer

# my_string = "abCdEfghIJ"
# result = "ABcDeFGHij"

# list_answer = []

# list_string = list(my_string)
# pass
# for x in range(len(list_string)):
#     if list_string[x].islower() == True :
#         list_answer.append(list_string[x].upper())
#     elif list_string[x].isupper() == True :
#         list_answer.append(list_string[x].lower())
# answer = "".join(list_answer)
# print(answer)