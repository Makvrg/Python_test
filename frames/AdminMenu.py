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
        self.rowconfigure(index=2, weight=3)
        self.rowconfigure(index=3, weight=3)
        self.columnconfigure(index=0, weight=1)

        self.menu_label = ctk.CTkLabel(self, text="Админ-меню",
                                       font=("Fira Sans SemiBold", 40), text_color="#000000",
                                       fg_color="#65bf65",
                                       height=50, corner_radius=10, width=180)
        self.menu_label.grid(row=0, column=0, sticky="nw", padx=[30, 0], pady=[30, 0])

        self.all_results_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=100)
        self.all_results_frame.grid(row=1, column=0, sticky="nsew", padx=25, pady=50)
        self.all_results_button = ctk.CTkButton(self.all_results_frame, command=self.go_to_all_results, text="Все результаты",
                                                fg_color="#009900", height=75, width=405, border_width=3,
                                                border_color="#006600", corner_radius=5, text_color="#FFF",
                                                font=("Fira Sans Bold", 50), hover_color="#007D00")
        self.all_results_button.pack(side="left", anchor="w", padx=10, pady=10)

        self.topic_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3",
                                              height=160)
        self.topic_frame.grid(row=2, column=0, sticky="nsew", padx=25, pady=50)
        self.topic_button = ctk.CTkButton(self.topic_frame, command=self.go_to_topic, text="Редактировать задания и типы",
                                                fg_color="#009900", height=75, width=760, border_width=3,
                                                border_color="#006600", corner_radius=5, text_color="#FFF",
                                                font=("Fira Sans Bold", 50), hover_color="#007D00")
        self.topic_button.pack(side="left", anchor="w", padx=10, pady=10)

        self.back_button = ctk.CTkButton(self, command=self.back_to_password, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 50), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=3, column=0, sticky="sw", padx=30, pady=[14, 36])

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

    def go_to_topic(self) -> NoReturn:
        self.destroy()

        import frames.TopicList

        topic_list_frame = frames.TopicList.TopicList(self.window_attribute, self.columns_names, border_width=15, border_color="#006600",
                                                         fg_color="#FFFFFF", corner_radius=30)
