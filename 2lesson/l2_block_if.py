post_title = "Питоны крутые змеи"
post_text = "Всем привет, как дела?"
is_published = True
is_draft = False

print(f"Пост: {post_title}")


guest_age = int(input("Введите ваш возраст? "))
is_adult_only = True
is_allow_view = True


if is_adult_only:
    # print("Доступ разрешен" if guest_age >= 18 else "Доступ заперещен")
    if guest_age >= 18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
        is_allow_view = False
else:
    print("Ограничений нет")


if is_allow_view:
    if is_published and not is_draft:
        print(f"Текст: {post_text}")
    elif is_draft:
        print("Статья в черновике")
    else:
        print(f"Пост скрыт.")
