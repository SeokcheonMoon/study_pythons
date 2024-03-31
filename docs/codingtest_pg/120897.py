# 약수 구하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120897

# 문제 설명
# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 24의 약수를 오름차순으로 담은 배열 [1, 2, 3, 4, 6, 8, 12, 24]를 return합니다.
# 입출력 예 #2

# 29의 약수를 오름차순으로 담은 배열 [1, 29]를 return합니다.

def solution(n):
    answer = []
    for x in range(1,n+1):
        if n%x == 0:
            answer.append(x)
    return answer

# n=24
# result=[1, 2, 3, 4, 6, 8, 12, 24]
# answer = []
# for x in range(1,n+1):
#     if n%x == 0:
#         answer.append(x)
# print(answer)