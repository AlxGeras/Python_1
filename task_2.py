def user_data(name, surname, date, city, email, phone):
    user_dict = {'name': name, 'surname': surname, 'date': date, 'city': city, 'email': email, 'phone': phone}
    return user_dict


user_dict = user_data(name='Alexander', surname='Gerasimov', city='Bogorodick', date='11.10.1993',
                      email='alxgeras@mail.ru', phone='+79531869845')

result = ''

for key, value in user_dict.items():
    result = result + key + ': ' + value + ', '

print(result)
