# 숨어있는 숫자의 덧셈 (1)

# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "aAb1B2cC34oOp"안의 한자리 자연수는 1, 2, 3, 4 입니다. 따라서 1 + 2 + 3 + 4 = 10 을 return합니다.
# 입출력 예 #2

# "1a2b3c4d123Z"안의 한자리 자연수는 1, 2, 3, 4, 1, 2, 3 입니다. 따라서 1 + 2 + 3 + 4 + 1 + 2 + 3 = 16 을 return합니다.

def solution(my_string):
    list_string = list(my_string)
    answer = 0
    for x in range(len(list_string)) :
        if list_string[x].isdecimal() == True:
            answer = answer + int(list_string[x])
    return answer

# my_string = "aAb1B2cC34oOp"
# result = 10

# list_string = list(my_string)
# answer = 0
# for x in range(len(list_string)) :
#     if list_string[x].isdecimal() == True:
#         answer = answer + int(list_string[x])
# print(answer)