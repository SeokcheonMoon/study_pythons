# https://school.programmers.co.kr/learn/courses/30/lessons/120908

# 문제 설명
# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "ab6CDE443fgh22iJKlmn1o" str1에 str2가 존재하므로 1을 return합니다.
# 입출력 예 #2

# "ppprrrogrammers" str1에 str2가 없으므로 2를 return합니다.
# 입출력 예 #3

# "AbcAbcA" str1에 str2가 없으므로 2를 return합니다.

def solution(str1, str2):
    if str1.count(str2) > 0 :
        answer = 1
    elif str1.count(str2) == 0 :
        answer = 2
    return answer

# str1 = "ab6CDE443fgh22iJKlmn1o"
# str2 = "6D"

# if str1.count(str2) > 0 :
#     answer = 1
# elif str1.count(str2) == 0 :
#     answer = 2
# print(answer)