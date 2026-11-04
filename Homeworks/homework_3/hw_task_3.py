grades = [95, 88, 60, 42, 100]

print("Результат оценивания: ")

for grade in grades:
    if grade >= 90:
        verdict = "Отлично"
    elif grade >= 70:
        verdict = "Хорошо"
    elif grade >= 50:
        verdict = "Удовлетворительно"
    else:
        verdict = "Неудовлетворительно"

    print(f"Оценка {grade}: {verdict}")

