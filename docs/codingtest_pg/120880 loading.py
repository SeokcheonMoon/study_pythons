# 특이한 정렬

# https://school.programmers.co.kr/learn/courses/30/lessons/120880

# 문제 설명
# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# 4에서 가까운 순으로 [4, 5, 3, 6, 2, 1]을 return합니다.
# 3과 5는 거리가 같으므로 더 큰 5가 앞에 와야 합니다.
# 2와 6은 거리가 같으므로 더 큰 6이 앞에 와야 합니다.
# 입출력 예 #2

# 30에서 가까운 순으로 [36, 40, 20, 47, 10, 6, 7000, 10000]을 return합니다.
# 20과 40은 거리가 같으므로 더 큰 40이 앞에 와야 합니다.

numlist = [10000,20,36,47,40,6,10,7000]
n = 30
result = [36, 40, 20, 47, 10, 6, 7000, 10000]

list_distance = []
for x in range(len(numlist)):
    original_distance = numlist[x]-n
    re_distance = int((original_distance**2)**0.5)
    list_distance.append(re_distance)
list_distance.sort(reverse=False)

list_answer = []
for y in range(len(numlist)):
    list_answer.append(list_distance.index(numlist[y])+1)

print(list_distance)