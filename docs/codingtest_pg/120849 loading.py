# 모음 제거

# https://school.programmers.co.kr/learn/courses/30/lessons/120849

# 문제 설명
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "bus"에서 모음 u를 제거한 "bs"를 return합니다.
# 입출력 예 #1

# "nice to meet you"에서 모음 i, o, e, u를 모두 제거한 "nc t mt y"를 return합니다.

# def solution(my_string):
#     answer = ''
#     return answer

my_string = "nice to meet you"
result = "nc t mt y"

list_string = list(my_string)
list_quest = ["a","e","i","o","u"]

for x in range(len(list_quest)):
    for y in range(len(list_string)):
        if list_quest[x] == list_string[y]:
            list_string.remove(list_string[y])

print(list_string)