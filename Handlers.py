import Global_variable as gv
#import GUI as gui


def answer_handler(answer_dict, task_dict):
    for index in range(1, gv.count_tasks + 1):
        answer = answer_dict[index].split(",")  # The answer to the task numbered index
        processed_answer = set()
        true_answer = task_dict[index][1]
        for x in answer:  # Set of answer for task
            x = x.strip()
            if x == "":
                continue

            if ("/" not in x) and ("." not in x) and (x.isdigit() or x[0] == "-" and x != "-" and x[1].isdigit()):    # Simple digits
                x = int(x)
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "/" in x and " " in x:  # Mixed fraction
                x = x.split()
                x[1] = x[1].split("/")
                if int(x[0]) < 0:
                    x = (-1) * (abs(int(x[0])) + int(x[1][0]) / int(x[1][1]))
                else:
                    x = int(x[0]) + int(x[1][0]) / int(x[1][1])
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "/" in x and " " not in x:  # Common fraction
                x = x.split("/")
                x = int(x[0]) / int(x[1])
                if x not in true_answer:
                    break
                processed_answer.add(x)

            elif "." in x:  # Decimals
                x = float(x)
                if x not in true_answer:
                    break
                processed_answer.add(x)

        if processed_answer == true_answer and len(processed_answer) == len(true_answer):
            gv.result += 1

#answer_handler({1: '9, -11 1/2', 2: "-0.0", 3: "-3"}, {1: ('x**2 + 2*x - 99 = 0', {-11.5, 9}), 2: ("x = 4", {0}), 3: ("x = 3", {-3})})
#print("     ", gv.result)


# def finish():
#     gui.app.destroy()  # Ручное закрытие окна и всего приложения
#     print('Закрытие приложения')

