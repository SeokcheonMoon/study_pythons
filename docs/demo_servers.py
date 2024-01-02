def home() : 
    html = "<body> It is home.</body>"
    return html

def error() : 
    html = "<body> It is error.</body>"
    return html

# 항시 응답 프로그램 만들기

# while True : --------------------------------------------------------------------고객 응대 기본 구성
#     work, value = input("업무 / 해당값 : ").split()
#     print("work : {}, value : {}".format(work,value))

while True : 
    work, value = input("업무 / 해당값 : ").split()
    print("work : {}, value : {}".format(work,value))    
    if work == "home" :
        result = home()
        print(result)
    else :
        result = error()
        print(result)