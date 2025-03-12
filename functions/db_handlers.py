from global_variables import for_data_base
import sqlite3
from typing import Tuple, List, Dict, Set, Any, NoReturn
import json
import random


def get_new_score_id() -> int:
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    new_score_id = c.execute('''SELECT seq FROM sqlite_sequence
                                WHERE name = 'score';''').fetchone()
    if new_score_id is None:
        new_score_id = 1
    else:
        new_score_id = new_score_id[0] + 1

    db.commit()
    db.close()

    return new_score_id


def get_amount_tasks(tasks_type: str) -> int:
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    amount_tasks = c.execute(f'''SELECT COUNT(*) 
                                 FROM task_and_exercise 
                                 JOIN topic USING (topic_id)
                                 WHERE topic_name = ?
                                 ;''', (tasks_type, )).fetchone()[0]

    db.commit()
    db.close()

    return amount_tasks


def get_list_task_id(tasks_type: str) -> List[int]:  # Need for random_tasks()
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    list_task_id = c.execute(f'''SELECT task_and_exercise_id 
                                 FROM task_and_exercise 
                                 JOIN topic USING (topic_id)
                                 WHERE topic_name = ?
                                 ;''', (tasks_type, )).fetchall()

    db.commit()
    db.close()

    list_task_id = list(map(lambda x: x[0], list_task_id))

    return list_task_id


def get_random_tasks_and_exercises(tasks_type: str, count_tasks: int) -> Tuple[Dict[int, Tuple[int, str, int, Set[Any]]], Dict[int, str]]:
    """ -> Tuple[Dict[task_number, Tuple[task_and_exercise_id, task, exercise_id, task_answer], Dict[exercise_id, exercise]] """
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()


    random_ids: List[int] = random.sample(get_list_task_id(tasks_type), count_tasks)

    # Receipt random tasks given topic
    c.execute(f'''SELECT task_and_exercise_id, task, exercise_id, task_answer, exercise_name 
                  FROM task_and_exercise JOIN exercise USING (exercise_id)
                  WHERE task_and_exercise_id IN ({", ".join(["?"] * len(random_ids))})
                  ;''', tuple(random_ids))

    output = c.fetchall()
    random.shuffle(output)  # Extra random subsequence (very need for absolute random!)

    of_task_dict = {}
    exercises_dict = {}
    number = 1

    for row in output:
        of_task_dict[number] = (row[0], row[1], row[2], set(json.loads(row[3])))

        if row[2] not in exercises_dict:
            exercises_dict[row[2]] = row[4]

        number += 1

    db.commit()
    db.close()

    return of_task_dict, exercises_dict


def errors_and_wrong_insert(*,
                            score_id: int,
                            task_and_exercise_id: int,
                            student_answer: str,
                            true_answer: str,
                            comment: str) -> NoReturn:

    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    c.execute('''INSERT INTO errors_and_wrong (score_id, task_and_exercise_id, student_answer, true_answer, comment)
    VALUES (?, ?, ?, ?, ?)
        ;''', (score_id, task_and_exercise_id, student_answer, true_answer, comment))

    db.commit()
    db.close()


