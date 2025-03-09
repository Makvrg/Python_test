from typing import Dict, Set, Any, Tuple, List
from pathlib import Path


class User:
    def __init__(self):
        self.name: str  # Example output "Максим"
        self.tasks_type: str  # Example output "Квадратные уравнения"
        self.count_tasks: str  # Example output 5

        self.officer_task_dict: Dict[int, Tuple[int, str, Set[Any]]]  # Example output {1: (1, 'x + 1 = 1', {0}), 2: (3, '2x + 1 = 1', {0}), 3: (4, '4x - 1 = 1', {0.5}), 4: (5, 'x + 2 = -1', {-3}), 5: (7, 'x - 999 = 1', {1000})}
        self.answer: Dict[int, str] = {}  # Example output {1: '0', 2: '56, 8', 3: '0, 1 4/5', 4: '-3', 5: '14'}
        self.result: List[int] = []  # Example output [1, 0, 1, 1, 1, 0]
        self.true_in_a_row: int = 0  # The number of correct responses in a row
        self.new_record_flag: bool = False  # Has the record been broken or not?
        self.old_true_in_a_row: int = 0  # The number of correct responses in a row

context_user: User = User()


class Test:
    def __init__(self):
        # Constants
        self.exercise: Dict[str, str] = {"Линейные уравнения": "Решите уравнение в действительных числах:",
                                    "Квадратные уравнения": "Решите уравнение в действительных числах:"
                                    }
        self.explanation: str = 'Записывайте по образцу: несколько ответов "12, -6", \nдесятичные дроби "1.21", обыкновенные дроби "5/4" и смешанные дроби "11 3/4"'

        # Variables
        self.current_task: int = 1

context_test: Test = Test()


class ForDataBase:
    def __init__(self):
        self.database_abs_path: Path  # Example output 'C:\Users\Mi\PycharmProjects\Math_train\math_simulator_database.db'
        self.db_names: Dict[str, str] = {"Линейные уравнения": "task_linear_equations",
                    "Квадратные уравнения": "task_quadratic_equations"}
        self.short_topic: Dict[str, str] = {"Линейные уравнения": "Лин-ые ур-я",
                                               "Квадратные уравнения": "Квад-ые ур-я"
                                            }

for_data_base: ForDataBase = ForDataBase()


class ColumnsNames:
    def __init__(self):
        self.columns_result: Tuple[str, ...] = ("number", "your answer", "true answer")
        self.columns_all_result: Tuple[str, ...] = ("score_id", "name_student", "topic_name", "abs_and_all_quantity", "ratio", "in_a_row", "date")
        self.columns_max_result: Tuple[str, ...] = ("max_score_id", "name_student", "topic_name", "in_a_row", "date")

columns_names: ColumnsNames = ColumnsNames()


hash_admin_password: bytes = "$2b$12$7STjEQhOc1wMnS6wFPFAjuPM3VhX7kGK/rBD.2EswVEjsrJ.9vt76".encode('utf-8')
