import functions.db_handlers as dbh
from typing import Tuple, Set, List, Dict, Any, NoReturn
from datetime import datetime
import json


def finish(win: Any, frame_for_save: Any = None) -> NoReturn:
    if frame_for_save is None:  # Expected application closure
        win.destroy()
    else:  # Intercepting premature program closure
        frame_for_save.save_answer()   #context_user.answer[frame_for_save.context_test.current_task] = (frame_for_save.task_entry.get().strip())  # Save the last answer

        dbh.create_database()

        answer_handler(frame_for_save, frame_for_save.context_user.answer, frame_for_save.context_user.officer_task_dict)  # Getting the value of an attribute context_user.result
        get_true_in_a_row(frame_for_save, frame_for_save.context_user.result)  # Getting the value of an attribute context_user.true_in_a_row

        # Database work
        dbh.database_insert(frame_for_save, name_student=frame_for_save.context_user.name,
                            topic_id=dbh.get_topic_id(frame_for_save.context_user.tasks_type),
                            abs_quantity=sum(frame_for_save.context_user.result),
                            all_quantity=frame_for_save.context_user.count_tasks,
                            ratio=round(sum(frame_for_save.context_user.result) / frame_for_save.context_user.count_tasks * 100, 2),
                            in_a_row=frame_for_save.context_user.true_in_a_row,
                            date=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

        win.destroy()


def answer_handler(frame_object: Any,
                   student_answer_dict: Dict[int, str],
                   of_task_dict: Dict[int, Tuple[int, str, int, Set[Any]]]) -> NoReturn:

    for index in range(1, frame_object.context_user.count_tasks + 1):
        answer = student_answer_dict[index].split(",")  # The answer to the task numbered index
        processed_answer = set()
        true_answer = of_task_dict[index][3]
        er_wg_comment: str = "Wrong answer or writing"
        for x in answer:  # Set of answer for task
            x = x.strip()
            if x == "":
                continue

            elif isinstance(true_answer, str):  # True answer is string
                if x != true_answer:
                    er_wg_comment = "Wrong answer or writing"
                    break
                processed_answer.add(x)

            elif ("/" not in x) and ("." not in x) and (x.isdigit() or (x[0] == "-" and x != "-" and x[1:].isdigit())):  # Simple digits
                try:
                    x = int(x)
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ValueError:
                    er_wg_comment = "ValueError"
                    break
                except TypeError:
                    er_wg_comment = "TypeError"
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
                    er_wg_comment = "ZeroDivisionError"
                    break
                except ValueError:
                    er_wg_comment = "ValueError"
                    break
                except TypeError:
                    er_wg_comment = "TypeError"
                    break

            elif "/" in x and " " not in x:  # Common fraction
                try:
                    x = x.split("/")
                    x = int(x[0]) / int(x[1])
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ZeroDivisionError:
                    er_wg_comment = "ZeroDivisionError"
                    break
                except ValueError:
                    er_wg_comment = "ValueError"
                    break
                except TypeError:
                    er_wg_comment = "TypeError"
                    break
            elif "." in x:  # Decimals
                try:
                    x = float(x)
                    if x not in true_answer:
                        break
                    processed_answer.add(x)
                except ValueError:
                    er_wg_comment = "ValueError"
                    break
                except TypeError:
                    er_wg_comment = "TypeError"
                    break
            else:
                break
        else:
            if processed_answer == true_answer:
                frame_object.context_user.result.append(1)
                continue

            # Add information about error or wrong answer
            else:
                frame_object.context_user.result.append(0)
                if not frame_object.error_data.score_id:
                    frame_object.error_data.score_id = dbh.get_new_score_id()
                    frame_object.error_data.task_and_exercise_id_list = [of_task_dict[index][0]]
                    frame_object.error_data.student_answer_list = [student_answer_dict[index]]
                    frame_object.error_data.true_answer_list = [", ".join(map(str, list(true_answer)))]
                    frame_object.error_data.comment_list=[er_wg_comment]
                else:
                    frame_object.error_data.task_and_exercise_id_list.append(of_task_dict[index][0])
                    frame_object.error_data.student_answer_list.append(student_answer_dict[index])
                    frame_object.error_data.true_answer_list.append(", ".join(map(str, list(true_answer))))
                    frame_object.error_data.comment_list.append(er_wg_comment)

                continue

        frame_object.context_user.result.append(0)

        # Add information about error or wrong answer
        if not frame_object.error_data.score_id:
            frame_object.error_data.score_id = dbh.get_new_score_id()
            frame_object.error_data.task_and_exercise_id_list = [of_task_dict[index][0]]
            frame_object.error_data.student_answer_list = [student_answer_dict[index]]
            frame_object.error_data.true_answer_list = [", ".join(map(str, list(true_answer)))]
            frame_object.error_data.comment_list = [er_wg_comment]
        else:
            frame_object.error_data.task_and_exercise_id_list.append(of_task_dict[index][0])
            frame_object.error_data.student_answer_list.append(student_answer_dict[index])
            frame_object.error_data.true_answer_list.append(", ".join(map(str, list(true_answer))))
            frame_object.error_data.comment_list.append(er_wg_comment)


def admin_answer(str_answer: str) -> str:  # Return serialize answer
    try:
        answer = str_answer.split(",")  # The answer to the task numbered index
        processed_answer = []
        for x in answer:
            x = x.strip()
            if x == "":
                return ""

            elif not all((sml.isdigit() or sml in "/ .-") for sml in x):  # Not digits (is string)
                processed_answer.append(x)

            elif "/" in x and " " in x:  # Mixed fraction
                x = x.split()
                x[1] = x[1].split("/")
                if int(x[0]) < 0:
                    account = (-1) * (abs(int(x[0])) + int(x[1][0]) / int(x[1][1]))
                else:
                    account = int(x[0]) + int(x[1][0]) / int(x[1][1])
                processed_answer.append(account)

            elif "/" in x and " " not in x:  # Common fraction
                x = x.split("/")
                x = int(x[0]) / int(x[1])
                processed_answer.append(x)

            else:
                processed_answer.append(x)

        return json.dumps(processed_answer)

    except ZeroDivisionError:
        return ""
    except ValueError:
        return ""
    except TypeError:
        return ""


def get_true_in_a_row(frame_object: Any,
                      iter_answer: List[int]) -> NoReturn:
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

    frame_object.context_user.true_in_a_row = m
