import customtkinter as ctk
#import Math_simulator_code as ms_code


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        self.geometry("1000x700+450+200")
        self.configure(fg_color="#c793f5")
        self.main_frame = ctk.CTkFrame(self, border_width=15, border_color="#0c0aa3",
                                       fg_color="#6f2da8", corner_radius=30)
        self.main_frame.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)
        self.hallo_label = ctk.CTkLabel(self.main_frame, text="Добро пожаловать в математический тренажер",
                                        font=("Arial", 37, "bold"), corner_radius=20, fg_color="#fff")
        self.hallo_label.pack(side="top", pady=60)
        self.go_button = ctk.CTkButton(self.main_frame, command=self.go_training, text="Начать", fg_color="#0c0aa3",
                                       height=100, width=400, font=("Arial", 70, "bold"), border_width=3,
                                       border_color="#fff", corner_radius=5)
        self.go_button.pack(side="bottom", pady=150)

    def go_training(self):
        self.main_frame.destroy()
        self.info_frame = InfoFrame(self, border_width=15, border_color="#0c0aa3", fg_color="#6f2da8", corner_radius=30)

    # Theme and mode setting
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("system")


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Grid configuration
        for i in range(4):
            self.rowconfigure(index=i, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Create widgets
        self.name_frame = ctk.CTkFrame(self, border_width=5, border_color="#74ccf2", fg_color="#fff", corner_radius=30, height=100)
        self.name_frame.grid(row=0, sticky="ew", padx=30, pady=40)

        self.type_frame = ctk.CTkFrame(self, border_width=5, border_color="#74ccf2", fg_color="#fff", corner_radius=30, height=100)
        self.type_frame.grid(row=1, sticky="ew", padx=30, pady=40)

        self.count_frame = ctk.CTkFrame(self, border_width=5, border_color="#74ccf2", fg_color="#fff", corner_radius=30, height=100)
        self.count_frame.grid(row=3, sticky="ew", padx=30, pady=40)





if __name__ == "__main__":
    app = App()
    app.mainloop()
