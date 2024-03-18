# https://school.programmers.co.kr/learn/courses/30/lessons/120818

# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 설명
# 입출력 예 #1

# 150,000원에서 5%를 할인한 142,500원을 return 합니다.
# 입출력 예 #2

# 580,000원에서 20%를 할인한 464,000원을 return 합니다.

def solution(price):
    if price >= 500000 :
        answer = price - (price*0.2)
    elif price >= 300000 :
        answer = price - (price*0.1)
    elif price >= 100000 : 
        answer = price - (price*0.05)
    else :
        answer = price
    answer = int(answer)
    return answer

# price =580000	

# result = 464000

# if price >= 500000 :
#     answer = price - (price*0.2)
# elif price >= 300000 :
#     answer = price - (price*0.1)
# elif price >= 100000 : 
#     answer = price - (price*0.05)
# else :
#     answer = price
# answer = int(answer)
# print(answer)



