# https://school.programmers.co.kr/learn/courses/30/lessons/120833

# 문제 설명
# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4, 5]의 1번째 인덱스 2부터 3번째 인덱스 4 까지 자른 [2, 3, 4]를 return 합니다.
# 입출력 예 #2

# [1, 3, 5]의 1번째 인덱스 3부터 2번째 인덱스 5까지 자른 [3, 5]를 return 합니다.

def solution(numbers, num1, num2):
    answer = []
    for x in range(num1, num2+1) :
        answer.append(numbers[x])
    return answer

# numbers = [1, 2, 3, 4, 5]
# num1 = 1
# num2 = 3

# answer = []
# for x in range(num1, num2+1) :
#     answer.append(numbers[x])
# print(answer)