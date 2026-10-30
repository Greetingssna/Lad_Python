try:
    age = int(input("Введите ваш возраст "))

    if age < 0 or age > 150:
        print("Ошибка. Неккоректный возраст. Введите число от 0 до 150")
    elif 0 <= age <= 12:
        print("Ребенок")
    elif 13 <= age <= 17:
        print("Подросток")
    elif 18 <= age <= 64:
        print("Взрослый")
    else:
        print("Пенсионер")

except ValueError:
    print("Ошибка. Введите целое число цифрами")