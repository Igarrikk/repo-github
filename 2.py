# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч: мм:сс.Используйте форматирование строк.

second = int(input("Введите время в секундах "))
def convert(sec):
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%03d: %02d: %02d: %02d" % (day, hour, min, sec)
print("Время в формате ддд: чч: мм: сс: ", convert(second))





