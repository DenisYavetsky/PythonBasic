# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def create_file():
    ''' создает файл с набором чисел через пробел '''
    with open('files/file5.txt', 'w', encoding='UTF-8') as f:
        nabor_chisel = '1 4 5 7 234 657 1 24 6 7 56  87 67 68 8 78 677'
        f.write(nabor_chisel)


def calculate(file):
    ''' считает сумму из чисел в файле '''
    with open(file, 'r', encoding='UTF-8') as f:
        r = f.read()
        s = sum(map(int, r.split()))
    return s


if __name__ == '__main__':
    create_file()
    print(calculate('files/file5.txt'))







