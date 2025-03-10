from tkinter import ttk
import customtkinter as ctk
from typing import Any


class AllResultTable(ttk.Treeview):
    def __init__(self, master: Any, frame_object: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.all_result_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.all_result_table_scrollbar.grid(row=0, column=1, sticky="ns", pady=0)
        self.configure(yscrollcommand=self.all_result_table_scrollbar.set)

        # Setting columns
        self.heading(frame_object.columns_names.columns_all_result[0], text='№',
                                      anchor="c")  # it is corresponding to column "score_id"
        self.heading(frame_object.columns_names.columns_all_result[1], text='Имя',
                                      anchor="c")  # it is corresponding to column "name_student"
        self.heading(frame_object.columns_names.columns_all_result[2], text='Тип',
                                      anchor="c")  # it is corresponding to column "topic_name"
        self.heading(frame_object.columns_names.columns_all_result[3], text='Рез-т',
                                      anchor="c")  # it is corresponding to columns "abs_quantity" and "all_quantity"
        self.heading(frame_object.columns_names.columns_all_result[4], text='Кач-во',
                                      anchor="c")  # it is corresponding to column "ratio"
        self.heading(frame_object.columns_names.columns_all_result[5], text='Подряд',
                                      anchor="c")  # it is corresponding to column "in_a_row"
        self.heading(frame_object.columns_names.columns_all_result[6], text='Дата и время',
                                      anchor="c")  # it is corresponding to column "date"

        self.column(column=frame_object.columns_names.columns_all_result[0], width=55)
        self.column(column=frame_object.columns_names.columns_all_result[1], width=200)
        self.column(column=frame_object.columns_names.columns_all_result[2], width=150)
        self.column(column=frame_object.columns_names.columns_all_result[3], width=85)
        self.column(column=frame_object.columns_names.columns_all_result[4], width=70)
        self.column(column=frame_object.columns_names.columns_all_result[5], width=80)
        self.column(column=frame_object.columns_names.columns_all_result[6], width=210)
