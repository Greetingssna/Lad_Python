n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} ({n}!) = {factorial}")

print("\nТаблица умножения от 1 до 5:")
for i in range(1,6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()