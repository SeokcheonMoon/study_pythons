# 주사위의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/120845

# 문제 설명
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 상자의 크기가 가로 1, 세로 1, 높이 1이므로 모서리의 길이가 1인 주사위는 1개 들어갈 수 있습니다.
# 입출력 예 #2

# 상자의 크기가 가로 10, 세로 8, 높이 6이므로 모서리의 길이가 3인 주사위는 12개 들어갈 수 있습니다.

def solution(box, n):
    list_answer = []
    for x in range(len(box)):
        list_answer.append(box[x]//n)

    answer = list_answer[0]*list_answer[1]*list_answer[2]
    return answer

# box = [10, 8, 6]
# n = 3

# list_answer = []
# for x in range(len(box)):
#     list_answer.append(box[x]//n)

# answer = list_answer[0]*list_answer[1]*list_answer[2]
# print(answer)