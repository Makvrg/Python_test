from typing import Dict, Set, Any, Tuple, List
from pathlib import Path


name: str  # Example output "Максим"
tasks_type: Tuple[int, str]  # Example output "Квадратные уравнения"
count_tasks: int  # Example output 5
# general_task_dict: Dict[str, Dict[str, Set[Any]]] = {"Линейные уравнения": {"x + 1 = 1": {0},
#                                             "x - 5 = 9": {14},
#                                             "2x + 1 = 1": {0},
#                                             "4x - 1 = 1": {0.5},
#                                             "x + 2 = -1": {-3}
#                                             },
#                "Квадратные уравнения": {"x² + x - 2 = 0": {-2, 1},
#                                         "x² + 2x - 99 = 0": {9, -11},
#                                         "x² - 7x = 0": {0, 7},
#                                         "x² - 17x + 52 = 0": {13, 4},
#                                         "x² - 10x + 25 = 0": {5},
#                                         "x² - 10x + 16 = 0": {8, 2},
#                                         "-x² - 2x + 63 = 0": {-9, 7}
#                                         }
#                      }
officer_task_dict: Dict[int, Tuple[int, str, Set[Any]]]  # Example output
exercise = {"Линейные уравнения": "Решите уравнение в действительных числах:",
            "Квадратные уравнения": "Решите уравнение в действительных числах:"
            }

# Blok database work
database_abs_path: Path  # Example output 'C:\Users\Mi\PycharmProjects\Math_train\math_simulator_database.db'
db_names = {"Линейные уравнения": "task_linear_equations",
            "Квадратные уравнения": "task_quadratic_equations"}
amount_tasks_this_topic: int

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
columns = ("number", "your answer", "true answer")
columns_all_result = ("score_id", "name_student", "topic_of_test", "abs_and_all_quantity", "ratio", "result")
columns_max_result = ("max_score_id", "name_student", "topic_of_test", "max_result")
