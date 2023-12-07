# 기본 function 형식 - 기다림. 불리울때 기능한다.-----------------우리가 코드를 만들어서 function 기능을 wrapping하는거라 생각하면 됨.
def functions() :
    pass
    return 0

## 그냥 연습
def my_function() :
  print("Hello from a function")

my_function()
pass

str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
print(str_anyone)

str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
print(str_anyone)

# 문항 1과 답항을 출력하는 function-------------------------------하나의 파일에는 fucntion 이름이 중독 되어서는 안됩니다

def print_question_and_answer() :
    str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
    print(str_anyone)

    str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
    print(str_anyone)
    return 0

print_question_and_answer()

