# Урок 1, задание 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

val = int(input('Введите число\n'))
#print(max(map(int, ''.join(val))))

max = 0
new_val = val

if val < 10:
    max = val
else:
    while new_val // 10 != 0:
        if max == 9:
            break

        tmp = new_val % 10
        new_val = (new_val - tmp) / 10
        if tmp > max:
            max = tmp
        if new_val < 10:
            if new_val > max:
                max = new_val

print('Самая большая цифра: ' + str(int(max)))
