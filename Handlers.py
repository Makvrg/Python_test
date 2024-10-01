import Global_variable as gv


def answer_handler(answer_dict, task_dict):
    for i in range(gv.count_tasks):
        if i not in answer_dict:
            continue
        answer = answer_dict[i].replace(",", "").split()
        print(answer)
        true_answer = task_dict[i][1]
        for x in answer:
            if ("/" not in x) or ("." not in x):
                if x not in true_answer:
                    print(78)
                    break

            if "/" in x and " " in x:
                True
answer_handler({1: '13'}, {1: ('x**2 + 2*x - 99 = 0', {'-11', '9'})})



