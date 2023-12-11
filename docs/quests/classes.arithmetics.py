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

num_first,num_second = input().split()
first = int(num_first)
second = int(num_second)
arithmetics = Arithmetics()

print("{}".format(arithmetics.minus(first,second)))

print("{}".format(arithmetics.multiply(first,second)))

print("{}".format(arithmetics.division(first,second)))