from tkinter import ttk
import customtkinter as ctk
from typing import Any


class TaskAndExerciseTable(ttk.Treeview):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.task_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.task_table_scrollbar.grid(row=1, column=3, sticky="ns", padx=(0, 18), pady=(0, 8))
        self.configure(yscrollcommand=self.task_table_scrollbar.set)

        # Setting columns
        self.heading(master.columns_names.columns_task[0], text='№ в БД',
                                      anchor="c")  # it is corresponding to column "task_and_exercise_id"`
        self.heading(master.columns_names.columns_task[1], text='Задача',
                                      anchor="c")  # it is corresponding to column "task"
        self.heading(master.columns_names.columns_task[2], text='Задание',
                                      anchor="c")  # it is corresponding to column "exercise_name"
        self.heading(master.columns_names.columns_task[3], text='Ответ',
                                      anchor="c")  # it is corresponding to column "task_answer"


        self.column(column=master.columns_names.columns_task[0], width=20)
        self.column(column=master.columns_names.columns_task[1], width=150)
        self.column(column=master.columns_names.columns_task[2], width=150)
        self.column(column=master.columns_names.columns_task[3], width=50)

    def get_selected_ids(self):
        selected_item = self.selection()  # Ids
        if selected_item:
            sel_rows = []
            for ids in selected_item:
                db_id = self.item(ids)['values'][0]
                sel_rows.append(db_id)

            return sel_rows
        else:
            pass