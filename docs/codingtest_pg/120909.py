# https://school.programmers.co.kr/learn/courses/30/lessons/120909

# 문제 설명
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.
# 입출력 예 #2

# 976은 제곱수가 아닙니다. 따라서 2를 return합니다.

def solution(n):
    a = n ** 0.5
    if n % a == 0:
        answer = 1
    elif n % a != 0:
        answer = 2
    return answer

# n = 144
# a = n ** 0.5
# if n % a == 0:
#     answer = 1
# elif n % a != 0:
#     answer = 2
# print(answer)