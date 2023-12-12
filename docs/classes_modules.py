# (같은 폴더, 다른 파일)에 있는 class and functions 호출

# class 순서

# 1. import -------------------같은 파일에 있을 경우 생략

import classes_format

# 2. clsss instance (생성자 호출)

person = classes_format.Person()
arithmetics = classes_format.Arithmetics()
class_name = classes_format.Class_name()

# 3. call function (원하는 function 호출)

person.add_age()

#############################################################################################################

# import 시 주로 사용하는 방법
from classes_format import Person, Arithmetics, Class_name
person_second = Person()
arithmetics_second = Arithmetics()
class_name_second = Class_name()