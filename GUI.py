import customtkinter as ctk
#import Math_simulator_code as ms_code

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        self.geometry("1000x700+450+200")
        self.configure(fg_color="#CCFFCC")
        self.main_frame = ctk.CTkFrame(self, border_width=15, border_color="#006600",
                                       fg_color="#FFFFFF", corner_radius=30)
        self.main_frame.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)
        self.hallo_label = ctk.CTkLabel(self.main_frame, text="Добро пожаловать в математический тренажер",
                                        font=("Arial", 37, "bold"), fg_color="#FFFFFF", text_color="#000000")
        self.hallo_label.pack(side="top", pady=60)
        self.go_button = ctk.CTkButton(self.main_frame, command=self.goto_info, text="Начать", fg_color="#009900",
                                       height=100, width=400, font=("Arial", 70, "bold"), border_width=3,
                                       border_color="#006600", corner_radius=5, text_color="#FFFFFF", hover_color="#007D00")
        self.go_button.pack(side="bottom", pady=150)

    def goto_info(self):
        self.main_frame.destroy()
        self.info_frame = InfoFrame(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)

    # Theme and mode setting
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("system")


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
                                       fg_color="#FFFFFF",text_color="#212121", border_color="#818c81")
        self.name_entry.bind("<KeyRelease>", self.get_name)
        self.name_entry.pack(side="left", anchor="nw", padx=10)
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
                                             button_color="#818c81", button_hover_color="#000", dropdown_fg_color="#FFF",
                                             dropdown_font=("Arial", 15), dropdown_hover_color="#dee3de",
                                             dropdown_text_color="#212121", state="readonly", values=["Квадратные уравнения", "Задачи"],
                                             command=self.combobox_selected)
        self.type_combobox.pack(side="left", anchor="nw", padx=10)
        self.combobox_error = ctk.CTkLabel(self.type_frame, text="",
                                       font=("Arial", 20), text_color="#ff5757")
        self.combobox_error.pack(side="left", anchor="nw", padx=10, pady=7)

        self.count_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.count_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=5)
        self.count_label = ctk.CTkLabel(self.count_frame, text="Установите количество задач", font=("Arial", 30),
                                       text_color="#737373")
        self.count_label.pack(anchor="nw", padx=10, pady=8)
        var = ctk.IntVar(value=4)
        self.count_entry = ctk.CTkEntry(self.count_frame, font=("Arial", 40), width=100, height=60,
                                        fg_color="#FFFFFF", text_color="#212121", border_color="#818c81",
                                        textvariable=var, state="disabled", justify="center")
        self.count_entry.pack(side="left", anchor="n", padx=10)

        self.count_slider = ctk.CTkSlider(self.count_frame, width=500, height=60, border_width=2,
                                          fg_color="#FFFFFF", border_color="#818c81", progress_color="#6fbd6f",
                                          button_color="#306130", hover=False, from_=1, to=10, number_of_steps=9,
                                          variable=var)
        self.count_slider.pack(side="left", anchor="n", padx=10)

        self.go_button = ctk.CTkButton(self, command=self.goto_training, text="Приступить к выполнению", fg_color="#009900",
                                       height=70, width=430, font=("Arial", 30, "bold"), border_width=3,
                                       border_color="#006600", corner_radius=5,
                                       text_color="#FFFFFF", hover_color="#007D00")
        self.go_button.grid(row=4, column=0, sticky="ne", padx=30, pady=[15, 28])

    def get_name(self, event):
        name = self.name_entry.get().strip()
        print(name)
        if len(name) == 0:
            self.name_error.configure(text="Имя не должно быть пустым.\nПожалуйста, напишите ещё раз")
            self.name_entry.configure(fg_color="#ffc9c9")
            self.info_label.configure(fg_color="#ff9191", text="Заполните все поля")
        else:
            if self.type_combobox.get() != "":
                self.info_label.configure(fg_color="#65bf65", text="Все поля заполнены")
            self.name_error.configure(text="")
            self.name_entry.configure(fg_color="#d9ffdf")

    def combobox_selected(self, event):
        self.info_label.configure(fg_color="#65bf65", text="Все поля заполнены")
        self.combobox_error.configure(text="")
        self.type_combobox.configure(fg_color="#d9ffdf")

    def goto_training(self):
        if self.name_entry.get() == "":
            self.name_error.configure(text="Имя не должно быть пустым.\nПожалуйста, напишите ещё раз")
            self.name_entry.configure(fg_color="#ffc9c9")
        if self.type_combobox.get() == "":
            self.combobox_error.configure(text="Тип задач не должен быть пустым.\nПожалуйста, выберете его из списка")
            self.type_combobox.configure(fg_color="#ffc9c9")


if __name__ == "__main__":
    app = App()
    app.mainloop()
