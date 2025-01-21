import global_variable as gv
import functions.db_handlers as dbh


def finish(win):
    win.destroy()  # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')


def answer_handler(answer_dict, task_dict):
    for index in range(1, gv.count_tasks + 1):
        answer = answer_dict[index].split(",")  # The answer to the task numbered index
        processed_answer = set()
        true_answer = task_dict[index][1]
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
                        x = (-1) * (abs(int(x[0])) + int(x[1][0]) / int(x[1][1]))
                    else:
                        x = int(x[0]) + int(x[1][0]) / int(x[1][1])
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
                dbh.errors_and_wrong_update(score_id=dbh.get_new_score_id(), task_id=task_dict[index][0],
                                        student_answer=answer_dict[index], true_answer=", ".join(map(str, list(true_answer))),
                                        comment=gv.er_wg_comment)
                continue
        gv.result.append(0)

        # Add information about error or wrong answer
        dbh.errors_and_wrong_update(score_id=dbh.get_new_score_id(), task_id=task_dict[index][0],
                                student_answer=answer_dict[index], true_answer=", ".join(map(str, list(true_answer))),
                                comment=gv.er_wg_comment)


#answer_handler({1: '-11.5, 9', 2: "0", 3: "-3"}, {1: ('x**2 + 2*x - 99 = 0', {-11.5, 9}), 2: ("x = 4", {0}), 3: ("x = 3", {-3})})
#print("Результат:", gv.result)


def get_true_in_a_row(iter_answer: list[int]):
    m = 0
    current = 0
    for i in iter_answer:
        if i == 1:
            current += 1
        else:
            if current > m:
                m = current
            current = 0

    gv.true_in_a_row = m
