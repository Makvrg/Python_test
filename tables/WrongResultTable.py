from tkinter import ttk
import customtkinter as ctk
from typing import Any


class WrongResultTable(ttk.Treeview):
    def __init__(self, master: Any, frame_object: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.wrong_result_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                             bg_color="transparent", fg_color="#e4ffcf",
                                                             button_color="#169c02",
                                                             orientation="vertical",
                                                             command=self.yview,
                                                             width=25, hover=True, button_hover_color="#007D00")
        self.wrong_result_table_scrollbar.grid(row=0, column=1, sticky="ns", pady=0)
        self.configure(yscrollcommand=self.wrong_result_table_scrollbar.set)

        # Setting columns
        self.heading(frame_object.columns_names.columns_wrong_result[0], text='№',
                                      anchor="c")  # it is corresponding to column "errors_and_wrong_id"
        self.heading(frame_object.columns_names.columns_wrong_result[1], text='№ тестa',
                                      anchor="c")  # it is corresponding to column "score_id"
        self.heading(frame_object.columns_names.columns_wrong_result[2], text='Имя',
                                      anchor="c")  # it is corresponding to column "name_student"
        self.heading(frame_object.columns_names.columns_wrong_result[3], text='Тип',
                                      anchor="c")  # it is corresponding to column "topic_name"
        self.heading(frame_object.columns_names.columns_wrong_result[4], text='Задача',
                                      anchor="c")  # it is corresponding to column "task"
        self.heading(frame_object.columns_names.columns_wrong_result[5], text='Ответ',
                                      anchor="c")  # it is corresponding to column "student_answer"
        self.heading(frame_object.columns_names.columns_wrong_result[6], text='Верно',
                                      anchor="c")  # it is corresponding to column "true_answer"
        self.heading(frame_object.columns_names.columns_wrong_result[7], text='Причина',
                                      anchor="c")  # it is corresponding to column "comment"

        self.column(column=frame_object.columns_names.columns_wrong_result[0], width=60)
        self.column(column=frame_object.columns_names.columns_wrong_result[1], width=110)
        self.column(column=frame_object.columns_names.columns_wrong_result[2], width=110)
        self.column(column=frame_object.columns_names.columns_wrong_result[3], width=150)
        self.column(column=frame_object.columns_names.columns_wrong_result[4], width=200)
        self.column(column=frame_object.columns_names.columns_wrong_result[5], width=120)
        self.column(column=frame_object.columns_names.columns_wrong_result[6], width=120)
        self.column(column=frame_object.columns_names.columns_wrong_result[7], width=150)
