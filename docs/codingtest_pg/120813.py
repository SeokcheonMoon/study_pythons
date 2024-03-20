# https://school.programmers.co.kr/learn/courses/30/lessons/120813

# 문제 설명
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 #1

# 10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.
# 입출력 #1

# 15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.

def solution(n):
    answer = []
    for x in range(n+1) : 
        if x % 2 == 1:
            answer.append(x)
    return answer

n = 10
result = [1, 3, 5, 7, 9]

answer = []

for x in range(n) : 
    if x % 2 == 1:
        answer.append(x)
print(answer)