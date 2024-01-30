# 압축된 for 문
numerics = [0, 1, 2, 3, 4]
numerics_list = []
for number in numerics : 
    result = number + 2
    numerics_list.append(result)
    pass
print(numerics_list)

print([number+2 for number in numerics])