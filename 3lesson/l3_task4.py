posts = [
    "Спутникстроение",
    "Циклы в Python",
    "Мир животных",
]

print("Свежие посты: ")
for number, title in enumerate(posts, start=1):
    print(f"{number} {title}")

print("\nКарточка статьи") #\n - перенос строки
for title in posts:
    print(f"{title} - {len(title)} символов")

print("\nПоиск")
if "Мир животных" in posts:
    print("Пост про 'Мир животных' есть в списке")
else:
    print("Такой статьи нет")

