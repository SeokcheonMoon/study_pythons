# https://school.programmers.co.kr/learn/courses/30/lessons/120910

# 문제 설명
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 처음엔 2마리, 1시간 후엔 4마리, 2시간 후엔 8마리, ..., 10시간 후엔 2048마리가 됩니다. 따라서 2048을 return합니다.
# 입출력 예 #2

# 처음엔 7마리, 1시간 후엔 14마리, 2시간 후엔 28마리, ..., 15시간 후엔 229376마리가 됩니다. 따라서 229,376을 return합니다.

def solution(n, t):
    answer = n
    for x in range(t) : 
        answer =  answer*2
    return answer

# n = 7
# t = 15
# answer = n
# for x in range(t) : 
#     answer =  answer*2
# print(answer)