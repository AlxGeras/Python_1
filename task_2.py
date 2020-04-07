my_list = [100, 35, 45, 50, 99]
print(my_list)
new_list = [el for el in my_list if el > my_list[len(my_list)-2]]
print(new_list)
