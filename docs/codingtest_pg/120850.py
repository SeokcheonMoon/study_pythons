# https://school.programmers.co.kr/learn/courses/30/lessons/120850

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# "hi12392"에 있는 숫자 1, 2, 3, 9, 2를 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.
# 입출력 예 #2

# "p2o4i8gj2"에 있는 숫자 2, 4, 8, 2를 오름차순 정렬한 [2, 2, 4, 8]을 return 합니다.
# 입출력 예 #3

# "abcde0"에 있는 숫자 0을 오름차순 정렬한 [0]을 return 합니다.

# def solution(my_string):
#     answer = []
#     return answer

my_string = "hi12392"
result = [1, 2, 2, 3, 9]

answer = []
for x in range(len(my_string)) : 
    if my_string[x].isdecimal() == True :
        answer.append(int(my_string[x]))
answer.sort(reverse=False)
print(answer)