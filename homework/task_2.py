is_published = True
is_premium = False
text = "Это мой новый пост"
has_subscription = True

is_text_valid = bool(text)

can_show = is_text_valid and is_published and (not is_premium or has_subscription)

if can_show:
    print("Пост виден")
    print(f"Текст поста: {text} ")
else:
    print("Пост не виден")
