import global_variable as gv
import sqlite3
from typing import Tuple, List, Any, NoReturn
import json
import random


def get_new_score_id() -> int:
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    new_score_id = c.execute('''SELECT seq FROM sqlite_sequence
                                WHERE name = 'score';''').fetchone()[0] + 1

    db.commit()
    db.close()

    return new_score_id


def get_amount_tasks(name_table: str) -> int:
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    name_table = gv.db_names[name_table]

    amount_tasks = c.execute(f'''SELECT COUNT(*) FROM {name_table};''').fetchone()[0]

    db.commit()
    db.close()

    return amount_tasks


def random_tasks():      # Номера могут не начинаться с 1, если были удалены до этого, надо переписать функцию либо придумать новую удобную и быструю систему индексации заданий в базе данных
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    random_ids = random.sample([i for i in range(1, gv.amount_tasks_this_topic + 1)], gv.count_tasks)

    # Receipt random tasks given topic
    c.execute(f'''SELECT * FROM {gv.db_names[gv.tasks_type]}
                      WHERE task_id IN ({random_ids})
                      ;''')


def errors_and_wrong_update(*,
                            score_id: int,
                            task_id: int,
                            student_answer: str,
                            true_answer: str,
                            comment: str) -> NoReturn:

    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    c.execute('''INSERT INTO errors_and_wrong (score_id, task_id, student_answer, true_answer, comment)
    VALUES (?, ?, ?, ?, ?)
        ;''', (score_id, task_id, student_answer, true_answer, comment))

    db.commit()
    db.close()


def create_database() -> NoReturn:  # Create database
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    c.execute('PRAGMA foreign_keys = ON;')

    c.execute('''
        CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_student TEXT
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS topic (
        topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_name TEXT
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS max_score (
        max_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        topic_id INTEGER NOT NULL,
        in_a_row INTEGER,
        date TEXT,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE,
        FOREIGN KEY (topic_id)
        REFERENCES topic(topic_id)
        ON DELETE CASCADE
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS score (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        topic_id INTEGER NOT NULL,
        abs_quantity INTEGER,
        all_quantity INTEGER,
        ratio REAL,
        in_a_row INTEGER,
        date TEXT,
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE,
        FOREIGN KEY (topic_id)
        REFERENCES topic(topic_id)
        ON DELETE CASCADE
        );''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS task_linear_equations (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            task_answer TEXT
            );''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS task_quadratic_equations (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            task_answer TEXT
            );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS errors_and_wrong (
        errors_and_wrong_id INTEGER PRIMARY KEY AUTOINCREMENT,
        score_id INTEGER NOT NULL,
        task_id INTEGER NOT NULL,
        student_answer TEXT,
        true_answer TEXT,
        comment TEXT,
        FOREIGN KEY (score_id)
        REFERENCES score(score_id),
        FOREIGN KEY (task_id)
        REFERENCES task_linear_equations(task_id)
        ON DELETE CASCADE,
        FOREIGN KEY (task_id)
        REFERENCES task_quadratic_equations(task_id)
        ON DELETE CASCADE
        );''')

    check_database(c)

    db.commit()
    db.close()


def check_database(c: sqlite3.Cursor) -> NoReturn:
    """Check database and back-up insertion tasks and topics into the database from admin_file.py if necessary"""
    if c.execute('''SELECT 1 FROM topic LIMIT 1;''').fetchone() is None:
        print("Таблица 'topic' пуста")

        import admin_files.topics as aft

        c.executemany('''
        INSERT INTO topic (topic_name)
        VALUES (?)
        ;''', aft.topics)

    if c.execute('''SELECT 1 FROM task_linear_equations LIMIT 1;''').fetchone() is None:
        print("Таблица 'task_linear_equations' пуста")

        import admin_files.task_linear_equations as afl

        c.executemany('''
                INSERT INTO task_linear_equations (task, task_answer)
                VALUES (?, ?)
                ;''', afl.task_linear_equations)

    if c.execute('''SELECT 1 FROM task_quadratic_equations LIMIT 1;''').fetchone() is None:
        print("Таблица 'task_quadratic_equations' пуста")

        import admin_files.task_quadratic_equations as afq

        c.executemany('''
                        INSERT INTO task_quadratic_equations (task, task_answer)
                        VALUES (?, ?)
                        ;''', afq.task_quadratic_equations)


def insert_data_from_admin(*,
                           table_name: str,
                           list_with_values: List[Tuple[str, ...]]) -> NoReturn:
    """Admin can add new tasks or topics, restore old tasks or old topics of test.
    Need to start program, because required get global_variable.database_abs_path
    For example: insert_data_from_admin(table_name="task_linear_equations", list_with_values=[("999x - 999 = 0", "[1]"), ("x - 999 = 1", "[1000]")])"""

    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    c.executemany(f'''INSERT INTO {table_name}
                      VALUES (NULL, {"?" + ", ?" * (len(list_with_values[0]) - 1)})''', list_with_values)

    db.commit()
    db.close()


