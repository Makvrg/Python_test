import customtkinter as ctk
from tkinter import ttk
from typing import Any, NoReturn, Tuple
import tables.TopicTable
from functions import db_handlers as dbh


class TopicList(ctk.CTkFrame):
    def __init__(self, master: Any, columns_names, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = columns_names

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=10)
        self.rowconfigure(index=2, weight=2)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)

        self.info_label = ctk.CTkLabel(self, text="Выберите для управления существующий тип задач или создайте новый",
                                       font=("Fira Sans SemiBold", 25), text_color="#000000",
                                       fg_color="#81d481", width=380, height=30, corner_radius=10)
        self.info_label.grid(row=0, column=0, columnspan=3, sticky="sw", padx=24, pady=[20, 10])

        # Create style
        self.table_style = ttk.Style()
        self.table_style.theme_use("default")
        self.table_style.configure("1.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('1.Treeview', background=[('selected', '#ebff69')], foreground=[("selected", "black")])
        self.table_style.configure("1.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Fira Sans SemiBold", 28))
        self.table_style.map("1.Treeview.Heading", background=[('active', '#5cd649')])


        # Treeview creating
        self.topic_table = tables.TopicTable.TopicTable(self, style="1.Treeview",
                                                           columns=self.columns_names.columns_topic,
                                                           show="headings", selectmode="browse")
        self.topic_table.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=(22, 0), pady=(0, 15))

        # Tag create
        self.topic_table.tag_configure("topic_table_tag_1", font=("Fira Sans SemiBold", 23))
        self.topic_table.tag_configure("topic_table_tag_2", font=("Fira Sans SemiBold", 23),
                                            background="#e6ffd4")

        # Filling topic_table
        self.k = 1
        for row in dbh.get_rows("topic_table"):
            if self.k % 2 == 0:
                self.topic_table.insert("", "end", values=row, tags="topic_table_tag_1")
            else:
                self.topic_table.insert("", "end", values=row, tags="topic_table_tag_2")
            self.k += 1

        # Choice button
        self.back_button = ctk.CTkButton(self, command=self.back_to_admin_menu, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 33), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=2, column=0, sticky="nw", padx=[25, 15], pady=[10, 4])

        self.my_topic_button = ctk.CTkButton(self, command=self.my_topic, text="Новый тип",
                                                     fg_color="#009900", height=50, width=330,
                                                     font=("Fira Sans Bold", 33), border_width=3,
                                                     border_color="#006600", corner_radius=5,
                                                     hover_color="#007D00", text_color="#FFF")
        self.my_topic_button.grid(row=2, column=1, sticky="ne", padx=[15, 15], pady=[8, 4])

        self.chose_from_table_button = ctk.CTkButton(self, command=self.chose_from_table, text="Тип из таблицы",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 33), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.chose_from_table_button.grid(row=2, column=2, columnspan=2, sticky="nw", padx=[15, 25], pady=[8, 4])





    # Methods
    def chose_from_table(self) -> NoReturn:
        selected_item: Tuple[int, str] = self.topic_table.get_selected_row()
        if selected_item:
            self.destroy()

            import frames.Editor

            editor_frame = frames.Editor.Editor(self.window_attribute, self.columns_names, selected_item,
                            border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)
        else:
            pass


    def my_topic(self) -> NoReturn:
        self.destroy()

        import frames.NewTopic

        new_t_frame = frames.NewTopic.NewTopic(self.window_attribute, border_width=15,
                                                border_color="#006600", fg_color="#FFFFFF",
                                                corner_radius=30)


    def back_to_admin_menu(self) -> NoReturn:
        self.destroy()

        import frames.AdminMenu

        admin_frame = frames.AdminMenu.AdminMenu(self.window_attribute, border_width=15, border_color="#006600",
                                               fg_color="#FFFFFF", corner_radius=30)
