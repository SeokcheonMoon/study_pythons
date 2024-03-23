# 중복된 문자 제거

# https://school.programmers.co.kr/learn/courses/30/lessons/120888

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "people"에서 중복된 문자 "p"와 "e"을 제거한 "peol"을 return합니다.
# 입출력 예 #2

# "We are the world"에서 중복된 문자 "e", " ", "r" 들을 제거한 "We arthwold"을 return합니다.

def solution(my_string):
    list_string = list(my_string)
    list_answer = []

    for x in range(len(list_string)) :
        if list_answer.count(list_string[x]) == 0 :
            list_answer.append(list_string[x])
    answer = "".join(list_answer)
    return answer

# my_string = "people"
# result = "peol"
# list_string = list(my_string)
# list_answer = []

# for x in range(len(list_string)) :
#     if list_answer.count(list_string[x]) == 0 :
#         list_answer.append(list_string[x])
# answer = "".join(list_answer)
# print(answer)