from typing import List, Tuple

'''This is Python objects for inserting all task and topic if the database or table is empty'''

topics: List[Tuple[str]] = [("Линейные уравнения", ), ("Квадратные уравнения", )]

task_linear_equations: List[Tuple[str, str]] = [("x + 1 = 1", "[0]"),
                                                ("x - 5 = 9", "[14]"),
                                                ("2x + 1 = 1", "[0]"),
                                                ("4x - 1 = 1", "[0.5]"),
                                                ("x + 2 = -1", "[-3]")
                                                ]
task_quadratic_equations: List[Tuple[str, ...]] = [("x² + x - 2 = 0", "[-2, 1]"),
                                                        ("x² + 2x - 99 = 0", "[9, -11]"),
                                                        ("x² - 7x = 0", "[0, 7]"),
                                                        ("x² - 17x + 52 = 0", "[13, 4]"),
                                                        ("x² - 10x + 25 = 0", "[5]"),
                                                        ("x² - 10x + 16 = 0", "[8, 2]"),
                                                        ("-x² - 2x + 63 = 0", "[-9, 7]")
                                                        ]