# https://school.programmers.co.kr/learn/courses/30/lessons/120824

# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.
# 입출력 예 #2

# [1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.

def solution(num_list):
    a = 0
    b = 0
    for x in range(len(num_list)) :  
        if num_list[x] % 2 == 0 :
            a = a + 1
        elif num_list[x] % 2 == 1 :
            b = b + 1
    answer = []
    answer.append(a)
    answer.append(b)
    return answer

# num_list = [1,2,3,4,5]
# a = 0
# b = 0
# for x in range(len(num_list)) :  
#     if num_list[x] % 2 == 0 :
#         a = a + 1
#     elif num_list[x] % 2 == 1 :
#         b = b + 1
# answer = []
# answer.append(a)
# answer.append(b)
# print(answer)