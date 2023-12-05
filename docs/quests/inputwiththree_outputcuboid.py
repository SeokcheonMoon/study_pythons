num_first, num_second, num_third = input().split()

first = int(num_first)
second = int(num_second)
third = int(num_third)
fourth = first * second * third
print("가로({})m * 세로({}) * 높이({}) = 직육면체({})m^3".format(first,second,third,fourth))