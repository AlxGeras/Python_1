revenue = int(input('Введите выручку фирмы: '))

cost = int(input('Введите издержки фирмы: '))

if revenue > cost:
    print('Финансовый результат фирмы: прибыль')
    profitability = (revenue - cost)/revenue*100
    print('Рентабельность равна: ', '%.2f' % profitability, '%')
    population = int(input('Введите численность сотрудников: '))
    rev_per_pop = (revenue - cost)/population
    print('Прибыль фирмы на одного сотрудника составляет: ', '%.2f' % rev_per_pop)
elif revenue < cost:
    print('Финансовый результат фирмы: убыток')
else:
    print('Финансовый результат фирмы: Нет прибыли')

