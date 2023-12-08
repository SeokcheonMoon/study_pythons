def cal() :
    str_first = input()
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if str_first == "q" :
        return "q"
    for num_second in num_list : 
        pass
        num_first = int(str_first)
        print("{} * {} = {}.".format(num_first,num_second,num_first*num_second))
    print("End program!")

def repeat() :
    while True : 
        number = cal()
        if number == "q" :
            break

repeat()
