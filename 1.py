# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Игорь'
age = 43
print(name, age)

name = input('Введите имя: ')
print('Привет', name)
age = int(input('Сколько вам лет?: '))
period = 50
age_period = age + period
print('Через', period, 'лет вам будет',  age_period)