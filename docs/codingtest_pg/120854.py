# https://school.programmers.co.kr/learn/courses/30/lessons/120854

# 문제 설명
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1
# ["We", "are", "the", "world!"]의 각 원소의 길이인 [2, 3, 3, 6]을 return합니다.
# 입출력 예 #2
# ["I", "Love", "Programmers."]의 각 원소의 길이인 [1, 4, 12]을 return합니다.

def solution(strlist):
    answer = []
    for x in range(0,len(strlist)) : 
        answer.append(len(list(strlist[x])))
    return answer

# strlist = ["We", "are", "the", "world!"]
# pass
# answer = []
# for x in range(0,len(strlist)) : 
#     answer.append(len(list(strlist[x])))

# print(answer)