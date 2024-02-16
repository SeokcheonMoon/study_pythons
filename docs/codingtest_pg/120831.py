# https://school.programmers.co.kr/learn/courses/30/lessons/120831

# 문제 설명
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 입출력 예 #1
# n이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.
# 입출력 예 #2
# n이 4이므로 2 + 4 = 6을 return 합니다.

def solution(n):
    list_number = []
    for number in range(1,n+1) :
        if number % 2 == 0 :
            list_number.append(number)
    answer = 0
    for index in range(0,len(list_number)+1):
        if index == len(list_number) : 
            break
        else:
            answer = answer + list_number[index]
    return answer