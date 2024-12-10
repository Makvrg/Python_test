from operator import index
import customtkinter as ctk
import Math_simulator_code as ms_code
import Global_variable as gv
import Handlers as hd
from random import sample
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import sqlite3


def finish():
    app.destroy()  # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        self.geometry("1000x700+450+200")
        self.configure(fg_color="#CCFFCC")

        # Theme and mode setting
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("system")

        self.main_frame = ctk.CTkFrame(self, border_width=15, border_color="#006600",
                                       fg_color="#FFFFFF", corner_radius=30)
        self.main_frame.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)
        self.hallo_label = ctk.CTkLabel(self.main_frame, text="Добро пожаловать в математический тренажер",
                                        font=("Arial", 37, "bold"), fg_color="#FFFFFF", text_color="#000000")
        self.hallo_label.pack(side="top", pady=60)
        self.go_button = ctk.CTkButton(self.main_frame, command=self.goto_info, text="Начать",
                                       fg_color="#009900", height=100, width=400, font=("Arial", 70, "bold"),
                                       border_width=3, border_color="#006600", corner_radius=5,
                                       text_color="#FFFFFF", hover_color="#007D00")
        self.go_button.pack(side="bottom", pady=150)

    def goto_info(self):
        self.main_frame.destroy()
        self.info_frame = InfoFrame(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        for i in range(1, 4):
            self.rowconfigure(index=i, weight=10000)
        self.rowconfigure(index=4, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Create widgets
        self.info_label = ctk.CTkLabel(self, text="Заполните все поля", height=45, corner_radius=10,
                                       width=390, font=("Arial", 35, "bold"), fg_color="#ff9191", text_color="#000000")
        self.info_label.grid(row=0, column=0, sticky="sw", padx=30, pady=[30, 13])

        self.name_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.name_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=5)
        self.name_label = ctk.CTkLabel(self.name_frame, text="Напишите свое имя", font=("Arial", 30),
                                       text_color="#737373")
        self.name_label.pack(anchor="nw", padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(self.name_frame, font=("Arial", 35), width=500, height=60,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.name_entry.bind("<KeyRelease>", self.get_name)
        self.name_entry.pack(side="left", anchor="nw", padx=10)
        self.name_entry.insert(0, "Максим")

        self.name_error = ctk.CTkLabel(self.name_frame, text="",
                                       font=("Arial", 20), text_color="#ff5757")
        self.name_error.pack(side="left", anchor="nw", padx=10, pady=7)

        self.type_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.type_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=5)
        self.type_label = ctk.CTkLabel(self.type_frame, text="Выберете тип задач", font=("Arial", 30),
                                       text_color="#737373")
        self.type_label.pack(anchor="nw", padx=10, pady=8)
        self.type_combobox = ctk.CTkComboBox(self.type_frame, hover=True, font=("Arial", 35), width=450, height=60,
                                             fg_color="#FFFFFF", text_color="#212121", border_color="#818c81",
                                             button_color="#818c81", button_hover_color="#000",
                                             dropdown_fg_color="#FFF",
                                             dropdown_font=("Arial", 15), dropdown_hover_color="#dee3de",
                                             dropdown_text_color="#212121", state="readonly",
                                             values=list(gv.general_task_dict.keys()),
                                             command=self.combobox_selected)
        self.type_combobox.pack(side="left", anchor="nw", padx=10)
        self.type_combobox.set(value="Квадратные уравнения")

        self.type_error = ctk.CTkLabel(self.type_frame, text="",
                                       font=("Arial", 20), text_color="#ff5757")
        self.type_error.pack(side="left", anchor="nw", padx=10, pady=7)

        self.count_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.count_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=5)
        self.count_label = ctk.CTkLabel(self.count_frame, text="Установите количество задач", font=("Arial", 30),
                                        text_color="#737373")
        self.count_label.pack(anchor="nw", padx=10, pady=8)
        self.var = ctk.IntVar(value=1)
        self.count_entry = ctk.CTkEntry(self.count_frame, font=("Arial", 40), width=100, height=60,
                                        fg_color="#FFFFFF", text_color="#212121", border_color="#818c81",
                                        textvariable=self.var, state="disabled", justify="center")
        self.count_entry.pack(side="left", anchor="n", padx=10)

        self.count_slider = ctk.CTkSlider(self.count_frame, width=500, height=60, border_width=2,
                                          fg_color="#FFFFFF", border_color="#818c81", progress_color="#6fbd6f",
                                          button_color="#306130", hover=False, from_=1, to=10, number_of_steps=9,
                                          variable=self.var, state="disabled")  # from_ and to is a stub, since they change dynamically
        self.count_slider.bind("<Button-1>", self.disabled_count_slider)
        self.count_slider.pack(side="left", anchor="n", padx=10)

        self.go_button = ctk.CTkButton(self, command=self.goto_training, text="Приступить к выполнению",
                                       fg_color="#009900", height=70, width=430, font=("Arial", 30, "bold"),
                                       border_width=3, border_color="#006600", corner_radius=5,
                                       text_color="#FFFFFF", hover_color="#007D00")
        self.go_button.grid(row=4, column=0, sticky="ne", padx=30, pady=[15, 28])

    def get_name(self, event):
        gv.name = self.name_entry.get().strip()  # save username for table column "name_student"
        if len(gv.name) == 0:
            self.name_error.configure(text="Имя не должно быть пустым\nПожалуйста, напишите ещё раз")
            self.name_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191", text="Заполните все поля")
        else:
            if self.type_combobox.get() != "":
                self.info_label.configure(fg_color="#65bf65", text="Все поля заполнены")
            self.name_error.configure(text="")
            self.name_entry.configure(fg_color="#d9ffdf")

    def combobox_selected(self, event):
        if self.name_entry.get().strip() != "":
            self.info_label.configure(fg_color="#65bf65", text="Все поля заполнены")
        self.type_error.configure(text="")
        self.type_combobox.configure(fg_color="#d9ffdf")
        self.count_slider.configure(state="normal", to=len(gv.general_task_dict[self.type_combobox.get()]),
                                    number_of_steps=len(gv.general_task_dict[self.type_combobox.get()]) - 1)
        self.var.set(value=1)
        self.count_slider.unbind("<Button-1>")

    def disabled_count_slider(self, event):
        self.type_error.configure(text="Сначала надо выбрать тип задач\nПожалуйста, выберете его здесь")

    def goto_training(self):
        if self.name_entry.get() == "":
            self.name_error.configure(text="Имя не должно быть пустым\nПожалуйста, напишите ещё раз")
            self.name_entry.configure(fg_color="#ffc9c9")
        if self.type_combobox.get() == "":
            self.type_error.configure(text="Тип задач не должен быть пустым\nПожалуйста, выберете его из списка")
            self.type_combobox.configure(fg_color="#ffc9c9")
        if self.name_entry.get() != "" and self.type_combobox.get() != "":
            gv.tasks_type = self.type_combobox.get()
            gv.count_tasks = int(self.count_slider.get())
            gv.officer_task_dict = dict(enumerate(sample(list(gv.general_task_dict[gv.tasks_type].items()), gv.count_tasks), start=1))

            self.destroy()
            self.task_frame = TaskFrame(app, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)


class TaskFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        for i in range(1, gv.count_tasks + 1):
            gv.answer[i] = ""

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=2)
        self.rowconfigure(index=2, weight=100)
        self.rowconfigure(index=3, weight=2)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.progress_var = ctk.DoubleVar(value=(gv.counter - 1) / gv.count_tasks)
        self.task_progress = ctk.CTkProgressBar(self, height=30, corner_radius=30, border_width=3, fg_color="#d9ffdf",
                                                progress_color="#1bc21b", border_color="#818c81",
                                                variable=self.progress_var)
        self.task_progress.grid(row=0, column=0, columnspan=2, sticky="ew", padx=25, pady=[20, 10])

        self.exercise_label = ctk.CTkLabel(self, text=gv.exercise[gv.tasks_type], height=45,
                                           width=390, font=("Arial", 35, "bold"), text_color="#000000")
        self.exercise_label.grid(row=1, column=0, columnspan=2, sticky="nw", padx=28)

        self.task_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=300)
        self.task_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30)

        self.number_entry = ctk.CTkEntry(self.task_frame, font=("Arial", 35, "bold"),
                                         fg_color="#FFFFFF", text_color="#212121",
                                         border_color="#818c81", width=100,
                                         justify="center")
        self.number_entry.insert(0, "1 / " + str(gv.count_tasks))
        self.number_entry.configure(state="disabled")
        self.number_entry.pack(anchor="nw", padx=20, pady=[20, 10])
        self.task_label = ctk.CTkLabel(self.task_frame, height=45, width=390, text="",
                                       font=("Arial", 45, "bold"), text_color="#000000")
        self.task_label.pack(anchor="center", padx=20, pady=[0, 20])

        self.answer_info = ctk.CTkLabel(self.task_frame, width=390, text=gv.explanation,
                                        font=("Arial", 13, "bold"), text_color="#000000", justify="left")
        self.answer_info.pack(expand=True, anchor="s", padx=[20, 150], pady=[0, 6])

        self.task_entry = ctk.CTkEntry(self.task_frame, font=("Arial", 40), width=650, height=70,
                                       fg_color="#FFFFFF", text_color="#212121",
                                       border_color="#818c81")
        self.task_entry.bind("<KeyRelease>", self.change_answer)
        self.task_entry.pack(side="left", anchor="w", expand=True, padx=[80, 5], pady=[0, 150])

        self.save_photo = ctk.CTkImage(dark_image=Image.open("Image/save9.1.png"), size=(59, 59))
        self.save_button = ctk.CTkButton(self.task_frame, command=self.save_answer, height=70, width=80,
                                         fg_color="#009900", font=("Arial", 40, "bold"), border_width=3,
                                         border_color="#006600", corner_radius=5, text="",
                                         hover_color="#007D00", image=self.save_photo)
        self.save_button.pack(expand=True, side="left", anchor="w", padx=[8, 95], pady=[0, 150])

        self.previous_button = ctk.CTkButton(self, command=self.previous_task, text="Назад",
                                             fg_color="#009900",
                                             height=60, width=330, font=("Arial", 40, "bold"), border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             text_color="#FFFFFF", hover_color="#007D00",
                                             state="disabled")
        self.previous_button.grid(row=3, column=0, sticky="w", padx=30, pady=[14, 28])

        if gv.count_tasks == 1:
            self.next_button = ctk.CTkButton(self, command=self.go_to_result, text="Завершить",
                                             fg_color="#009900",
                                             height=60, width=330, font=("Arial", 40, "bold"), border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             text_color="#FFFFFF", hover_color="#007D00")
        else:
            self.next_button = ctk.CTkButton(self, command=self.next_task, text="Дальше",
                                             fg_color="#009900",
                                             height=60, width=330, font=("Arial", 40, "bold"), border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             text_color="#FFFFFF", hover_color="#007D00")
        self.next_button.grid(row=3, column=1, sticky="e", padx=30, pady=[14, 28])

        self.task_label.configure(text=gv.officer_task_dict[gv.counter][0])

    def save_answer(self):
        gv.answer[gv.counter] = (self.task_entry.get().strip())
        self.task_entry.configure(fg_color="#d9ffdf")

    def change_answer(self, event):
        self.task_entry.configure(fg_color="#ffffff")

    def next_task(self):
        gv.counter += 1
        self.progress_var.set(value=(gv.counter - 1) / gv.count_tasks)

        self.previous_button.configure(state="normal")

        self.task_label.configure(text=gv.officer_task_dict[gv.counter][0])
        self.task_entry.delete(0, "end")
        if gv.answer[gv.counter] != "":
            self.task_entry.insert(0, gv.answer[gv.counter])
            self.task_entry.configure(fg_color="#d9ffdf")
        else:
            self.task_entry.configure(fg_color="#ffffff")

        self.number_entry.configure(state="normal")
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, f'{gv.counter} / {gv.count_tasks}')
        self.number_entry.configure(state="disabled")

        if gv.counter == gv.count_tasks:
            self.next_button.configure(text="Завершить", command=self.go_to_result)

    def previous_task(self):
        if gv.counter == gv.count_tasks:
            self.next_button.configure(text="Дальше", command=self.next_task)

        gv.counter -= 1
        self.progress_var.set(value=(gv.counter - 1) / gv.count_tasks)

        self.task_label.configure(text=gv.officer_task_dict[gv.counter][0])
        self.task_entry.delete(0, "end")
        if gv.answer[gv.counter] != "":
            self.task_entry.insert(0, gv.answer[gv.counter])
            self.task_entry.configure(fg_color="#d9ffdf")
        else:
            self.task_entry.configure(fg_color="#ffffff")

        self.number_entry.configure(state="normal")
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, f'{gv.counter} / {gv.count_tasks}')
        self.number_entry.configure(state="disabled")

        if gv.counter == 1:
            self.previous_button.configure(state="disabled")

    def go_to_result(self):
        hd.answer_handler(gv.answer, gv.officer_task_dict)  # Getting the value of a variable gv.result
        hd.get_true_in_a_row(gv.result)  # Getting the value of a variable gv.true_in_a_row

        # Database work
        hd.create_database()
        hd.database_update(name_student=gv.name, topic_of_test=gv.tasks_type,
                           abs_quantity=sum(gv.result), all_quantity=gv.count_tasks,
                           ratio=round(sum(gv.result) / gv.count_tasks * 100, 2),
                           result=gv.true_in_a_row)

        # Проверка базы данных для разработчика
        db = sqlite3.connect('Math_simulator_database.db')
        c = db.cursor()
        c.execute('''SELECT * FROM student;''')
        table1 = (c.fetchall(), 'student')
        c.execute('''SELECT * FROM max_score ORDER BY max_result DESC;''')
        table2 = (c.fetchall(), 'max_score')
        c.execute('''SELECT * FROM score;''')
        table3 = (c.fetchall(), 'score')
        hd.print_table(table1, table2, table3)

        self.destroy()
        self.result_frame = ResultFrame(app, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)


class ResultFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=2)
        self.rowconfigure(index=2, weight=100)
        self.rowconfigure(index=3, weight=2)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Ознакомьтесь с вашими результатами:",
                                        font=("Arial", 35, "bold"), text_color="#000000")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="sw", padx=30, pady=[19, 13])

        self.result_label = ctk.CTkLabel(self, text=f"Вы решили {sum(gv.result)} из {gv.count_tasks} задач",
                                         font=("Arial", 35, "bold"), text_color="#000000",
                                         height=45, corner_radius=10, width=390, fg_color="#a5faa5")
        self.result_label.grid(row=1, column=0, columnspan=2, sticky="n", padx=30, pady=[0, 10])

        # Create style
        self.table_style = ttk.Style()  # Need refactor
        self.table_style.theme_use("default")
        self.table_style.configure("1.Treeview",
                                   background="#c5faac", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('1.Treeview', background=[('selected', '#f5ffb8')], foreground=[("selected", "black")])
        self.table_style.configure("1.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Calibri", 28, "bold"))
        self.table_style.map("1.Treeview.Heading", background=[('active', '#5cd649')])

        # Treeview creating
        self.result_table = ttk.Treeview(self, style="1.Treeview", columns=gv.columns,
                                         show="headings", selectmode="extended")
        # Tag create
        self.result_table.tag_configure("table_tag_true", font=("Calibri", 23, "bold"))
        self.result_table.tag_configure("table_tag_false", font=("Calibri", 23, "bold"), background="#fca4a4")

        # Setting columns
        self.result_table.heading(gv.columns[0], text='Задача', anchor="c")
        self.result_table.heading(gv.columns[1], text='Ваш ответ', anchor="c")
        self.result_table.heading(gv.columns[2], text='Правильный ответ', anchor="c")

        self.result_table.column(column=gv.columns[0], width=100)
        self.result_table.column(column=gv.columns[1], width=300)
        self.result_table.column(column=gv.columns[2], width=300)

        self.result_table.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30, pady=(0, 25))

        # Insert rows
        for num in range(1, gv.count_tasks + 1):
            if gv.result[num - 1] == 1:  # True answer, so table row - green (use tags="table_tag_true")
                self.result_table.insert("", "end",
                                         values=(num, gv.answer[num], ", ".join(map(str, sorted(list(gv.officer_task_dict[num][1]))))),
                                         tags="table_tag_true")
            else:  # False answer, so table row - red (use tags="table_tag_false")
                self.result_table.insert("", "end",
                                         values=(num, gv.answer[num], ", ".join(map(str, sorted(list(gv.officer_task_dict[num][1]))))),
                                         tags="table_tag_false")

        # Label congratulations on new record
        if gv.new_record_flag is True:
            self.new_record_label = ctk.CTkLabel(self, text=f"Поздравляю! Вы побили свой рекорд по решённым\nподряд заданиям: {gv.old_true_in_a_row} >>> {gv.true_in_a_row}",
                                             font=("Arial", 33, "bold"), text_color="#000000",
                                             height=45, corner_radius=7, width=390, fg_color="#a5faa5")
            self.new_record_label.grid(row=3, column=0, columnspan=2, sticky="s", padx=35, pady=[5, 5])
            # self.rowconfigure(index=4, weight=2)

        # Final button
        self.all_results_button = ctk.CTkButton(self, command=self.go_to_all_results, text="Все результаты",
                                                fg_color="#009900", height=60, width=330,
                                                font=("Arial", 40, "bold"), border_width=3,
                                                border_color="#006600", corner_radius=5,
                                                text_color="#FFFFFF", hover_color="#007D00")
        self.all_results_button.grid(row=4, column=0, sticky="nw", padx=30, pady=[14, 28])

        self. close_program_button = ctk.CTkButton(self, command=finish, text="Завершить",
                                                   fg_color="#009900", height=60, width=330,
                                                   font=("Arial", 40, "bold"), border_width=3,
                                                   border_color="#006600", corner_radius=5,
                                                   text_color="#FFFFFF", hover_color="#007D00")
        self.close_program_button.grid(row=4, column=1, sticky="ne", padx=30, pady=[14, 28])

    def go_to_all_results(self):
        self.destroy()
        self.all_results_frame = AllResultsFrame(app, border_width=15, border_color="#006600",
                                                 fg_color="#FFFFFF", corner_radius=30)


class AllResultsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create Notebook
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=True, fill="both", padx=19, pady=19)

        self.frame1 = ttk.Frame(master=self.tabs, relief="solid", borderwidth=3)
        self.frame2 = ttk.Frame(master=self.tabs, relief="solid", borderwidth=3)
        self.frame1.pack(expand=True, fill="both")
        self.frame2.pack(expand=True, fill="both")

        # Grid setting
        self.frame1.rowconfigure(index=0, weight=100)
        self.frame1.rowconfigure(index=1, weight=1)
        self.frame1.columnconfigure(index=0, weight=1)
        self.frame1.columnconfigure(index=1, weight=1)

        self.frame2.rowconfigure(index=0, weight=100)
        self.frame2.rowconfigure(index=1, weight=1)
        self.frame2.columnconfigure(index=0, weight=1)
        self.frame2.columnconfigure(index=1, weight=1)

        # Creating an image
        im_trophy = Image.open("Image/Trophy.png")
        im_trophy.thumbnail(size=(30, 30))
        im_star = Image.open("Image/star.png")
        im_star.thumbnail(size=(30, 30))
        global trophy_icon, star_icon
        trophy_icon = ImageTk.PhotoImage(im_trophy)
        star_icon = ImageTk.PhotoImage(im_star)

        self.tabs.add(child=self.frame1, text='Все результаты', image=star_icon, compound="left")
        self.tabs.add(child=self.frame2, text='Лучшие результаты', image=trophy_icon, compound="left")

        # Create style
        self.table_style = ttk.Style() # Need refactor
        self.table_style.theme_use("default")
        self.table_style.configure("2.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('2.Treeview', background=[('selected', '#f5ffb8')], foreground=[("selected", "black")])
        self.table_style.configure("2.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Calibri", 25, "bold"))
        self.table_style.map("2.Treeview.Heading", background=[('active', '#5cd649')])

        # Information loading to frame1 and frame2
        # Treeview creating
        self.all_result_table = ttk.Treeview(self.frame1, style="2.Treeview", columns=gv.columns_all_result,
                                             show="headings", selectmode="extended")

        # Tag create
        self.all_result_table.tag_configure("all_result_table_tag_1", font=("Calibri", 20, "bold"))

        # Setting columns
        self.all_result_table.heading(gv.columns_all_result[0], text='№', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[1], text='Имя', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[2], text='Тип', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[3], text='Результат', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[4], text='Качество', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[5], text='Подряд', anchor="c")

        self.all_result_table.column(column=gv.columns_all_result[0], width=1)
        self.all_result_table.column(column=gv.columns_all_result[1], width=10)
        self.all_result_table.column(column=gv.columns_all_result[2], width=50)
        self.all_result_table.column(column=gv.columns_all_result[3], width=80)
        self.all_result_table.column(column=gv.columns_all_result[4], width=30)
        self.all_result_table.column(column=gv.columns_all_result[5], width=30)

        self.all_result_table.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 5))

        # Button
        self.back_button = ctk.CTkButton(self.frame1, command=self.back_to_result, text="Назад",
                                         fg_color="#009900", height=60, width=330,
                                         font=("Arial", 40, "bold"), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         text_color="#FFFFFF", hover_color="#007D00")
        self.back_button.grid(row=1, column=0, sticky="nw", padx=5, pady=[0, 3])

        self.close_program_button_1 = ctk.CTkButton(self.frame1, command=finish, text="Завершить",
                                                    fg_color="#009900", height=60, width=330,
                                                    font=("Arial", 40, "bold"), border_width=3,
                                                    border_color="#006600", corner_radius=5,
                                                    text_color="#FFFFFF", hover_color="#007D00")
        self.close_program_button_1.grid(row=1, column=1, sticky="ne", padx=5, pady=[0, 3])

        # Row insert
        for row in hd.get_rows("all_result_table"):
            self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_1")

        # for row in hd.get_rows("max_result_table")
        # Need color setting, place setting and more

        # Methods
    def back_to_result(self):
        self.destroy()
        self.result_frame = ResultFrame(app, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)



if __name__ == "__main__":
    app = App()
    app.protocol('WM_DELETE_WINDOW', finish)
    app.mainloop()
