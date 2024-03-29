# 진료순서 정하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120835

# 문제 설명
# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# emergency가 [3, 76, 24]이므로 응급도의 크기 순서대로 번호를 매긴 [3, 1, 2]를 return합니다.
# 입출력 예 #2

# emergency가 [1, 2, 3, 4, 5, 6, 7]이므로 응급도의 크기 순서대로 번호를 매긴 [7, 6, 5, 4, 3, 2, 1]를 return합니다.
# 입출력 예 #3

# emergency가 [30, 10, 23, 6, 100]이므로 응급도의 크기 순서대로 번호를 매긴 [2, 4, 3, 5, 1]를 return합니다.

def solution(emergency):
    solving_list = []
    for x in range(len(emergency)):
        solving_list.append(emergency[x])

    solving_list.sort(reverse=True)
    answer = []
    for x in range(len(emergency)):
        answer.append(solving_list.index(emergency[x])+1)
    return answer

# emergency = [3, 76, 24]
# # solving_emergency = [3, 76, 24]
# # result = [3, 1, 2]

# # solving_emergency.sort(reverse=True)
# # list_answer = []
# # for x in range(len(origin_emergency)):
# #     list_answer.append(solving_emergency.index(origin_emergency[x])+1)
# # print(list_answer)

# solving_list = []
# for x in range(len(emergency)):
#     solving_list.append(emergency[x])

# solving_list.sort(reverse=True)
# answer = []
# for x in range(len(emergency)):
#     answer.append(solving_list.index(emergency[x])+1)

# print(answer)