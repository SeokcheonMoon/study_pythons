# https://school.programmers.co.kr/learn/courses/30/lessons/120886

# 문제 설명
# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# "olleh"의 순서를 바꾸면 "hello"를 만들 수 있습니다.
# 입출력 예 #2

# "allpe"의 순서를 바꿔도 "apple"을 만들 수 없습니다.

# def solution(before, after):
#     answer = 0
#     return answer

before = "olleh"
after = "hello"
result = 1

list_before = list(before)
list_after = list(after)
list_before.reverse()
if list_before == list_after
    answer = 1
else :
    answer = 0

print(answer)