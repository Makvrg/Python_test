from typing import Dict, Set, Any, Tuple, List
from pathlib import Path


name: str  # Example output "Максим"
tasks_type: str  # Example output "Квадратные уравнения"
count_tasks: int  # Example output 5
officer_task_dict: Dict[int, Tuple[int, str, Set[Any]]]  # Example output
exercise = {"Линейные уравнения": "Решите уравнение в действительных числах:",
            "Квадратные уравнения": "Решите уравнение в действительных числах:"
            }

# Blok database work
database_abs_path: Path  # Example output 'C:\Users\Mi\PycharmProjects\Math_train\math_simulator_database.db'
db_names = {"Линейные уравнения": "task_linear_equations",
            "Квадратные уравнения": "task_quadratic_equations"}

explanation = 'Записывайте по образцу: несколько ответов "12, -6", \nдесятичные дроби "1.21", обыкновенные дроби "5/4" и смешанные дроби "11 3/4"'
answer: Dict[int, str] = {}  # Example output {1: '0', 2: '56, 8', 3: '0, 1 4/5', 4: '-3', 5: '14'}
counter: int = 1
result: List[int] = []  # Example output [1, 0, 1, 1, 1, 0]
er_wg_comment = "Wrong answer or writing"
true_in_a_row: int = 0  # The number of correct responses in a row

# Block "Label congratulations on new record"
new_record_flag: bool = False  # Has the record been broken or not?
old_true_in_a_row: int = 0  # The number of correct responses in a row

# Block "Columns"
columns_result = ("number", "your answer", "true answer")
columns_all_result = ("score_id", "name_student", "topic_name", "abs_and_all_quantity", "ratio", "in_a_row", "date")
columns_max_result = ("max_score_id", "name_student", "topic_name", "in_a_row", "date")
