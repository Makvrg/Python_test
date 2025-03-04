import customtkinter as ctk
from typing import Any, NoReturn


class AdminMenu(ctk.CTkFrame):
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

        # Button
        self.back_button = ctk.CTkButton(self, command=self.back_to_password, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 50), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=2, column=0, sticky="sw", padx=30, pady=[14, 36])

        self.go_admin_button = ctk.CTkButton(self, text="None",
                                             text_color="#FFF", fg_color="#009900",
                                             height=50, width=330, border_width=3,
                                             border_color="#006600", corner_radius=5,
                                             hover_color="#007D00", font=("Fira Sans Bold", 50))
        self.go_admin_button.grid(row=2, column=1, sticky="se", padx=30, pady=[14, 36])


    def back_to_password(self) -> NoReturn:
        self.destroy()

        import frames.Password

        first_frame = frames.Password.Password(self.window_attribute, border_width=15, border_color="#006600",
                                               fg_color="#FFFFFF", corner_radius=30)