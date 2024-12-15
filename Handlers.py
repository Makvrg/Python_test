import Global_variable as gv
import sqlite3
from random import sample, choice

#import GUI as gui


def answer_handler(answer_dict, task_dict):
    for index in range(1, gv.count_tasks + 1):
        answer = answer_dict[index].split(",")  # The answer to the task numbered index
        processed_answer = set()
        true_answer = task_dict[index][1]
        for x in answer:  # Set of answer for task
            x = x.strip()
            if x == "":
                continue

            if ("/" not in x) and ("." not in x) and (x.isdigit() or x[0] == "-" and x != "-" and x[1].isdigit()):    # Simple digits
                x = int(x)
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "/" in x and " " in x:  # Mixed fraction
                x = x.split()
                x[1] = x[1].split("/")
                if int(x[0]) < 0:
                    x = (-1) * (abs(int(x[0])) + int(x[1][0]) / int(x[1][1]))
                else:
                    x = int(x[0]) + int(x[1][0]) / int(x[1][1])
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "/" in x and " " not in x:  # Common fraction
                x = x.split("/")
                x = int(x[0]) / int(x[1])
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "." in x:  # Decimals
                x = float(x)
                if x not in true_answer:
                    break
                processed_answer.add(x)

        if processed_answer == true_answer:
            gv.result.append(1)
        else:
            gv.result.append(0)

#answer_handler({1: '9, -11 1/2', 2: "-0.0", 3: "-3"}, {1: ('x**2 + 2*x - 99 = 0', {-11.5, 9}), 2: ("x = 4", {0}), 3: ("x = 3", {-3})})
#print("     ", gv.result)


def get_true_in_a_row(iter_answer):
    count = 0
    m = 0
    a = iter_answer[0]
    if a == 1:
        count += 1
        m = max(m, count)
    if len(iter_answer) == 1:
        gv.true_in_a_row = m
        return None
    for i in range(1, len(iter_answer)):
        a, b = iter_answer[i - 1], iter_answer[i]
        if b == 1:
            count += 1
            m = max(m, count)
        else:
            count = 0
    gv.true_in_a_row = m


#get_true_in_a_row([0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0])
#print(gv.true_in_a_row)


# def finish():
#     gui.app.destroy()  # Ручное закрытие окна и всего приложения
#     print('Закрытие приложения')


def create_database():  # Create database
    db = sqlite3.connect('Math_simulator_database.db')
    c = db.cursor()

    c.execute('PRAGMA foreign_keys = ON;')
    c.execute('''CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_student TEXT
        );''')
    c.execute('''CREATE TABLE IF NOT EXISTS max_score (
        max_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        topic_of_test TEXT,
        max_result INTEGER,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE
        );''')
    c.execute('''CREATE TABLE IF NOT EXISTS score (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        topic_of_test TEXT,
        abs_quantity INTEGER,
        all_quantity INTEGER,
        ratio REAL,
        result INTEGER,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE
        );''')
    db.commit()
    db.close()


def database_update(*, name_student, topic_of_test, abs_quantity, all_quantity, ratio, result):
    db = sqlite3.connect('Math_simulator_database.db')
    c = db.cursor()

    if name_student in map(lambda x: x[0], c.execute('SELECT name_student FROM student;')):
        c.execute('''INSERT INTO score (student_id, topic_of_test, abs_quantity, all_quantity, ratio, result)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?, ?, ?
                           );
                           ''', (name_student, topic_of_test, abs_quantity, all_quantity, ratio, result))
        if topic_of_test in map(lambda x: x[0], c.execute('''SELECT topic_of_test FROM max_score
                               WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?)
                               ;''', (name_student, ))):
            old_max_result = int(c.execute('''SELECT max_result FROM max_score
                                   WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?) 
                                   AND topic_of_test = ?
                                   ;''', (name_student, topic_of_test)).fetchone()[0])
            new_max_result = result
            if new_max_result > old_max_result:  # New record
                gv.new_record_flag = True
                gv.old_true_in_a_row = old_max_result
                print("gv.old_true_in_a_row", gv.old_true_in_a_row, type(gv.old_true_in_a_row))
                c.execute('''UPDATE max_score
                             SET max_result = ?
                             WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?) 
                             AND topic_of_test = ?;
                             ''', (new_max_result, name_student, topic_of_test))
        else:
            c.execute('''INSERT INTO max_score (student_id, topic_of_test, max_result)
                                       VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?
                                       );
                                       ''', (name_student, topic_of_test, result))

    else:
        c.execute('''INSERT INTO student (name_student)
                     VALUES (?
                     );
                     ''', (name_student, ))
        c.execute('''INSERT INTO max_score (student_id, topic_of_test, max_result)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?
                           );
                           ''', (name_student, topic_of_test, result))
        c.execute('''INSERT INTO score (student_id, topic_of_test, abs_quantity, all_quantity, ratio, result)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?, ?, ?
                           );
                           ''', (name_student, topic_of_test, abs_quantity, all_quantity, ratio, result))
    db.commit()
    db.close()


def table_editor():  # Edit database
    db = sqlite3.connect("Math_simulator_database.db")
    c = db.cursor()
    c.executescript('''
        ALTER TABLE max_score
        RENAME TO max_score1;
        ALTER TABLE student
        RENAME TO student1;
        ALTER TABLE score
        RENAME TO score1;

        CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_student TEXT
        );
        INSERT INTO student
        SELECT * FROM student1;

        CREATE TABLE IF NOT EXISTS max_score (
        max_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        max_result REAL,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE
        );
        INSERT INTO max_score
        SELECT * FROM max_score1;

        CREATE TABLE IF NOT EXISTS score (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        result REAL,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE
        );
        INSERT INTO score
        SELECT * FROM score1;
        DROP TABLE student1;
        DROP TABLE max_score1;
        DROP TABLE score1;''')
    db.commit()
    db.close()


def print_table(*tables):
    db = sqlite3.connect("Math_simulator_database.db")
    c = db.cursor()
    name_table = {'student': 'Студент',
                  'max_score': 'Максимальный результат',
                  'score': 'Все результаты'}
    print()
    for table, t_name in tables:
        print(f'Таблица: {name_table[t_name]}')
        for i in table:
            print(*list(map(lambda x: str(x).ljust(7), i)))
            print()


def get_rows(treeview_name):  # treeview_name is a "all_result_table" or "max_result_table"
    db = sqlite3.connect('Math_simulator_database.db')
    c = db.cursor()
    if treeview_name == "all_result_table":
        all_rows = c.execute('''SELECT score_id, name_student, topic_of_test, abs_quantity, all_quantity, ratio, result 
                                FROM score JOIN student USING(student_id);''').fetchall()

        # Union for column "Результат" and conversion to percentage column "Качество"
        list_rows = []
        for row in all_rows:
            list_rows.append(tuple(list(row[0:3]) + [f'{str(row[3])} / {str(row[4])}'] + [f'{round(row[5])}%'] + list(row[6:])))

    elif treeview_name == "max_result_table":
        list_rows = c.execute('''SELECT max_score_id, name_student, topic_of_test, max_result 
                                 FROM max_score JOIN student USING(student_id);''').fetchall()
    db.commit()
    db.close()
    return list_rows


# def finish_test(object):
#     object.destroy()  # Ручное закрытие окна и всего приложения
#     print('Закрытие приложения')




