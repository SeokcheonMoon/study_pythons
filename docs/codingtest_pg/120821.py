# https://school.programmers.co.kr/learn/courses/30/lessons/120821

# 문제 설명
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 설명
# 입출력 예 #1

# num_list가 [1, 2, 3, 4, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 4, 3, 2, 1]을 return합니다.
# 입출력 예 #2

# num_list가 [1, 1, 1, 1, 1, 2]이므로 순서를 거꾸로 뒤집은 배열 [2, 1, 1, 1, 1, 1]을 return합니다.
# 입출력 예 #3

# num_list가 [1, 0, 1, 1, 1, 3, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 3, 1, 1, 1, 0, 1]을 return합니다.

<<<<<<< HEAD:docs/codingtest_pg/120821 loading.py
# def solution(num_list):
#     answer = list.reversed(num_list)
#     return answer

num_list = [1,2,3,4,5]
answer_list = []
for x in range(1,len(num_list)+1) :
    answer_list.append(x)
pass 
=======
def solution(num_list):
    answer = list(reversed(num_list))
    return answer
>>>>>>> fbeeab0d6b0e704fbfced12472c00fd1dafe29f2:docs/codingtest_pg/120821.py
