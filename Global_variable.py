import Image_initialization as Ii

name = ""  # Example output "Максим"
tasks_type = ""  # Example output "Квадратные уравнения"
count_tasks = 0  # Example output 5
general_task_dict = {"Линейные уравнения": {0: {0},
                                            1: {14},
                                            2: {0},
                                            3: {0.5},
                                            4: {-3}
                                            },
               "Квадратные уравнения": {0: {-2, 1},
                                        1: {9, -11},
                                        2: {0, 7},
                                        3: {13, 4},
                                        4: {5},
                                        5: {8, 2},
                                        6: {-9, 7}
                                        }
                     }
officer_task_dict = {}  # Example output {1: (1, {14}), 2: (2, {0}), 3: (4, {-3}), 4: (3, {0.5}), 5: (0, {0})}
exercise = {"Линейные уравнения": Ii.get_label_exercise_1_image(),
            "Квадратные уравнения": Ii.get_label_exercise_1_image()
            }
answer = {}  # Example output {1: '1, -2', 2: '9, -11', 3: '-9, 7', 4: '5', 5: '0, 7', 6: '2, 16/2', 7: '13, 4'}
counter = 1
result = []  # Example output [1, 0, 1, 1, 1, 0]
er_wg_comment = "Wrong answer or writing"
true_in_a_row = 0  # The number of correct responses in a row

# Block "Label congratulations on new record"
new_record_flag = False  # Has the record been broken or not?
old_true_in_a_row = 0  # The number of correct responses in a row

columns = ("number", "your answer", "true answer")
columns_all_result = ("score_id", "name_student", "topic_of_test", "abs_and_all_quantity", "ratio", "result")
columns_max_result = ("max_score_id", "name_student", "topic_of_test", "max_result")
