def my_func(a, b):
    c = a
    for i in range(abs(b)-1):
        a = c*a
    return 1/a


print(my_func(2, -4))
