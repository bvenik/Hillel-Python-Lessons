import string


def count_specific_words(text: str, target_words: list[str]) -> dict[str, int]:
    """
    Підраховує кількість повторень лише заданих слів у тексті.

    :param text: Вхідний текст для аналізу.
    :param target_words: Список слів, які потрібно знайти.
    :return: Словник, де ключ — цільове слово, а значення — кількість його повторів.
    """
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, "")

    words_list = text.split()
    word_count: dict[str, int] = {}

    for target in target_words:
        target_lower = target.lower()
        word_count[target] = words_list.count(target_lower)

    return word_count


input_text = 'Python, Pythom, Pyton, python, Python, Puton, Пітон'
search_list = ['Python', 'Pyton']

result = count_specific_words(input_text, search_list)

print("Результат пошуку:")
for word, count in result.items():
    print(f"Слово '{word}' зустрічається {count} разів")