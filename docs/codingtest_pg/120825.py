# https://school.programmers.co.kr/learn/courses/30/lessons/120825

# 문제 설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# "hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.

def solution(my_string, n):
    list_answer = []
    for x in range(len(my_string)):
        for y in range(n):
            list_answer.append(my_string[x])
    answer = "".join(list_answer)
    return answer

# my_string = "hello"
# n = 3
# list_answer = []
# for x in range(len(my_string)):
#     for y in range(n):
#         list_answer.append(my_string[x])
# answer = "".join(list_answer)
# print(answer)