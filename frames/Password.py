import customtkinter as ctk
from typing import Any, NoReturn
from functions import password_security as ps


class Password(ctk.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=3)
        self.rowconfigure(index=2, weight=5)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.info_label_1 = ctk.CTkLabel(self, text="Этот раздел предназначен только для учителя",
                                         font=("Fira Sans SemiBold", 37), fg_color="#65bf65", text_color="#000000",
                                         height=50, corner_radius=10, width=380)
        self.info_label_1.grid(row=0, column=0, columnspan=2, sticky="nw", padx=30, pady=28)

        # Frame and Entry
        self.password_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=120)
        self.password_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=30, pady=100)
        self.info_label_2 = ctk.CTkLabel(self.password_frame, text="Для доступа к админ-панели введите пароль",
                                         font=("Fira Sans", 35), text_color="#6b6b6b")
        self.info_label_2.pack(anchor="nw", padx=10, pady=[8, 10])
        self.password_entry = ctk.CTkEntry(self.password_frame, font=("Tahoma", 40), width=700, height=75,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.password_entry.bind("<KeyRelease>", self.input_password)
        self.password_entry.pack(anchor="nw", padx=10)
        self.password_error = ctk.CTkLabel(self.password_frame, text="",
                                       font=("Fira Sans", 20), text_color="#FF5555")
        self.password_error.pack(side="left", anchor="nw", padx=10, pady=[10, 7])

        # Button
        self.back_button = ctk.CTkButton(self, command=self.back_to_first, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 50), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=2, column=0, sticky="sw", padx=30, pady=[14, 36])

        self.go_admin_button = ctk.CTkButton(self, command=self.go_admin, text="Далее",
                                             text_color="#FFF", fg_color="#009900",
                                             height=50, width=330, border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             hover_color="#007D00", font=("Fira Sans Bold", 50))
        self.go_admin_button.grid(row=2, column=1, sticky="se", padx=30, pady=[14, 36])


    def back_to_first(self) -> NoReturn:
        self.destroy()

        import frames.First

        first_frame = frames.First.First(self.window_attribute, border_width=15, border_color="#006600",
                                         fg_color="#FFFFFF", corner_radius=30)


    def input_password(self, event: Any) -> NoReturn:
        self.password_entry.configure(fg_color="#FFFFFF")
        self.password_error.configure(text="")


    def go_admin(self) -> NoReturn:
        if ps.verify_password(self.password_entry.get()):
            self.destroy()

            import frames.AdminMenu

            admin_frame = frames.AdminMenu.AdminMenu(self.window_attribute, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)
        else:
            self.password_entry.configure(fg_color="#ffc9c9")
            self.password_error.configure(text="Неверный пароль. Пожалуйста, напишите ещё раз")
