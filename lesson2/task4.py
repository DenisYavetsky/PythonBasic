# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове

s = input('Введите строку разделенную пробелами: ')
words = s.split()

i = 1

for word in words:
    print(i, word[:10] + '...' if len(word) > 10 else word)
    i = i + 1