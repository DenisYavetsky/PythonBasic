# Урок 1, задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

num_seconds = int(input('Введите время в секундах\n'))
if num_seconds >= 0 and num_seconds < 360000:
    hours = num_seconds // 3600
    minutes = num_seconds % 3600 // 60
    seconds = num_seconds % 3600 % 60

    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)

    print('{}:{}:{}'.format(hours, minutes, seconds))
else:
    print('Для такого числа представить время в формате "чч:мм:сс" невозможно')
