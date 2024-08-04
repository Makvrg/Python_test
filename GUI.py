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
                                       border_color="#006600", corner_radius=5, text_color="#FFFFFF")
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
        self.info_label = ctk.CTkLabel(self, text="Заполните все пропуски", height=40, corner_radius=10,
                                       width=390, font=("Arial", 30, "bold"), fg_color="#ff9191", text_color="#000000")
        self.info_label.grid(row=0, column=0, sticky="sw", padx=30, pady=25)

        self.name_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.name_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=5)

        self.type_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.type_frame.grid(row=2, column=0, sticky="nsew", padx=30, pady=5)

        self.count_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.count_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=5)

        self.go_button = ctk.CTkButton(self, command=self.goto_training, text="Приступить к выполнению", fg_color="#009900",
                                       height=70, width=430, font=("Arial", 30, "bold"), border_width=3,
                                       border_color="#006600", corner_radius=5, text_color="#FFFFFF")
        self.go_button.grid(row=4, column=0, sticky="ne", padx=30, pady=28)

    def goto_training(self):
        #self.main_frame.destroy()
        #self.info_frame = InfoFrame(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
