# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translate = {'One': 'Один',
             'Two': 'Два',
             'Three': 'Три',
             'Four': 'Четыре'}

with open('files/file4.txt', 'r', encoding='UTF-8') as file1, open('files/file4-1.txt', 'w', encoding='UTF-8') as file2:
    for line in file1.readlines():
        for k, v in translate.items():
            if k in line:
                new_line = line.replace(k, v)
                file2.write(new_line)

