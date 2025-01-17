import customtkinter as ctk
import Global_variable as gv
from random import sample

import Classes.Class_TaskFrame


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        for i in range(1, 4):
            self.rowconfigure(index=i, weight=10000)
        self.rowconfigure(index=4, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Create widgets
        self.info_label = ctk.CTkLabel(self, text="Заполните все поля", font=("Fira Sans SemiBold", 35) , height=45, corner_radius=10,
                                       width=350, fg_color="#ff9191", text_color="#000000")
        self.info_label.grid(row=0, column=0, sticky="sw", padx=30, pady=[30, 13])

        self.name_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.name_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=5)
        self.name_label = ctk.CTkLabel(self.name_frame, text="Напишите своё имя", font=("Fira Sans", 30),
                                       text_color="#6b6b6b")
        self.name_label.pack(anchor="nw", padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(self.name_frame, font=("Tahoma", 35), width=500, height=60,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.name_entry.bind("<KeyRelease>", self.get_name)
        self.name_entry.pack(side="left", anchor="nw", padx=10)
        #self.name_entry.insert(0, "Тестовое имя")

        self.name_error = ctk.CTkLabel(self.name_frame, text="",
                                       font=("Fira Sans", 20), text_color="#FF5555")
        self.name_error.pack(side="left", anchor="nw", padx=10, pady=7)

        self.type_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.type_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=5)
        self.type_label = ctk.CTkLabel(self.type_frame, text="Выберите тип задач", font=("Fira Sans", 30),
                                       text_color="#6b6b6b")
        self.type_label.pack(anchor="nw", padx=10, pady=8)
        self.type_combobox = ctk.CTkComboBox(self.type_frame, hover=True, font=("Tahoma", 35), width=450, height=60,
                                             fg_color="#FFFFFF", text_color="#212121", border_color="#818c81",
                                             button_color="#818c81", button_hover_color="#6f7f6f",
                                             dropdown_fg_color="#FFF",
                                             dropdown_font=("Tahoma", 17), dropdown_hover_color="#dee3de",
                                             dropdown_text_color="#212121", state="readonly",
                                             values=list(gv.general_task_dict.keys()),
                                             command=self.combobox_selected)
        self.type_combobox.pack(side="left", anchor="nw", padx=10)
        #self.type_combobox.set(value="Квадратные уравнения")

        self.type_error = ctk.CTkLabel(self.type_frame, text="",
                                       font=("Fira Sans", 20), text_color="#FF5555")
        self.type_error.pack(side="left", anchor="nw", padx=10, pady=7)

        self.count_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.count_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=5)
        self.count_label = ctk.CTkLabel(self.count_frame, text="Установите количество задач",  font=("Fira Sans", 30),
                                        text_color="#6b6b6b")
        self.count_label.pack(anchor="nw", padx=10, pady=8)
        self.var = ctk.IntVar(value=1)
        self.count_entry = ctk.CTkEntry(self.count_frame, font=("Fira Sans", 45), width=100, height=60,
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
                                       fg_color="#009900", height=70, width=445, text_color="#FFF",
                                       border_width=3, border_color="#006600", corner_radius=5,
                                       font=("Fira Sans SemiBold", 33), hover_color="#007D00")
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
        self.type_error.configure(text="Сначала надо выбрать тип задач\nПожалуйста, выберите его здесь")

    def goto_training(self):
        if self.name_entry.get() == "":
            self.name_error.configure(text="Имя не должно быть пустым\nПожалуйста, напишите ещё раз")
            self.name_entry.configure(fg_color="#ffc9c9")
        if self.type_combobox.get() == "":
            self.type_error.configure(text="Тип задач не должен быть пустым\nПожалуйста, выберите его из списка")
            self.type_combobox.configure(fg_color="#ffc9c9")
        if self.name_entry.get() != "" and self.type_combobox.get() != "":
            gv.tasks_type = self.type_combobox.get()
            gv.count_tasks = int(self.count_slider.get())
            gv.officer_task_dict = dict(enumerate(sample(list(gv.general_task_dict[gv.tasks_type].items()), gv.count_tasks), start=1))

            self.destroy()

            task_frame = Classes.Class_TaskFrame.TaskFrame(self.window_attribute, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)
