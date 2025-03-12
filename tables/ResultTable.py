from tkinter import ttk
import customtkinter as ctk
from typing import Any


class ResultTable(ttk.Treeview):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.result_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                       bg_color="transparent", fg_color="#e4ffcf",
                                                       button_color="#169c02",
                                                       orientation="vertical", command=self.yview,
                                                       width=25, hover=True, button_hover_color="#007D00")
        self.result_table_scrollbar.grid(row=2, column=2, sticky="ns", padx=(0, 25), pady=(0, 19))
        self.configure(yscrollcommand=self.result_table_scrollbar.set)

        # Setting columns
        self.heading(master.columns_names.columns_result[0], text="Задача", anchor="c")
        self.heading(master.columns_names.columns_result[1], text="Ваш ответ", anchor="c")
        self.heading(master.columns_names.columns_result[2], text="Правильный ответ", anchor="c")

        self.column(column=master.columns_names.columns_result[0], width=100)
        self.column(column=master.columns_names.columns_result[1], width=300)
        self.column(column=master.columns_names.columns_result[2], width=300)

        self.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=(30, 0), pady=(0, 25))