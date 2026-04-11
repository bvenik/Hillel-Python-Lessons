import threading

def file_word_counter(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            word_counter = 0
            for line in f:
                words = line.split()
                word_counter += len(words)
            print(f"Кількість слів у '{filename}': {word_counter}")
            return word_counter
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено!")


t1 = threading.Thread(target=file_word_counter, args=('lesson12_test.txt',))
t2 = threading.Thread(target=file_word_counter, args=('lesson12_test_2.txt',))

t1.start()
print('Старт потоку для 1-го файлу')

t2.start()
print('Старт потоку для 2-го файлу')

t1.join()
t2.join()

print("Усі потоки завершили роботу.")