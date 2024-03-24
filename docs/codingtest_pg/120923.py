# 연속된 수의 합

# https://school.programmers.co.kr/learn/courses/30/lessons/120923

# 문제 설명
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# num = 3, total = 12인 경우 [3, 4, 5]를 return합니다.
# 입출력 예 #2

# num = 5, total = 15인 경우 [1, 2, 3, 4, 5]를 return합니다.
# 입출력 예 #3

# 4개의 연속된 수를 더해 14가 되는 경우는 2, 3, 4, 5입니다.
# 입출력 예 #4

# 설명 생략

def solution(num, total):
    value = 0
    for x in range(num):
        value = value + x
    first = int((total-value)/num)

    answer = []
    for y in range(first, first+num):
        answer.append(y)
    return answer

# num = 3
# total = 12
# # total = n*first+ 3보다 작은 자연수들 합.
# # first = {total - (n보다 작은 자연수의 합)} / num

# value = 0
# for x in range(num):
#     value = value + x
# first = int((total-value)/num)

# answer = []
# for y in range(first, first+num):
#     answer.append(y)
# print(answer)