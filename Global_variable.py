name = None
tasks_type = None
count_tasks = 3
task_list = None
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
sergeant_task_list = None
exercise = {"Линейные уравнения": "Решите уравнение в действительных числах:",
            "Квадратные уравнения": "Решите уравнение в действительных числах:"
            }
explanation = "Записывайте по образцу: несколько ответов <<12, -6>>, \nдесятичные дроби <<1.21>>, обыкновенные дроби <<5/4>> и смешанные дроби <<11 3/4>>"
answer = {}  # Example output {1: '1, -2', 2: '9, -11', 3: '-9, 7', 4: '5', 5: '0, 7', 6: '2, 16/2', 7: '13, 4'}
counter = 1
result = 0
columns = ("number", "your answer", "true answer")
