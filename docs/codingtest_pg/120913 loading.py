# 잘라서 배열로 저장하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120913

# 문제 설명
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# "abc1Addfggg4556b" 를 길이 6씩 잘라 배열에 저장한 ["abc1Ad", "dfggg4", "556b"]를 return해야 합니다.
# 입출력 예 #2

# "abcdef123" 를 길이 3씩 잘라 배열에 저장한 ["abc", "def", "123"]를 return해야 합니다.

def solution(my_str, n):
    answer = []
    return answer

my_str = "abc1Addfggg4556b"
n = 6
result = ["abc1Ad", "dfggg4", "556b"]

list_str = list(my_str)

k = 0
answer = []

for x in range(len(my_str)):
    answer.append(list_str[k:k+6])
print(answer)