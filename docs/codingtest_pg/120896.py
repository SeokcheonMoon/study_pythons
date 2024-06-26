# 한 번만 등장한 문자

# https://school.programmers.co.kr/learn/courses/30/lessons/120896

# 문제 설명
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

# 입출력 예 설명
# 입출력 예 #1

# "abcabcadc"에서 하나만 등장하는 문자는 "d"입니다.
# 입출력 예 #2

# "abdc"에서 모든 문자가 한 번씩 등장하므로 사전 순으로 정렬한 "abcd"를 return 합니다.
# 입출력 예 #3

# "hello"에서 한 번씩 등장한 문자는 "heo"이고 이를 사전 순으로 정렬한 "eho"를 return 합니다.

def solution(s):
    list_string = list(s)
    list_answer = []
    for x in range(len(list_string)):
        if list_string.count(list_string[x]) == 1:
            list_answer.append(list_string[x])
    list.sort(list_answer)
    answer = "".join(list_answer)
    return answer

# s = "abdc"
# result = "abcd"

# list_string = list(s)
# list_answer = []
# for x in range(len(list_string)):
#     if list_string.count(list_string[x]) == 1:
#         list_answer.append(list_string[x])
# list.sort(list_answer)
# answer = "".join(list_answer)
# print(answer)