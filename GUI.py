import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        self.geometry("1000x700+450+200")
        self.configure(fg_color="#F2FBFF")
        self.hallo_label = ctk.CTkLabel(self, text="Добро пожаловать в математический тренажер", font=("Fira Sans", 16))
        self.hallo_label.pack(anchor="n")
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("system")






if __name__ == "__main__":
    app = App()
    app.mainloop()