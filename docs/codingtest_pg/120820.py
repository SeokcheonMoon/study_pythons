# https://school.programmers.co.kr/learn/courses/30/lessons/120820

# 문제 설명
# 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

# 입출력 예 #1
# 2022년 기준 40살이므로 1983년생입니다.
# 입출력 예 #2
# 2022년 기준 23살이므로 2000년생입니다.

def solution(age):
    answer = 2023 - age
    return answer