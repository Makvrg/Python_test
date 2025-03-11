from tkinter import ttk
import customtkinter as ctk
from typing import Any


class TopicTable(ttk.Treeview):
    def __init__(self, master: Any, frame_object: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.max_result_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.max_result_table_scrollbar.grid(row=0, column=1, sticky="ns", pady=0)
        self.configure(yscrollcommand=self.max_result_table_scrollbar.set)

        # Setting columns
        self.heading(frame_object.columns_names.columns_max_result[0], text='№',
                                      anchor="c")  # it is corresponding to column "max_score_id"`
        self.heading(frame_object.columns_names.columns_max_result[1], text='Имя',
                                      anchor="c")  # it is corresponding to column "name_student"
        self.heading(frame_object.columns_names.columns_max_result[2], text='Тип',
                                      anchor="c")  # it is corresponding to column "topic_name"
        self.heading(frame_object.columns_names.columns_max_result[3], text='Подряд',
                                      anchor="c")  # it is corresponding to column "in_a_row"
        self.heading(frame_object.columns_names.columns_max_result[4], text='Дата и время',
                                      anchor="c")  # it is corresponding to column "date"

        self.column(column=frame_object.columns_names.columns_max_result[0], width=70)
        self.column(column=frame_object.columns_names.columns_max_result[1], width=270)
        self.column(column=frame_object.columns_names.columns_max_result[2], width=200)
        self.column(column=frame_object.columns_names.columns_max_result[3], width=100)
        self.column(column=frame_object.columns_names.columns_max_result[4], width=220)