def create_database() -> NoReturn:  # Create database
    db = sqlite3.connect(for_data_base.database_abs_path)
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
            ON DELETE CASCADE
            ON UPDATE CASCADE,
            FOREIGN KEY (topic_id)
            REFERENCES topic(topic_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
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
            ON DELETE CASCADE
            ON UPDATE CASCADE,
            FOREIGN KEY (topic_id)
            REFERENCES topic(topic_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS exercise (
            exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_name TEXT
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS task_and_exercise (
            task_and_exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            task TEXT,
            exercise_id INTEGER,
            task_answer TEXT,
            FOREIGN KEY (topic_id) 
            REFERENCES topic(topic_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE,
            FOREIGN KEY (exercise_id)
            REFERENCES exercise (exercise_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS errors_and_wrong (
            errors_and_wrong_id INTEGER PRIMARY KEY AUTOINCREMENT,
            score_id INTEGER NOT NULL,
            task_and_exercise_id INTEGER NOT NULL,
            student_answer TEXT,
            true_answer TEXT,
            comment TEXT,
            FOREIGN KEY (score_id)
            REFERENCES score(score_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
            FOREIGN KEY (task_and_exercise_id)
            REFERENCES task_and_exercise(task_and_exercise_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );''')

    check_database(c)

    db.commit()
    db.close()


def check_database(c: sqlite3.Cursor) -> NoReturn:
    """Check database and back-up insertion tasks and topics into the database from admin_file.py if necessary"""

    import admin_files.topics as aftop
    import admin_files.exercise as afe
    import admin_files.task_linear_equations as afl
    import admin_files.task_quadratic_equations as afq

    for t in aftop.topics:
        c.execute('''INSERT INTO topic (topic_name)
                            SELECT ?
                            WHERE NOT EXISTS (SELECT 1 FROM topic WHERE topic_name = ?)
                            ;''', (t[0], t[0]))

    for e in afe.exercise:
        c.execute('''INSERT INTO exercise (exercise_name)
                         SELECT ?
                         WHERE NOT EXISTS (SELECT 1 FROM exercise WHERE exercise_name = ?)
                         ;''', (e[0], e[0]))

    for l in afl.task_linear_equations:
        c.execute('''
                        INSERT INTO task_and_exercise (topic_id, task, exercise_id, task_answer)
                        SELECT (SELECT topic_id FROM topic WHERE topic_name = 'Линейные уравнения'), ?, 
                        (SELECT exercise_id FROM exercise WHERE exercise_name = 'Решите уравнение в действительных числах:'), 
                        ?
                        WHERE NOT EXISTS (SELECT 1 FROM task_and_exercise 
                        WHERE topic_id = (SELECT topic_id FROM topic WHERE topic_name = 'Линейные уравнения') AND task = ? AND 
                        exercise_id = (SELECT exercise_id FROM exercise WHERE exercise_name = 'Решите уравнение в действительных числах:') 
                        AND task_answer = ?)
                        ;''', (l[0], l[1], l[0], l[1]))

    for q in afq.task_quadratic_equations:
        c.execute('''
                        INSERT INTO task_and_exercise (topic_id, task, exercise_id, task_answer)
                        SELECT (SELECT topic_id FROM topic WHERE topic_name = 'Квадратные уравнения'), ?, 
                        (SELECT exercise_id FROM exercise WHERE exercise_name = 'Решите уравнение в действительных числах:'), 
                        ?
                        WHERE NOT EXISTS (SELECT 1 FROM task_and_exercise 
                        WHERE topic_id = (SELECT topic_id FROM topic WHERE topic_name = 'Квадратные уравнения') AND task = ? AND 
                        exercise_id = (SELECT exercise_id FROM exercise WHERE exercise_name = 'Решите уравнение в действительных числах:') 
                        AND task_answer = ?)
                        ;''', (q[0], q[1], q[0], q[1]))


# Need comment
def insert_task_from_admin(*,
                           tasks_type: str,
                           task_type_is_exist: bool = False,
                           task_exercise: str,
                           task_exercise_is_exist: bool = False,
                           list_with_values: List[Tuple[str, str]] | List[Tuple[str, str, str, str]]) -> NoReturn:
    """Admin can add new tasks or topics, restore old tasks or old topics of test.
    Need to start program, because required get global_variable.database_abs_path

    #########For example: insert_data_from_admin(table_name="task_linear_equations", list_with_values=[("999x - 999 = 0", "[1]"), ("x - 999 = 1", "[1000]")])"""

    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    new_list_with_values = []
    for i in range(len(list_with_values)):
        new_list_with_values[i] = tuple([tasks_type] + [list_with_values[i][0]] + [task_exercise] + [list_with_values[i][1]])
    list_with_values = new_list_with_values
    print("list_with_values", list_with_values)

    if task_type_is_exist is False:
        c.execute('''INSERT INTO topic (topic_name)
                         SELECT ?
                         WHERE NOT EXISTS (SELECT 1 FROM topic WHERE topic_name = ?)
                         ;''', (tasks_type, tasks_type))

    if task_exercise_is_exist is False:
        c.execute('''INSERT INTO exercise (exercise_name)
                                 SELECT ?
                                 WHERE NOT EXISTS (SELECT 1 FROM exercise WHERE exercise_name = ?)
                                 ;''', (task_exercise, task_exercise))

    c.executemany(f'''INSERT INTO task_and_exercise (topic_id, task, exercise_id, task_answer)
                      VALUES ((SELECT topic_id FROM topic WHERE topic_name = ?), ?, 
                      (SELECT exercise_id FROM exercise WHERE exercise_name = ?), ?)
                      ;''', list_with_values)

    db.commit()
    db.close()


def database_insert(frame_object: Any,
                    *,
                    name_student: str,
                    topic_id: int,
                    abs_quantity: int,
                    all_quantity: int,
                    ratio: float,
                    in_a_row: int,
                    date: str) -> NoReturn:

    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    if name_student in map(lambda x: x[0], c.execute('SELECT name_student FROM student;')):
        c.execute('''INSERT INTO score (student_id, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date)
                           VALUES ((SELECT student_id FROM student WHERE name_student = ?), ?, ?, ?, ?, ?, ?
                           );
                           ''', (name_student, topic_id, abs_quantity, all_quantity, ratio, in_a_row, date))
        if topic_id in map(lambda x: x[0], c.execute('''SELECT topic_id FROM max_score
                               WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?)
                               ;''', (name_student, ))):
            new_record(c, frame_object, name_student=name_student, topic_id=topic_id, in_a_row=in_a_row, date=date)

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
               frame_object: Any,
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
        frame_object.context_user.new_record_flag = True
        frame_object.context_user.old_true_in_a_row = old_max_in_a_row

        c.execute('''UPDATE max_score
                                 SET in_a_row = ?, date = ?
                                 WHERE student_id = (SELECT student_id FROM student WHERE name_student = ?) 
                                 AND topic_id = ?;
                                 ''', (new_max_in_a_row, date, name_student, topic_id))


def get_topic_id(name_type: str) -> int:
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    return c.execute('''SELECT topic_id FROM topic WHERE topic_name = ?;''', (name_type, )).fetchone()[0]

    db.commit()
    db.close()


def print_table() -> NoReturn:  # For developer (can will using in Task.py)
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    print("\nПроверка базы данных\n")
    for t_name in c.execute('''SELECT name FROM sqlite_master;''').fetchall():
        t_name = t_name[0]
        if t_name == "sqlite_sequence": continue
        c.execute(f'''SELECT * FROM ?;''', (t_name, ))

        print(f'Таблица: {t_name}')

        for i in c.fetchall():
            print(*list(map(lambda x: str(x).ljust(9), i)))
            print()

    db.commit()
    db.close()


def get_rows(treeview_name: str, topic_id: int | None = None) -> List[Tuple[Any, ...]]:  # treeview_name is an "all_result_table" or "max_result_table" or "wrong_result_table"
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    list_rows: List[Tuple[Any, ...]] = []
    if treeview_name == "all_result_table":
        all_rows1 = c.execute('''SELECT score_id, name_student, topic_name, abs_quantity, all_quantity, ratio, in_a_row, date 
                                FROM score JOIN student USING(student_id)
                                JOIN topic USING(topic_id);''').fetchall()
        # Union for column "Результат", conversion to percentage column "Качество", shortening length name_topic
        for row in all_rows1:
            if row[2] in for_data_base.short_topic:  # If standard type
                list_rows.append(tuple(list(row[0:2]) + [for_data_base.short_topic[row[2]]] + [f'{str(row[3])} / {str(row[4])}'] + [f'{round(row[5])}%'] + list(row[6:])))
            else:  # If admin type
                list_rows.append(tuple(list(row[0:2]) + [row[2]] + [f'{str(row[3])} / {str(row[4])}'] + [f'{round(row[5])}%'] + list(row[6:])))

    elif treeview_name == "max_result_table":
        all_rows2 = c.execute('''SELECT max_score_id, name_student, topic_name, in_a_row, date 
                                 FROM max_score JOIN student USING(student_id)
                                 JOIN topic USING(topic_id);''').fetchall()
        # Shortening length name_topic
        for row in all_rows2:
            if row[2] in for_data_base.short_topic:  # If standard type
                list_rows.append(tuple(list(row[0:2]) + [for_data_base.short_topic[row[2]]] + list(row[3:])))
            else:  # If admin type
                list_rows.append(tuple(list(row[0:2]) + [row[2]] + list(row[3:])))

    elif treeview_name == "wrong_result_table":
        all_rows3 = c.execute(f'''SELECT errors_and_wrong_id, score_id, name_student, topic_name, task, 
                                  student_answer, true_answer, comment 
                                  FROM topic JOIN score USING(topic_id)
                                  JOIN student USING(student_id)
                                  JOIN errors_and_wrong USING(score_id)
                                  JOIN task_and_exercise USING(task_and_exercise_id)
                                  ;''').fetchall()
        # Shortening length name_topic
        for row in all_rows3:
            if row[3] in for_data_base.short_topic:  # If standard type
                list_rows.append(tuple(list(row[0:3]) + [for_data_base.short_topic[row[3]]] + list(row[4:])))
            else:  # If admin type
                list_rows.append(tuple(list(row[0:3]) + [row[3]] + list(row[4:])))

    elif treeview_name == "topic_table":
        all_rows4 = c.execute('''SELECT topic_id, topic_name
                                 FROM topic;''').fetchall()

        list_rows = all_rows4

    elif treeview_name == "task_table":
        all_rows5 = c.execute('''SELECT task_and_exercise_id, task, exercise_name, task_answer
                                 FROM task_and_exercise
                                 JOIN exercise USING(exercise_id)
                                 WHERE topic_id = ?;''', (topic_id, )).fetchall()
        # Parsing with json
        for row in all_rows5:
            list_rows.append(tuple(list(row[0:3]) + ["     " + ", ".join(map(str, json.loads(row[3])))]))

    db.commit()
    db.close()

    return list_rows


def rename_topic(topic_id: int, new_name: str) -> NoReturn:
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    c.execute('''UPDATE topic SET topic_name = ?
                 WHERE topic_id = ?''', (new_name, topic_id))

    db.commit()
    db.close()


def delete_topic(topic_id: int) -> NoReturn:
    db = sqlite3.connect(for_data_base.database_abs_path)
    c = db.cursor()

    c.execute('''DELETE FROM topic
                     WHERE topic_id = ?''', (topic_id, ))

    db.commit()
    db.close()
