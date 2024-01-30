def add(first, second) :          #이 줄에 변수
    sum = first + second
    return sum # --------------------------------------------------- 상수 대신 변수사용!

def multiply(first, second) :          #이 줄에 변수
    result = first * second
    return result

def process_call_function(first, second, callback_function) :
    result = callback_function(first,second)
    return result

if __name__ == "__main__":
    # result = add(5,6)
    result = process_call_function(5,6,add)
    result = process_call_function(5,6,multiply)
    pass