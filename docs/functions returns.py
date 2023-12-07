## Call by value
## 나오는 값 처리

def add() :
    first = 5
    second = 4
    sum = first + second
    return sum # --------------------------------------------------- 상수 대신 변수사용!

# num_sum = 0 

num_sum = add()
print("add return 결과 : {}".format(num_sum))

# 두 수를 곱해서 결과 return

def multiply() : 
    num_first = 4
    num_second = 5
    result = num_first * num_second
    return result

num_multiply = multiply()
print("num_multiply return value : {}".format(num_multiply))