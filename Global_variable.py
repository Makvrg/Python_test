import Image_initialization as Ii

name = ""  # Example output "Максим"
tasks_type = ""  # Example output "Квадратные уравнения"
count_tasks = 0  # Example output 5
general_task_dict = {"Линейные уравнения": {"x + 1 = 1": {0},
                                      "x - 5 = 9": {14},
                                      "2x + 1 = 1": {0},
                                      "4x - 1 = 1": {0.5},
                                      "x + 2 = -1": {-3}
                                            },
               "Квадратные уравнения": {"x**2 + x - 2 = 0": {-2, 1},
                                        "x**2 + 2*x - 99 = 0": {9, -11},
                                        "x**2 - 7*x = 0": {0, 7},
                                        "x**2 - 17*x + 52 = 0": {13, 4},
                                        "x**2 - 10*x + 25 = 0": {5},
                                        "x**2 - 10*x + 16 = 0": {8, 2},
                                        "- x**2 - 2*x + 63 = 0": {-9, 7}
                                        }
                     }
officer_task_dict = {}  # Example output {1: ('2x + 1 = 1', {0}), 2: ('x + 2 = -1', {-3}), 3: ('x + 1 = 1', {0})}
exercise = {"Линейные уравнения": Ii.get_label_exercise_1_image(),
            "Квадратные уравнения": Ii.get_label_exercise_1_image()
            }
answer = {}  # Example output {1: '1, -2', 2: '9, -11', 3: '-9, 7', 4: '5', 5: '0, 7', 6: '2, 16/2', 7: '13, 4'}
counter = 1
result = []  # Example output [1, 0, 1, 1, 1, 0]
true_in_a_row = 0  # The number of correct responses in a row

# Block "Label congratulations on new record"
new_record_flag = False  # Has the record been broken or not?
old_true_in_a_row = 0  # The number of correct responses in a row

columns = ("number", "your answer", "true answer")
columns_all_result = ("score_id", "name_student", "topic_of_test", "abs_and_all_quantity", "ratio", "result")
columns_max_result = ("max_score_id", "name_student", "topic_of_test", "max_result")
