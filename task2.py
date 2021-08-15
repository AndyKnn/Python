# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.Реализовать
# вывод данных о пользователе одной строкой.

def my_func(
        name: str = None,
        surname: str = None,
        year_of_birth: int = None,
        city: str = None,
        email: str = None,
        phone: str = None
):
    print(f"{name} {surname}, год рождения: {year_of_birth}, город проживания: {city}, email:{email}, телефон:{phone}")


user_name = input("Наберите имя >>> ")
user_surname = input("Наберите фамилию >>> ")
user_year_of_birth = int(input("год рождения >>> "))
user_city = input("город проживания >>> ")
user_email = input("email >>> ")
user_phone = input("номер телефона >>> ")

my_func(user_name, user_surname, user_year_of_birth, user_city, user_email, user_phone)
