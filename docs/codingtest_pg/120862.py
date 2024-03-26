# 최댓값 만들기 (2)

# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 두 수의 곱중 최댓값은 -3 * -5 = 15 입니다.
# 입출력 예 #2

# 두 수의 곱중 최댓값은 10 * 24 = 240 입니다.
# 입출력 예 #3

# 두 수의 곱중 최댓값은 20 * 30 = 600 입니다.

# def solution(numbers):
#     answer = 0
#     return answer

numbers = [0, -31, 24, 10, 1, 9]
result = 240

numbers.sort(reverse=True)
answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])

# list_answer = []
# if numbers[0] > 0 and numbers[1] > 0 :
#     list_answer.append(numbers[0]*numbers[1])
# if numbers[-1] < 0 and numbers[-2]<0:
#     list_answer.append(numbers[-1]*numbers[-2])
# answer = max(list_answer)

print(answer)