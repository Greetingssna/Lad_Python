users = ["Александр", "Надежда", "Виктория", "Владислав"]
scores = [55, 43, 13]

print("Список участников:")
for number, name in enumerate(users, start=1):
    print(f"{number}. {name}")

print("Результаты по паре: имя, оценка")
for name, score in zip(users, scores):
    print(f"{name}. {score}")
