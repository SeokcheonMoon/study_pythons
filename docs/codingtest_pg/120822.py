# https://school.programmers.co.kr/learn/courses/30/lessons/120822

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 #1
# my_string이 "jaron"이므로 거꾸로 뒤집은 "noraj"를 return합니다.
# 입출력 예 #2
# my_string이 "bread"이므로 거꾸로 뒤집은 "daerb"를 return합니다.

def solution(my_string):
    list_string = list(my_string)
    list.reverse(list_string)
    answer = "".join(list_string)
    return answer

# my_string = "jaron"
# list_string = list(my_string)
# list.reverse(list_string)
# answer = "".join(list_string)

# pass