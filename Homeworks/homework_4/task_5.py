def check_email(email):
    # символ @ встречается ровно один раз
    if email.count("@") != 1:
        return False

    # Разделяем e-mail на две части
    parts = email.split("@")
    name = parts[0]
    domain = parts[1]

    if name.strip() == "" or domain.strip() == "":
        return False

    # Проверка наличия точки
    if "." not in domain:
        return False

    suffix = domain.split(".")[-1]

    if len(suffix) < 2 or not suffix.isalpha():
        return False
    return True

# Проверка номера телефона
def check_phone(phone):
    parts = phone.split("-")

    if len(parts) != 5:
        return False

    if parts[0] != "+7":
        return False

    if len(parts[1]) != 3 or not parts[1].isdigit():
        return False

    if len(parts[2]) != 3 or not parts[2].isdigit():
        return False

    if len(parts[3]) != 2 or not parts[3].isdigit():
        return False

    if len(parts[4]) != 2 or not parts[4].isdigit():
        return False

    return True

emails = [
    "student@gmail.com",
    "test@mail.ru",
    "userexample.com",
    "user@@mail.com",
    "@gmail.com",
    "user@mail",
    "user@mail.c"
]

print("Проверка e-mail:")

for email in emails:
    print(f"{email}: {check_email(email)}")

print("-" * 40)

phones = [
    "+7-999-123-45-67",
    "+7-123-456-78-90",
    "8-999-123-45-67",
    "+7-99-123-45-67",
    "+7-999-abc-45-67",
    "+7-999-123-456-67"
]

print("Проверка телефонов:")

for phone in phones:
    print(f"{phone}: {check_phone(phone)}")