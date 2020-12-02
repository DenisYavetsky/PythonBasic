# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой


def custom_user(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name}\nФамилия: {lastname}\nГод рождения: {year_of_birth}\nГород проживания: '
                 f'{city}\nEmail: {email}\nТелефон: {phone}\n')


custom_user(name=input('Имя: '), lastname=input('Фамилия: '), year_of_birth=input('Год Рождения: '),
            city=input('Город проживания: '), email=input('email: '), phone=input('phone: '))
