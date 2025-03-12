from tkinter import ttk
import customtkinter as ctk
from typing import Any


class TopicTable(ttk.Treeview):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Create scrollbar
        self.topic_table_scrollbar = ctk.CTkScrollbar(master, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.topic_table_scrollbar.grid(row=1, column=3, sticky="ns", padx=(0, 18), pady=(0, 12))
        self.configure(yscrollcommand=self.topic_table_scrollbar.set)

        # Setting columns
        self.heading(master.columns_names.columns_topic[0], text='№ в БД',
                                      anchor="c")  # it is corresponding to column "topic_id"`
        self.heading(master.columns_names.columns_topic[1], text='Название типа',
                                      anchor="c")  # it is corresponding to column "topic_name"


        self.column(column=master.columns_names.columns_topic[0], width=100)
        self.column(column=master.columns_names.columns_topic[1], width=350)

    def get_selected_row(self):
        selected_item = self.selection()
        if selected_item:
            item_data = self.item(selected_item[0])['values']
            return item_data
        else:
            pass
