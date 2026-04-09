import re


def validate_name() -> str:
    """
    Запитує ПІБ користувача та валідує його за допомогою регулярного виразу.
    :return: Валідований рядок з ПІБ.
    """
    word = r"[A-Za-zА-Яа-я']+"
    pattern = rf"^{word}\s{word}\s{word}$"

    while True:
        name = input("Введіть ваше ПІБ: ").strip()
        if re.fullmatch(pattern, name):
            return name
        print("Помилка! ПІБ має містити три слова та лише літери (без цифр та знаків).")


username = validate_name()
print(f"ПІБ '{username}' успішно валідовано!")
