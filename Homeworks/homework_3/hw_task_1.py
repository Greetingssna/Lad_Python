total = int(input("Введите число: "))

print(f"Таблица умножения для числа {total}")

for number in range(1, 10):
    resalt = total * number
    print(f"{total} * {number} = {resalt}")

