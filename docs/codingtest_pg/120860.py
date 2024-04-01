# 직사각형 넓이 구하기

# 문제 설명
# 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# 좌표 [[1, 1], [2, 1], [2, 2], [1, 2]] 를 꼭짓점으로 갖는 직사각형의 가로, 세로 길이는 각각 1, 1이므로 직사각형의 넓이는 1 x 1 = 1입니다.
# 입출력 예 #2

# 좌표 [[-1, -1], [1, 1], [1, -1], [-1, 1]]를 꼭짓점으로 갖는 직사각형의 가로, 세로 길이는 각각 2, 2이므로 직사각형의 넓이는 2 x 2 = 4입니다.

# def solution(dots):
#     answer = 0
#     return answer

def solution(dots):
    list_answer = []
    a = int(((dots[0][0]-dots[1][0])**2+(dots[0][1]-dots[1][1])**2)**0.5)
    b = int(((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2)**0.5)
    c = int(((dots[0][0]-dots[3][0])**2+(dots[0][1]-dots[3][1])**2)**0.5)
    list_answer.append(a)
    list_answer.append(b)
    list_answer.append(c)
    list_answer.remove(max(list_answer))
    answer = list_answer[0]*list_answer[1]
    return answer
# answer = solution(dots)



# list_answer = []
# a = int(((dots[0][0]-dots[1][0])**2+(dots[0][1]-dots[1][1])**2)**0.5)
# b = int(((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2)**0.5)
# c = int(((dots[0][0]-dots[3][0])**2+(dots[0][1]-dots[3][1])**2)**0.5)
# list_answer.append(a)
# list_answer.append(b)
# list_answer.append(c)
# list_answer.remove(max(list_answer))
# answer = list_answer[0]*list_answer[1]
# print(answer)
# x = (dots[1][0] - dots[2][1])**2
# y= (dots[0][0] - dots[1][0])**2

# num_x = int(x**0.5)
# num_y = int(y**0.5)
# answer = num_x*num_y