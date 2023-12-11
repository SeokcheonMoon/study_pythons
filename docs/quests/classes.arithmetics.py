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

arithmetics = Arithmetics()

print("{}".format(arithmetics.minus(5,2)))

print("{}".format(arithmetics.multiply(8,7)))

print("{}".format(arithmetics.division(9,3)))