import customtkinter as ctk
from typing import Any, NoReturn
from functions import db_handlers as dbh
from functions import image_initialization as ii
import global_variables as gv


class NewTopic(ctk.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Grid configuration
        self.rowconfigure(index=0, weight=10)
        self.rowconfigure(index=1, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.new_topic_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=90)
        self.new_topic_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=25, pady=[27, 10])
        self.new_topic_label = ctk.CTkLabel(self.new_topic_frame, text="Новый тип:",
                                       font=("Fira Sans SemiBold", 35), text_color="#000000")
        self.new_topic_label.grid(row=0, column=0, sticky="ne", padx=[15, 0], pady=[30, 5])

        self.new_topic_entry = ctk.CTkEntry(self.new_topic_frame, font=("Tahoma", 35), width=500, height=71,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.new_topic_entry.grid(row=0, column=1, sticky="n", padx=[10, 10], pady=10)

        self.new_topic_button = ctk.CTkButton(self.new_topic_frame, command=self.create_new_topic, height=70, width=70,
                                         fg_color="#009900", border_width=3,
                                         border_color="#006600", corner_radius=5, text="",
                                         hover_color="#007D00", image=ii.get_button_save_image())
        self.new_topic_button.grid(row=0, column=2, sticky="nw", padx=[0, 15], pady=10)

        self.back_button = ctk.CTkButton(self, command=self.back_to_topic_list, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 33), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=1, column=0, sticky="nw", padx=[25, 15], pady=[10, 4])


    def create_new_topic(self) -> NoReturn:
        new_topic_name = self.new_topic_entry.get().strip()

        if new_topic_name == "":
            self.new_topic_entry.configure(fg_color="#ffc9c9")
        elif new_topic_name in dbh.get_topics():
            self.new_topic_entry.configure(fg_color="#ffc9c9")
        else:
            dbh.create_new_topic(new_topic_name)
            self.new_topic_entry.configure(fg_color="#d9ffdf")


    def back_to_topic_list(self) -> NoReturn:
        self.destroy()

        import frames.TopicList

        topic_list_frame = frames.TopicList.TopicList(self.window_attribute, gv.columns_names, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)