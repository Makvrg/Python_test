import global_variable as gv
import sqlite3


def get_new_score_id():
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    new_score_id = c.execute('''SELECT seq FROM sqlite_sequence
                                WHERE name = 'score';''').fetchone()[0] + 1

    db.commit()
    db.close()

    return new_score_id


def errors_and_wrong_update(*, score_id, task_id, student_answer, true_answer, comment):
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    c.execute('''INSERT INTO errors_and_wrong (score_id, task_id, student_answer, true_answer, comment)
    VALUES (?, ?, ?, ?, ?)
        ;''', (score_id, task_id, student_answer, true_answer, comment))

    db.commit()
    db.close()


def create_database():  # Create database
    db = sqlite3.connect(gv.database_abs_path)
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
    c.execute('''CREATE TABLE IF NOT EXISTS errors_and_wrong (
        errors_and_wrong_id INTEGER PRIMARY KEY AUTOINCREMENT,
        score_id INTEGER NOT NULL,
        task_id INTEGER,
        student_answer TEXT,
        true_answer TEXT,
        comment TEXT,
        FOREIGN KEY (score_id)
        REFERENCES score(score_id)
        ON DELETE CASCADE
        );''')

    db.commit()
    db.close()


def database_update(*, name_student, topic_of_test, abs_quantity, all_quantity, ratio, result):
    db = sqlite3.connect(gv.database_abs_path)
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
                #print("gv.old_true_in_a_row", gv.old_true_in_a_row, type(gv.old_true_in_a_row))
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
    db = sqlite3.connect(gv.database_abs_path)
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


def print_table():  # For developer (can using in Task.py)
    db = sqlite3.connect(gv.database_abs_path)
    c = db.cursor()

    print()
    for t_name in gv.name_table:
        c.execute(f'''SELECT * FROM {t_name};''')

        print(f'Таблица: {t_name}')

        for i in c.fetchall():
            print(*list(map(lambda x: str(x).ljust(9), i)))
            print()

    db.commit()
    db.close()


def get_rows(treeview_name):  # treeview_name is an "all_result_table" or "max_result_table"
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
