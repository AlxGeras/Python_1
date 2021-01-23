def my_func(a, b):
    c = a
    if b != 0:
        for i in range(abs(b) - 1):
            a = c * a
    else:
        a = 1
    return 1 / a


print(my_func(2, -1))
