import global_variable as gv
import functions.db_handlers as dbh
from typing import Tuple, Set, List, Dict, Any, NoReturn
from datetime import datetime


def finish(win: Any, frame_for_save: Any = None) -> None:
    if frame_for_save is None:  # Expected application closure
        win.destroy()
    else:  # Intercepting premature program closure
        gv.answer[gv.counter] = (frame_for_save.task_entry.get().strip())  # Save the last answer

        dbh.create_database()

        answer_handler(gv.answer, gv.officer_task_dict)  # Getting the value of a variable gv.result
        get_true_in_a_row(gv.result)  # Getting the value of a variable gv.true_in_a_row

        # Database work
        dbh.database_update(name_student=gv.name, topic_id=dbh.get_topic_id(gv.tasks_type),
                           abs_quantity=sum(gv.result), all_quantity=gv.count_tasks,
                           ratio=round(sum(gv.result) / gv.count_tasks * 100, 2),
                           in_a_row=gv.true_in_a_row, date=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

        win.destroy()


def answer_handler(student_answer_dict: Dict[int, str],
                   of_task_dict: Dict[int, Tuple[int, str, Set[Any]]]) -> NoReturn:

    for index in range(1, gv.count_tasks + 1):
        answer = student_answer_dict[index].split(",")  # The answer to the task numbered index
        processed_answer = set()
        true_answer = of_task_dict[index][2]
        gv.er_wg_comment = "Wrong answer or writing"
        for x in answer:  # Set of answer for task
            x = x.strip()
            if x == "":
                continue

            if ("/" not in x) and ("." not in x) and (x.isdigit() or x[0] == "-" and x != "-" and x[1].isdigit()):  # Simple digits
                try:
                    x = int(x)
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ValueError:
                    gv.er_wg_comment = "ValueError"
                    break
                except TypeError:
                    gv.er_wg_comment = "TypeError"
                    break

            elif "/" in x and " " in x:  # Mixed fraction
                try:
                    x = x.split()
                    x[1] = x[1].split("/")
                    if int(x[0]) < 0:
                        account = (-1) * (abs(int(x[0])) + int(x[1][0]) / int(x[1][1]))
                    else:
                        account = int(x[0]) + int(x[1][0]) / int(x[1][1])
                    if account not in true_answer:
                        break
                    processed_answer.add(account)
                except ZeroDivisionError:
                    gv.er_wg_comment = "ZeroDivisionError"
                    break
                except ValueError:
                    gv.er_wg_comment = "ValueError"
                    break
                except TypeError:
                    gv.er_wg_comment = "TypeError"
                    break

            elif "/" in x and " " not in x:  # Common fraction
                try:
                    x = x.split("/")
                    x = int(x[0]) / int(x[1])
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ZeroDivisionError:
                    gv.er_wg_comment = "ZeroDivisionError"
                    break
                except ValueError:
                    gv.er_wg_comment = "ValueError"
                    break
                except TypeError:
                    gv.er_wg_comment = "TypeError"
                    break
            elif "." in x:  # Decimals
                try:
                    x = float(x)
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ValueError:
                    gv.er_wg_comment = "ValueError"
                    break
                except TypeError:
                    gv.er_wg_comment = "TypeError"
                    break
            else:
                break
        else:
            if processed_answer == true_answer:
                gv.result.append(1)
                continue
            else:
                gv.result.append(0)
                dbh.errors_and_wrong_update(score_id=dbh.get_new_score_id(), task_id=of_task_dict[index][0],
                                            student_answer=student_answer_dict[index], true_answer=", ".join(map(str, list(true_answer))),
                                            comment=gv.er_wg_comment)
                continue
        gv.result.append(0)

        # Add information about error or wrong answer
        dbh.errors_and_wrong_update(score_id=dbh.get_new_score_id(), task_id=of_task_dict[index][0],
                                    student_answer=student_answer_dict[index], true_answer=", ".join(map(str, list(true_answer))),
                                    comment=gv.er_wg_comment)


#answer_handler({1: '-11.5, 9', 2: "0", 3: "-3"}, {1: ('x**2 + 2*x - 99 = 0', {-11.5, 9}), 2: ("x = 4", {0}), 3: ("x = 3", {-3})})
#print("Результат:", gv.result)


def get_true_in_a_row(iter_answer: List[int]) -> NoReturn:
    m = 0
    current = 0
    for i in iter_answer:
        if i == 1:
            current += 1
        else:
            if current > m:
                m = current
            current = 0
    if current > m:
        m = current

    gv.true_in_a_row = m
