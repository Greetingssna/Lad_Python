def build_slug(title: str) -> str:

    result = title.lower()

    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip("-")

    return result

posts = [
    "Изучаем Python с нуля",
    "Как создать сайт на Django",
    "Основы программирования на Python",
    "Работа с базами данных",
    "Python для начинающих",
    "Создание первого проекта"
]

print("Посты о Python:")

for title in posts:
    if "Python" in title:
        print(f"Заголовок: {title}")
        print(f"Slug: {build_slug(title)}")
        print("-" * 40)