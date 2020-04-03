def my_func(a,b,c):
    my_list = [a, b, c]
    Max_1 = max(my_list)
    my_list.remove(max(my_list))
    Max_2 = max(my_list)
    return Max_1 + Max_2


print(my_func(4, 6, 7))
