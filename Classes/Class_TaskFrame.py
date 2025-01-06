import customtkinter as ctk
import Global_variable as gv
import Handlers as hd
import sqlite3
import Image_initialization as Ii


class TaskFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        for i in range(1, gv.count_tasks + 1):
            gv.answer[i] = ""

        # Create attribute from window
        self.window_attribute = master

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
        self.task_progress.grid(row=0, column=0, columnspan=2, sticky="ew", padx=25, pady=[23, 5])

        self.exercise_label = ctk.CTkLabel(self, text="", image=gv.exercise[gv.tasks_type])
        self.exercise_label.grid(row=1, column=0, columnspan=2, sticky="nw", padx=30)

        self.task_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=300)
        self.task_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30)

        self.number_entry = ctk.CTkEntry(self.task_frame, font=("Arial", 35, "bold"),
                                         fg_color="#FFFFFF", text_color="#212121",
                                         border_color="#818c81", width=100,
                                         justify="center")
        self.number_entry.insert(0, "1 / " + str(gv.count_tasks))
        self.number_entry.configure(state="disabled")
        self.number_entry.pack(anchor="nw", padx=20, pady=[20, 10])
        self.task_label = ctk.CTkLabel(self.task_frame, text="")
        self.task_label.pack(anchor="center", padx=20, pady=[20, 20])

        self.answer_info = ctk.CTkLabel(self.task_frame, width=390, image=Ii.get_label_explanation_image(),
                                        text="")
        self.answer_info.pack(expand=True, anchor="sw", padx=70, pady=[0, 6])

        self.task_entry = ctk.CTkEntry(self.task_frame, font=("Arial", 40), width=650, height=70,
                                       fg_color="#FFFFFF", text_color="#212121",
                                       border_color="#818c81")
        self.task_entry.bind("<KeyRelease>", self.change_answer)
        self.task_entry.pack(side="left", anchor="w", expand=True, padx=[80, 5], pady=[0, 150])

        self.save_button = ctk.CTkButton(self.task_frame, command=self.save_answer, height=70, width=70,
                                         fg_color="#009900", font=("Arial", 40, "bold"), border_width=3,
                                         border_color="#006600", corner_radius=5, text="",
                                         hover_color="#007D00", image=Ii.get_button_save_image())
        self.save_button.pack(expand=True, side="left", anchor="w", padx=[8, 95], pady=[0, 154])

        self.previous_button = ctk.CTkButton(self, command=self.previous_task, text="",
                                             fg_color="#009900", image=Ii.get_taskframe_button_previous_disabled_image(),
                                             height=60, width=330, border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             hover_color="#007D00", state="disabled")
        self.previous_button.grid(row=3, column=0, sticky="w", padx=30, pady=[14, 28])

        if gv.count_tasks == 1:
            self.next_button = ctk.CTkButton(self, command=self.go_to_result, text="",
                                             fg_color="#009900", image=Ii.get_taskframe_button_complete_image(),
                                             height=60, width=330, border_width=3, border_color="#006600",
                                             corner_radius=5, hover_color="#007D00")
        else:
            self.next_button = ctk.CTkButton(self, command=self.next_task, text="",
                                             fg_color="#009900", image=Ii.get_taskframe_button_next_image(),
                                             height=60, width=330, border_width=3, border_color="#006600",
                                             corner_radius=5, hover_color="#007D00")
        self.next_button.grid(row=3, column=1, sticky="e", padx=30, pady=[14, 28])

        self.task_label.configure(image=hd.output_task(gv.officer_task_dict[gv.counter][0], gv.tasks_type))

    def save_answer(self):
        gv.answer[gv.counter] = (self.task_entry.get().strip())
        self.task_entry.configure(fg_color="#d9ffdf")

    def change_answer(self, event):
        self.task_entry.configure(fg_color="#ffffff")

    def next_task(self):
        gv.counter += 1
        self.progress_var.set(value=(gv.counter - 1) / gv.count_tasks)

        self.previous_button.configure(state="normal", image=Ii.get_taskframe_button_previous_image())

        self.task_label.configure(image=hd.output_task(gv.officer_task_dict[gv.counter][0], gv.tasks_type))
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
            self.next_button.configure(image=Ii.get_taskframe_button_complete_image(), command=self.go_to_result)

    def previous_task(self):
        if gv.counter == gv.count_tasks:
            self.next_button.configure(image=Ii.get_taskframe_button_next_image(), command=self.next_task)

        gv.counter -= 1
        self.progress_var.set(value=(gv.counter - 1) / gv.count_tasks)

        self.task_label.configure(image=hd.output_task(gv.officer_task_dict[gv.counter][0], gv.tasks_type))
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
            self.previous_button.configure(state="disabled", image=Ii.get_taskframe_button_previous_disabled_image())

    def go_to_result(self):
        hd.create_database()

        hd.answer_handler(gv.answer, gv.officer_task_dict)  # Getting the value of a variable gv.result
        hd.get_true_in_a_row(gv.result)  # Getting the value of a variable gv.true_in_a_row

        # Database work
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
        c.execute('''SELECT * FROM errors_and_wrong;''')
        table4 = (c.fetchall(), 'errors_and_wrong')
        hd.print_table(table1, table2, table3, table4)

        db.commit()
        db.close()

        self.destroy()
        import Classes.Class_ResultFrame
        self.result_frame = Classes.Class_ResultFrame.ResultFrame(self.window_attribute, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)
