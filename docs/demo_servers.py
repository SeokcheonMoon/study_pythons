def home(value) : 
    html = "<body> It is home, value {} </body>".format(value)
    return html

def error(value) : 
    html = "<body> It is error, value {} </body>".format(value)
    return html

# 항시 응답 프로그램 만들기

# while True : --------------------------------------------------------------------고객 응대 기본 구성
#     work, value = input("업무 / 해당값 : ").split()
#     print("work : {}, value : {}".format(work,value))

while True : 
    work, value = input("업무 / 해당값 : ").split()
    print("work : {}, value : {}".format(work,value))    
    if work == "home" :
        result = home(value)
        print(result)
    else :
        result = error(value)
        print(result)