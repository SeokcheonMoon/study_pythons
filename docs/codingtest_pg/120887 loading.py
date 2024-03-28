# k의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

# 문제 설명
# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 본문과 동일합니다.
# 입출력 예 #2

# 10부터 50까지 5는 15, 25, 35, 45, 50 총 5번 등장합니다. 따라서 5를 return 합니다.
# 입출력 예 #3

# 3부터 10까지 2는 한 번도 등장하지 않으므로 0을 return 합니다.

# def solution(i, j, k):
#     answer = 0
#     return answer

i = 1
j = 13
k = 1
result = 6

string_number = []
answer = 0
for x in range(i,j+1):
    string_number.append(str(x))

list_number = []
for y in range(len(string_number)):
    list_number.append(str(string_number[y]).split())

list_final = list(map(int(list_number)))
print(list_final)

# list_number = list(map(int,string_number))
# for y in range(len(list_number)):
#     list