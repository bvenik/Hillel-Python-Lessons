import sqlite3

db_connection = None

try:
    db_connection = sqlite3.connect('../lesson13/students_list.db')
    cursor = db_connection.cursor()
    print("З'єднання з SQLite відкрито")

    # Створюємо таблицю
    create_table_query = '''CREATE TABLE IF NOT EXISTS students \
                            ( \
                                id \
                                INTEGER \
                                PRIMARY \
                                KEY \
                                AUTOINCREMENT, \
                                first_name \
                                TEXT \
                                NOT \
                                NULL, \
                                last_name \
                                TEXT \
                                NOT \
                                NULL, \
                                age \
                                INTEGER, \
                                phone \
                                TEXT, \
                                email \
                                TEXT
                            );'''
    cursor.execute(create_table_query)

    # Дані для вставки
    new_students = [
        ('Олександр', 'Ковальчук', 16, '+380671112233', 'oea_ko@gmail.com'),
        ('Марія', 'Шевченко', 17, '+380504445566', 'm6sha@gmail.com'),
        ('Олександр', 'Матросов', 16, '+380937778899', 'sasha12034@gmail.com'),
        ('Анна', 'Мельник', 16, '+380682223344', 'melanna@gmail.com'),
        ('Максим', 'Бондаренко', 17, '+380955556677', 'bondarenkomax@gmail.com')
    ]

    insert_query = '''INSERT INTO students (first_name, last_name, age, phone, email)
                      VALUES (?, ?, ?, ?, ?);'''

    cursor.executemany(insert_query, new_students)
    db_connection.commit()

    print(f"Запис успішно вставлено. Додано рядків: {cursor.rowcount}")

    # --- ОСЬ ЦЕЙ БЛОК ПОКАЖЕ ТОБІ ДАНІ ---
    print("\nПоточний вміст бази даних:")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    # -------------------------------------

except sqlite3.Error as error:
    print("Помилка при роботі з SQLite:", error)

finally:
    if db_connection:
        db_connection.close()
        print("З'єднання з SQLite закрито")