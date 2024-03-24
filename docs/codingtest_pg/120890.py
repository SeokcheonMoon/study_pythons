# 가까운 수

# https://school.programmers.co.kr/learn/courses/30/lessons/120890

# 문제 설명
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 3, 10, 28 중 20과 가장 가까운 수는 28입니다.
# 입출력 예 #2

# 10, 11, 12 중 13과 가장 가까운 수는 12입니다.
# ※ 공지 - 2023년 3월 29일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.

def solution(array, n):
    list_answer = []
    for x in range(len(array)):
        list_answer.append((n-array[x])**2)

    list_array = []
    for y in range(len(list_answer)):
        if list_answer[y] == min(list_answer):
            list_array.append(array[y])

    answer = min(list_array)
    return answer

# array = [3, 10, 30]	
# n = 20
# result = 28

# list_answer = []
# for x in range(len(array)):
#     list_answer.append((n-array[x])**2)

# list_array = []
# for y in range(len(list_answer)):
#     if list_answer[y] == min(list_answer):
#         list_array.append(array[y])

# answer = min(list_array)
# print(answer)