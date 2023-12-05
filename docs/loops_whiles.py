# condition이 True인 동안에 동작
# while True :
#     pass

num_virtual = 0
# while 정지 -첫번째 방법: break문 사용-
while True :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5:
        pass
        break
    pass

# while 정지 -두번째 방법:
num_virtual = 0
while num_virtual < 5:
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    pass


# 풀기 : 5 구구단 결과 매번 출력