def database_update(*,
                    name_student: str,
                    topic_id: int,
                    abs_quantity: int,
                    all_quantity: int,
                    ratio: float,
                    in_a_row: int,
                    date: str) -> NoReturn:

    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    if name_student in map(lambda x: x[0], c.execute('SELECT name_student FROM student;')):
        c.execute('''INSERT INTO score (student_id, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?, ?, ?, ?
                           );
                           ''', (name_student, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date))
        if topic_id in map(lambda x: x[0], c.execute('''SELECT topic_id FROM max_score
                               WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?)
                               ;''', (name_student, ))):
            new_record(c, name_student=name_student, topic_id=topic_id, in_a_row=in_a_row, date=date)

        else:
            c.execute('''INSERT INTO max_score (student_id, topic_id, in_a_row, date)
                                       VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?
                                       );
                                       ''', (name_student, topic_id, in_a_row, date))

    else:
        c.execute('''INSERT INTO student (name_student)
                     VALUES (?
                     );
                     ''', (name_student, ))
        c.execute('''INSERT INTO max_score (student_id, topic_id, in_a_row, date)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?
                           );
                           ''', (name_student, topic_id, in_a_row, date))
        c.execute('''INSERT INTO score (student_id, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?, ?, ?, ?
                           );
                           ''', (name_student, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date))

    db.commit()
    db.close()


def new_record(c: sqlite3.Cursor,
               *,
               name_student: str,
               topic_id: int,
               in_a_row: int,
               date: str) -> NoReturn:
    old_max_in_a_row = int(c.execute('''SELECT in_a_row FROM max_score
                                       WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?) 
                                       AND topic_id = ?
                                       ;''', (name_student, topic_id)).fetchone()[0])
    new_max_in_a_row = in_a_row
    if new_max_in_a_row > old_max_in_a_row:  # New record
        gv.new_record_flag = True
        gv.old_true_in_a_row = old_max_in_a_row

        c.execute('''UPDATE max_score
                                 SET in_a_row = ?, date = ?
                                 WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?) 
                                 AND topic_id = ?;
                                 ''', (new_max_in_a_row, date, name_student, topic_id))


# def table_editor() -> NoReturn:  # Edit database
#     db = sqlite3.connect(gv.database_abs_path)
#     c = db.cursor()
#
#     c.executescript('''
#         ALTER TABLE max_score
#         RENAME TO max_score1;
#         ALTER TABLE student
#         RENAME TO student1;
#         ALTER TABLE score
#         RENAME TO score1;
#
#         CREATE TABLE IF NOT EXISTS student (
#         student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name_student TEXT
#         );
#         INSERT INTO student
#         SELECT * FROM student1;
#
#         CREATE TABLE IF NOT EXISTS max_score (
#         max_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER NOT NULL,
#         max_result REAL,
#         FOREIGN KEY (student_id)
#         REFERENCES student(student_id)
#         ON DELETE CASCADE
#         );
#         INSERT INTO max_score
#         SELECT * FROM max_score1;
#
#         CREATE TABLE IF NOT EXISTS score (
#         score_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER NOT NULL,
#         result REAL,
#         FOREIGN KEY (student_id)
#         REFERENCES student(student_id)
#         ON DELETE CASCADE
#         );
#         INSERT INTO score
#         SELECT * FROM score1;
#         DROP TABLE student1;
#         DROP TABLE max_score1;
#         DROP TABLE score1;''')
#
#     db.commit()
#     db.close()


def print_table() -> NoReturn:  # For developer (can will using in Task.py)
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    print("\nПроверка базы данных\n")
    for t_name in c.execute('''SELECT name FROM sqlite_master;''').fetchall():
        t_name = t_name[0]
        if t_name == "sqlite_sequence": continue
        c.execute(f'''SELECT * FROM {t_name};''')

        print(f'Таблица: {t_name}')

        for i in c.fetchall():
            print(*list(map(lambda x: str(x).ljust(9), i)))
            print()

    db.commit()
    db.close()


def get_rows(treeview_name: str) -> List[Tuple[Any]]:  # treeview_name is an "all_result_table" or "max_result_table"
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    list_rows = []
    if treeview_name == "all_result_table":
        all_rows = c.execute('''SELECT score_id, name_student, topic_of_test, abs_quantity, all_quantity, ratio, result 
                                FROM score JOIN student USING(student_id);''').fetchall()

        # Union for column "Результат" and conversion to percentage column "Качество"
        for row in all_rows:
            list_rows.append(tuple(list(row[0:3]) + [f'{str(row[3])} / {str(row[4])}'] + [f'{round(row[5])}%'] + list(row[6:])))

    elif treeview_name == "max_result_table":
        list_rows = c.execute('''SELECT max_score_id, name_student, topic_of_test, max_result 
                                 FROM max_score JOIN student USING(student_id);''').fetchall()

    db.commit()
    db.close()
    return list_rows
