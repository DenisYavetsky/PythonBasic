# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('files/file2.txt', 'r', encoding='UTF-8') as f:
    for i, s in enumerate(f.readlines()):
        print(f'В строке "{"".join(s).rstrip()}" {len("".join(s).rstrip())} символов')
    print(f'Всего строк: {i+1}')
