num_weight, num_tall = input().split()

weight = int(num_weight)
tall = int(num_tall)*0.01

BMI = weight / tall**2

print("({})kg / ({})m^2=({})".format(weight,tall,BMI))

if BMI < 18 :
    pass
    print("{}은 저체중입니다".format(BMI))
elif 18<= BMI <= 22 :
    pass
    print("{}은 정상입니다".format(BMI))
elif 23<= BMI <=24 :
    pass
    print("{}은 과체중입니다".format(BMI))
else : 
    pass
    print("{}은 비만입니다".format(BMI))
print("End Program!")