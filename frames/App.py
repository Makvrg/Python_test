from typing import NoReturn
import customtkinter as ctk
from functions import image_initialization as ii
import functions.db_handlers as dbh

import frames.Info, frames.AdminMenu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        #self.iconbitmap("")
        self.geometry("1000x700+360+150")
        self.resizable(False, False)
        self.configure(fg_color="#CCFFCC")

        # Theme and mode setting
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("light")

        # Grid configuration
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=10)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.main_frame = ctk.CTkFrame(self, border_width=15, border_color="#006600",
                                       fg_color="#FFFFFF", corner_radius=30)
        self.main_frame.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        self.hallo_label = ctk.CTkLabel(self.main_frame, image=ii.get_first_display_image(),
                                        fg_color="#FFFFFF", text="")
        self.hallo_label.grid(row=0, column=0, columnspan=2, sticky="n", padx=[33, 15], pady=[50, 0])

        self.go_admin_button = ctk.CTkButton(self.main_frame, command=self.goto_admin_menu, text="",
                                             fg_color="#009900", height=52, width=52, border_width=3,
                                             border_color="#006600", corner_radius=5, hover_color="#007D00",
                                             text_color="#FFF", image=ii.get_admin_image())
        self.go_admin_button.grid(row=1, column=0, sticky="e", padx=[15, 10], pady=[125, 195])
        self.go_button = ctk.CTkButton(self.main_frame, command=self.goto_info, text="Начать",
                                       fg_color="#009900", height=45, width=400, border_width=3,
                                       border_color="#006600", corner_radius=5, hover_color="#007D00",
                                       text_color="#FFF", font=("Fira Sans Bold", 70))
        self.go_button.grid(row=1, column=1, sticky="w", padx=[5, 20], pady=[125, 195])

    def goto_info(self) -> NoReturn:
        dbh.create_database()  # Connect or create and check database

        self.main_frame.destroy()

        info_frame = frames.Info.Info(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)

    def goto_admin_menu(self) -> NoReturn:
        dbh.create_database()  # Connect or create and check database

        self.main_frame.destroy()

        admin_frame = frames.AdminMenu.AdminMenu(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)
