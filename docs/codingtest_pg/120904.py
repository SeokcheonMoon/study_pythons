# 숫자 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/120904

# 문제 설명
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# 29183에서 1은 3번째에 있습니다.
# 입출력 예 #2

# 232443에서 4는 4번째에 처음 등장합니다.
# 입출력 예 #3

# 123456에 7은 없으므로 -1을 return 합니다.

def solution(num, k):
    str_num =str(num)
    list_num = list(map(int,str_num))


    for x in range(len(list_num)):
        if list_num[x] == k :
            answer = x+1
            break
        else :
            answer = -1
    return answer

# num = 123456
# k = 7
# result = 4

# str_num =str(num)
# list_num = list(map(int,str_num))


# for x in range(len(list_num)):
#     if list_num[x] == k :
#         answer = x+1
#         break
#     else :
#         answer = -1

# print(answer)