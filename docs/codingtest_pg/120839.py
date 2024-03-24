# 가위 바위 보

# https://school.programmers.co.kr/learn/courses/30/lessons/120839

# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# "2"는 가위이므로 바위를 나타내는 "0"을 return 합니다.
# 입출력 예 #2

# "205"는 순서대로 가위, 바위, 보이고 이를 모두 이기려면 바위, 보, 가위를 순서대로 내야하므로 “052”를 return합니다.

def solution(rsp):
    list_rsp = list(rsp)
    list_answer = []
    for x in range(len(list_rsp)):
        if list_rsp[x] == "0" :
            list_answer.append("5")
        elif list_rsp[x] == "2" :
            list_answer.append("0")
        elif list_rsp[x] == "5" :
            list_answer.append("2")

    answer = "".join(list_answer)
    return answer

# rsp = "205"
# result = "052"

# list_rsp = list(rsp)
# list_answer = []
# for x in range(len(list_rsp)):
#     if list_rsp[x] == "0" :
#         list_answer.append("5")
#     elif list_rsp[x] == "2" :
#         list_answer.append("0")
#     elif list_rsp[x] == "5" :
#         list_answer.append("2")

# answer = "".join(list_answer)
# print(answer)