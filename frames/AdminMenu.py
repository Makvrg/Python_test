import global_variables as gv
import customtkinter as ctk
from typing import Any, NoReturn


class AdminMenu(ctk.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = gv.columns_names

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

        self.all_results_button = ctk.CTkButton(self, command=self.go_to_all_results, text="Все результаты",
                                                fg_color="#009900", height=60, width=330, border_width=3,
                                                border_color="#006600", corner_radius=5, text_color="#FFF",
                                                font=("Fira Sans Bold", 40), hover_color="#007D00")
        self.all_results_button.grid(row=0, column=0, sticky="nw", padx=30, pady=[28, 28])

        self.edit_button = ctk.CTkButton(self, command=self.go_to_editor, text="Редактировать задания и типы",
                                                fg_color="#009900", height=60, width=330, border_width=3,
                                                border_color="#006600", corner_radius=5, text_color="#FFF",
                                                font=("Fira Sans Bold", 40), hover_color="#007D00")
        self.edit_button.grid(row=1, column=0, sticky="nw", padx=30, pady=[28, 28])


    def back_to_password(self) -> NoReturn:
        self.destroy()

        import frames.Password

        first_frame = frames.Password.Password(self.window_attribute, border_width=15, border_color="#006600",
                                               fg_color="#FFFFFF", corner_radius=30)

    def go_to_all_results(self) -> NoReturn:
        self.destroy()

        import frames.AdminAllResults

        all_results_frame = frames.AdminAllResults.AdminAllResults(self.window_attribute, self.columns_names,
                                                         border_width=15, border_color="#006600",
                                                         fg_color="#FFFFFF", corner_radius=30)

    def go_to_editor(self) -> NoReturn:
        self.destroy()

        import frames.Editor

        editor_frame = frames.Editor.Editor(self.window_attribute, self.columns_names, border_width=15, border_color="#006600",
                                                         fg_color="#FFFFFF", corner_radius=30)
