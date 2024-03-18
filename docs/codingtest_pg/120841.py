# https://school.programmers.co.kr/learn/courses/30/lessons/120841

# 문제 설명
# 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.

# 입출력 예 설명
# 입출력 예 #1

# dot이 [2, 4]로 x 좌표와 y 좌표 모두 양수이므로 제 1 사분면에 속합니다. 따라서 1을 return 합니다.
# 입출력 예 #2

# dot이 [-7, 9]로 x 좌표가 음수, y 좌표가 양수이므로 제 2 사분면에 속합니다. 따라서 2를 return 합니다.

def solution(dot):
    if dot[0] > 0 and dot[1] > 0 :
        answer = 1
    elif dot[0] < 0 and dot[1] > 0 :
        answer = 2
    elif dot[0] < 0 and dot[1] < 0 :
        answer = 3
    elif dot[0] > 0 and dot[1] < 0 :
        answer = 4
    return answer

# dot = [2, 4]
# result = 1

# if dot[0] > 0 and dot[1] > 0 :
#     answer = 1
# elif dot[0] < 0 and dot[1] > 0 :
#     answer = 2
# elif dot[0] < 0 and dot[1] < 0 :
#     answer = 3
# elif dot[0] > 0 and dot[1] < 0 :
#     answer = 4
# print(answer)