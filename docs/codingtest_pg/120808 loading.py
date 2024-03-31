# 분수의 덧셈

# https://school.programmers.co.kr/learn/courses/30/lessons/120808

# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
# 입출력 예 #2

# 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

def solution(numer1, denom1, numer2, denom2):
    answer = []
    return answer

numer1=1
denom1=2
numer2=3
denom2=4

for x in range(max(denom1, denom2),denom1*denom2+1):
    if x%denom1 == 0 and x%denom2 == 0:
        num_bottom = x
        break

num_first = numer1/denom1
num_second = numer2/denom2

num_answer = num_first+num_second
num_top=int(num_answer*num_bottom)
answer = []
answer.append(num_top)
answer.append(num_bottom)
print(answer)