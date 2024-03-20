# https://school.programmers.co.kr/learn/courses/30/lessons/120847

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 두 수의 곱중 최댓값은 4 * 5 = 20 입니다.
# 입출력 예 #1

# 두 수의 곱중 최댓값은 31 * 24 = 744 입니다.

def solution(numbers):
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    return answer

# numbers = [0, 31, 24, 10, 1, 9]	
# numbers.sort(reverse=True)
# answer = numbers[0] * numbers[1]
# print(answer)