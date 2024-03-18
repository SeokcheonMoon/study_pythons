# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 문제 설명
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# 입출력 예 설명
# 입출력 예 #1

# 1 + 2 + 3 + 4 = 10을 return합니다.
# 입출력 예 #2

# 9 + 3 + 0 + 2 + 1 + 1 = 16을 return합니다.

def solution(n):
    str_num = str(n)
    answer = 0
    for x in range(len(str_num)) :
        answer = answer + int(str_num[x])
    return answer
# n = 1234
# result = 10

# str_num = str(n)
# answer = 0
# for x in range(len(str_num)) :
#     answer = answer + int(str_num[x])
# print(answer)