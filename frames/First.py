from typing import NoReturn, Any
import customtkinter as ctk
from functions import image_initialization as ii
import functions.db_handlers as dbh

import frames.Info


class First(ctk.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Grid configuration
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.hallo_label = ctk.CTkLabel(self, image=ii.get_first_display_image(),
                                        fg_color="#FFFFFF", text="")
        self.hallo_label.grid(row=0, column=0, columnspan=2, sticky="n", padx=[15, 15], pady=[50, 0])

        self.go_password_button = ctk.CTkButton(self, command=self.goto_password_check, text="",
                                                fg_color="#009900", height=52, width=52, border_width=3,
                                                border_color="#006600", corner_radius=5, hover_color="#007D00",
                                                text_color="#FFF", image=ii.get_admin_image())
        self.go_password_button.grid(row=1, column=0, sticky="e", padx=[15, 10], pady=[50, 115])
        self.go_button = ctk.CTkButton(self, command=self.goto_info, text="Начать",
                                       fg_color="#009900", height=45, width=400, border_width=3,
                                       border_color="#006600", corner_radius=5, hover_color="#007D00",
                                       text_color="#FFF", font=("Fira Sans Bold", 70))
        self.go_button.grid(row=1, column=1, sticky="w", padx=[5, 20], pady=[50, 115])

    def goto_info(self) -> NoReturn:
        dbh.create_database()  # Connect or create and check database

        self.destroy()

        info_frame = frames.Info.Info(self.window_attribute, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)

    def goto_password_check(self) -> NoReturn:
        self.destroy()

        import frames.Password

        password_frame = frames.Password.Password(self.window_attribute, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)