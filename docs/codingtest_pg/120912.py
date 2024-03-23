# 7의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/120912

# 문제 설명
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# [7, 77, 17]에는 7이 4개 있으므로 4를 return 합니다.
# 입출력 예 #2

# [10, 29]에는 7이 없으므로 0을 return 합니다.

def solution(array):
    split_array = []
    for x in range(len(array)):
        split_array.append(str(array[x]))

    join_array = "".join(split_array)
    list_array = list(map(int,join_array))
    answer = list_array.count(7)
    return answer

# array = [7, 77, 17]
# result = 4

# split_array = []
# for x in range(len(array)):
#     split_array.append(str(array[x]))

# join_array = "".join(split_array)
# list_array = list(map(int,join_array))
# answer = list_array.count(7)
# print(answer)