total_sum = 0

print("Вводите числа для сложения. Введите 0, чтобы остановиться и узнать сумму.")

while True:
    try:
        number = int(input("Введите число: "))

        if number == 0:
            break
        total_sum += number

    except ValueError:
        print("Ошибка. Введите целое число.")

    print(f"Сумма всез введенных чисел:{total_sum}")