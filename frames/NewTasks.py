import customtkinter as ctk
from typing import Any, NoReturn, Tuple
from functions import db_handlers as dbh, handlers as hd


class NewTasks(ctk.CTkFrame):
    def __init__(self, master: Any, columns_names, choice_type, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = columns_names

        # Create attribute with choice_type
        self.choice_type: Tuple[int, str] = choice_type


        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        for i in range(1, 4):
            self.rowconfigure(index=i, weight=10000)
        self.rowconfigure(index=4, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        # Create widgets
        self.info_label = ctk.CTkLabel(self, text=f"Задача типа: {self.choice_type[1]}", font=("Fira Sans SemiBold", 35), height=45,
                                       corner_radius=10,
                                       width=350, fg_color="#ff9191", text_color="#000000")
        self.info_label.grid(row=0, column=0, columnspan=2, sticky="sw", padx=30, pady=[30, 13])


        self.task_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.task_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=30, pady=5)
        self.task_label = ctk.CTkLabel(self.task_frame, text="Напишите задачу", font=("Fira Sans", 30),
                                       text_color="#6b6b6b")
        self.task_label.pack(anchor="nw", padx=10, pady=8)
        self.task_entry = ctk.CTkEntry(self.task_frame, font=("Tahoma", 33), width=550, height=60,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.task_entry.bind("<KeyRelease>", self.get_task)
        self.task_entry.pack(side="left", anchor="nw", padx=[10, 0])

        self.task_error = ctk.CTkLabel(self.task_frame, text="",
                                       font=("Fira Sans", 20), text_color="#FF5555")
        self.task_error.pack(side="left", anchor="nw", padx=10, pady=7)


        self.exercise_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.exercise_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30, pady=5)
        self.exercise_label = ctk.CTkLabel(self.exercise_frame, text="Напишите задание", font=("Fira Sans", 30),
                                       text_color="#6b6b6b")
        self.exercise_label.pack(anchor="nw", padx=10, pady=8)
        self.exercise_entry = ctk.CTkEntry(self.exercise_frame, font=("Tahoma", 33), width=550, height=60,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.exercise_entry.bind("<KeyRelease>", self.get_exercise)
        self.exercise_entry.pack(side="left", anchor="nw", padx=[10, 0])

        self.exercise_error = ctk.CTkLabel(self.exercise_frame, text="",
                                       font=("Fira Sans", 20), text_color="#FF5555")
        self.exercise_error.pack(side="left", anchor="nw", padx=10, pady=7)


        self.answer_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.answer_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=30, pady=5)
        self.answer_label = ctk.CTkLabel(self.answer_frame, text="Напишите ответ", font=("Fira Sans", 30),
                                           text_color="#6b6b6b")
        self.answer_label.pack(anchor="nw", padx=10, pady=8)
        self.answer_entry = ctk.CTkEntry(self.answer_frame, font=("Tahoma", 33), width=550, height=60,
                                           fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.answer_entry.bind("<KeyRelease>", self.get_answer)
        self.answer_entry.pack(side="left", anchor="nw", padx=[10, 0])

        self.answer_error = ctk.CTkLabel(self.answer_frame, text="",
                                           font=("Fira Sans", 20), text_color="#FF5555")
        self.answer_error.pack(side="left", anchor="nw", padx=10, pady=7)


        self.back_button = ctk.CTkButton(self, command=self.back_to_editor, text="Назад",
                                         fg_color="#009900", height=70, width=250, text_color="#FFF",
                                         border_width=3, border_color="#006600", corner_radius=5,
                                         font=("Fira Sans SemiBold", 47), hover_color="#007D00")
        self.back_button.grid(row=4, column=0, sticky="nw", padx=30, pady=[15, 28])
        self.new_task_button = ctk.CTkButton(self, command=self.create_new_task, text="Создать",
                                       fg_color="#009900", height=70, width=445, text_color="#FFF",
                                       border_width=3, border_color="#006600", corner_radius=5,
                                       font=("Fira Sans SemiBold", 47), hover_color="#007D00")
        self.new_task_button.grid(row=4, column=1, sticky="ne", padx=30, pady=[15, 28])



    def get_task(self, event: Any) -> NoReturn:
        if len(self.task_entry.get().strip()) == 0:
            self.task_error.configure(text="Задача не должна быть пустой\nПожалуйста, напишите ещё раз")
            self.task_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")
        else:
            if len(self.exercise_entry.get().strip()) != 0 and len(self.answer_entry.get().strip()) != 0:
                self.info_label.configure(fg_color="#65bf65")
            self.task_error.configure(text="")
            self.task_entry.configure(fg_color="#d9ffdf")


    def get_exercise(self, event: Any) -> NoReturn:
        if len(self.exercise_entry.get().strip()) == 0:
            self.exercise_error.configure(text="Задание не должно быть пустым\nПожалуйста, напишите ещё раз")
            self.exercise_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")
        else:
            if len(self.task_entry.get().strip()) != 0 and len(self.answer_entry.get().strip()) != 0:
                self.info_label.configure(fg_color="#65bf65")
            self.exercise_error.configure(text="")
            self.exercise_entry.configure(fg_color="#d9ffdf")


    def get_answer(self, event: Any) -> NoReturn:
        if len(self.answer_entry.get().strip()) == 0:
            self.answer_error.configure(text="Ответ не должен быть пустым\nПожалуйста, напишите ещё раз")
            self.answer_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")
        else:
            if len(self.task_entry.get().strip()) != 0 and len(self.exercise_entry.get().strip()) != 0:
                self.info_label.configure(fg_color="#65bf65")
            self.answer_error.configure(text="")
            self.answer_entry.configure(fg_color="#d9ffdf")


    def create_new_task(self) -> NoReturn:
        if len(self.task_entry.get().strip()) == 0:
            self.task_error.configure(text="Задача не должна быть пустой\nПожалуйста, напишите ещё раз")
            self.task_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")

        if len(self.exercise_entry.get().strip()) == 0:
            self.exercise_error.configure(text="Задание не должно быть пустым\nПожалуйста, напишите ещё раз")
            self.exercise_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")

        if len(self.answer_entry.get().strip()) == 0:
            self.answer_error.configure(text="Ответ не должен быть пустым\nПожалуйста, напишите ещё раз")
            self.answer_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191")

        if len(self.task_entry.get().strip()) != 0 and len(self.exercise_entry.get().strip()) != 0 and len(self.answer_entry.get().strip()) != 0:
            serialize_answer = hd.admin_answer(self.answer_entry.get().strip())

            if serialize_answer == "":
                self.answer_error.configure(text="Недопустимый ответ\nПожалуйста, напишите ещё раз")
                self.answer_entry.configure(fg_color="#ffc9c9")
                self.info_label.configure(fg_color="#ff9191")

            else:
                dbh.insert_task_from_admin(tasks_type=self.choice_type[1], task_type_is_exist=True,
                                           task_exercise=self.exercise_entry.get().strip(),
                                           list_with_values=(self.task_entry.get().strip(), serialize_answer))
                self.task_entry.delete(0, "end")
                self.answer_entry.delete(0, "end")
                self.info_label.configure(fg_color="#ff9191")
                self.task_entry.configure(fg_color="#FFF")
                self.answer_entry.configure(fg_color="#FFF")



    def back_to_editor(self):
        self.destroy()

        import frames.Editor

        editor_frame = frames.Editor.Editor(self.window_attribute, self.columns_names, self.choice_type,
                                            border_width=15, border_color="#006600", fg_color="#FFFFFF",
                                            corner_radius=30)