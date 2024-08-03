import sqlite3
from random import sample, choice

db = sqlite3.connect('Math_simulator_database.db')
c = db.cursor()

# Создание базы данных
c.execute('PRAGMA foreign_keys = ON;')
c.execute('''CREATE TABLE IF NOT EXISTS student (
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name_student VARCHAR(50)
);''')
c.execute('''CREATE TABLE IF NOT EXISTS max_score (
max_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
max_result INTEGER,
FOREIGN KEY (student_id)
REFERENCES student(student_id)
ON DELETE CASCADE
);''')
c.execute('''CREATE TABLE IF NOT EXISTS score (
score_id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
result INTEGER,
FOREIGN KEY (student_id)
REFERENCES student(student_id)
ON DELETE CASCADE
);''')

# Код математического тренажера

# Константы, функции
d = {'x + 1 = 1': '0',
     'x - 5 = 9': '14',
     '2x + 1 = 1': '0',
     '4x - 1 = 1': '0.5',
     'x + 2 = -1': '-3',}
name_table = {'student': 'Студент',
              'max_score': 'Максимальный результат',
              'score': 'Все результаты'}
cond = ['Молодец!', 'Верно!', 'Правильно!', 'Так точно!']
total = 0

def task_input(st):
    a = input(st)
    if a.isdigit():
        a = int(a)
        if a > len(d):
            return task_input(f'Количество задач не должно превышать {len(d)}. Напишите ещё раз: ')
        elif a <= 0:
            return task_input(f'Количество задач не должно быть меньше 1. Напишите ещё раз: ')
        else:
            return a
    else:
        return task_input(f'Количество задач должно быть числом. Напишите ещё раз: ')
def name_input(name):
    name = input(name).strip()
    if len(name) == 0:
        return name_input('Имя не должно быть пустым. Пожалуйста, напишите ещё раз: ')
    return name
def print_table(*tables):
    print()
    for table, n in tables:
        print(f'Таблица: {name_table[n]}')
        for i in table:
            print(*list(map(lambda x: str(x).ljust(7), i)))
            print()

# Ввод информации от пользователя
username = name_input('Как вас зовут?\n')
print(f'Сколько задач вы хотите? Всего есть {len(d)}')
count_tasks = task_input('Количество: ')
l = sample(list(d.keys()), count_tasks)

print()

# Вывод и решение задач
for i in range(len(l)):
    print(f'Задача номер {i + 1}', l[i], sep='\n')
    if input('Ваш ответ: ').strip() == d[l[i]]:
        total += 1
        print(choice(cond))
    else:
        print(f'Неправильно, верный ответ - это {d[l[i]]}')
    print()

# Вывод результата
python_result = round(total / count_tasks, 2)
print(f'Ваш результат: {python_result}')

# Занесение информации о пользователе в базу данных
if username in map(lambda x: x[0], c.execute('SELECT name_student FROM student;')):
    c.execute('''INSERT INTO score (student_id, result)
                       VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?
                       );
                       ''', (username, python_result))
    old_per = float(c.execute('''SELECT max_result FROM max_score
                           WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?);
                           ''', (username, )).fetchone()[0])
    new_per = python_result
    if new_per > old_per:
        print('*' * 40, '   Поздравляю! Вы побили свой рекорд!', '*' * 40, sep='\n')
        c.execute('''UPDATE max_score
                     SET max_result = ?
                     WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?);
                     ''', (new_per, username))
else:
    c.execute('''INSERT INTO student (name_student)
                 VALUES (?
                 );
                 ''', (username, ))
    c.execute('''INSERT INTO max_score (student_id, max_result)
                       VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?
                       );
                       ''', (username, python_result))
    c.execute('''INSERT INTO score (student_id, result)
                       VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?
                       );
                       ''', (username, python_result))

# Проверка базы данных для разработчика
c.execute('''SELECT * FROM student;''')
table1 = (c.fetchall(), 'student')
c.execute('''SELECT * FROM max_score ORDER BY max_result DESC;''')
table2 = (c.fetchall(), 'max_score')
c.execute('''SELECT * FROM score;''')
table3 = (c.fetchall(), 'score')
print_table(table1, table2, table3)




# Завершение работы
db.commit()
db.close()
