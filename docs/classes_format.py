# class 기본구조

class Class_name : 
    def __init__(self) : #class를 사용하면 __init__ 라고 하는 function을 자동적으로 가지고 있음. : class 생성자라고 함. - class의 모든 자원들을 return값으로 함.(그래서 return필요 X)
        pass                

    def function_name(self) : #class 안에 있는 function 에는 self 키워드가 필요.-class 소속 확인용.
        pass
        return 0
    
# class 순서
# 1. import -------------------같은 파일에 있을 경우 생략
# 2. clsss instance (생성자 호출)
# 3. call function (원하는 function 호출)

class Person : 
    def __init__(self) :
        pass

    def add_age(self) :
        pass
        print("45세")
        return 0
    
#class를 변수지정하고
person = Person() #================> 변수에 담아야함.
#class의 function을 호출
person.add_age() #============> class + . + function 구조

####################################################################################

#사칙연산 class 만들기


class Arithmetics : 
    
    def __init__(self) :
        pass    

    def add(self, first, second) :          
        sum = first + second
        return sum

    def minus(self, first, second) :
        result = first - second
        return result
    
    def multiply(self, first, second) :
        answer = first * second
        return answer

    def division(self, first, second) :
        value = first / second
        return value


# class 순서
# 1. import -------------------같은 파일에 있을 경우 생략
# 2. clsss instance (생성자 호출)--- 이 단계에서 변수로 정해주자.
arithmetics = Arithmetics()
# 3. call function (원하는 function 호출) 
print(arithmetics.add(5,6))
print