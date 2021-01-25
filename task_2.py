my_list = [100, 35, 45, 50, 99]
print(my_list)
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)
