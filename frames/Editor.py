import customtkinter as ctk
from tkinter import ttk
from typing import Any, NoReturn, Tuple
import tables.TaskAndExerciseTable
from functions import db_handlers as dbh
from functions import image_initialization as ii


class Editor(ctk.CTkFrame):
    def __init__(self, master: Any, columns_names, choice_type, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = columns_names

        # Create attribute with choice_type
        self.choice_type: Tuple[int, str] = choice_type

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=10)
        self.rowconfigure(index=2, weight=2)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)
        self.columnconfigure(index=2, weight=2)

        self.rename_frame = ctk.CTkFrame(self, border_width=1, border_color="#000000", fg_color="#ecffe3", height=90)
        self.rename_frame.grid(row=0, column=0, columnspan=4, sticky="ew", padx=25, pady=[27, 10])
        self.rename_label = ctk.CTkLabel(self.rename_frame, text="Переименовать:",
                                       font=("Fira Sans SemiBold", 35), text_color="#000000")
        self.rename_label.grid(row=0, column=0, sticky="ne", padx=[15, 0], pady=[30, 5])

        self.rename_entry = ctk.CTkEntry(self.rename_frame, font=("Tahoma", 35), width=500, height=71,
                                       fg_color="#FFFFFF", text_color="#212121", border_color="#818c81")
        self.rename_entry.grid(row=0, column=1, sticky="n", padx=[10, 10], pady=10)
        self.rename_entry.insert(0, self.choice_type[1])
        self.rename_button = ctk.CTkButton(self.rename_frame, command=self.rename, height=70, width=70,
                                         fg_color="#009900", border_width=3,
                                         border_color="#006600", corner_radius=5, text="",
                                         hover_color="#007D00", image=ii.get_button_save_image())
        self.rename_button.grid(row=0, column=2, sticky="nw", padx=[0, 15], pady=10)

        # Task table
        self.table_style = ttk.Style()
        self.table_style.theme_use("default")
        self.table_style.configure("3.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('3.Treeview', background=[('selected', '#ebff69')], foreground=[("selected", "black")])
        self.table_style.configure("3.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Fira Sans SemiBold", 23))
        self.table_style.map("3.Treeview.Heading", background=[('active', '#5cd649')])

        # Treeview creating
        self.task_table = tables.TaskAndExerciseTable.TaskAndExerciseTable(self, style="3.Treeview",
                                                        columns=self.columns_names.columns_task,
                                                        show="headings", selectmode="extended")
        self.task_table.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=(22, 0), pady=(0, 10))

        # Tag create
        self.task_table.tag_configure("task_table_tag_1", font=("Fira Sans SemiBold", 20))
        self.task_table.tag_configure("task_table_tag_2", font=("Fira Sans SemiBold", 20),
                                       background="#e6ffd4")

        # Filling topic_table
        self.k = 1
        for row in dbh.get_rows("task_table", self.choice_type[0]):
            if self.k % 2 == 0:
                self.task_table.insert("", "end", values=row, tags="task_table_tag_1")
            else:
                self.task_table.insert("", "end", values=row, tags="task_table_tag_2")
            self.k += 1


        self.back_button = ctk.CTkButton(self, command=self.back_to_topic, text="Назад",
                                         fg_color="#009900", height=65, width=250,
                                         font=("Fira Sans Bold", 37), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=3, column=0, sticky="nw", padx=[30, 5], pady=[3, 30])

        self.change_count = 0
        self.change_button = ctk.CTkButton(self, command=self.change, text="",
                                          fg_color="#009900", height=60, width=60,
                                          border_width=3, border_color="#006600",
                                          corner_radius=5, hover_color="#007D00",
                                          image=ii.get_change_image())
        self.change_button.grid(row=3, column=1, sticky="n", pady=[3, 30])

        self.delete_type_count = 0
        self.delete_tasks_count = 0
        self.functional_button = ctk.CTkButton(self, command=self.go_to_add_tasks, text="Добавить новые задачи",
                                         fg_color="#009900", height=65, width=500,
                                         font=("Fira Sans Bold", 37), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.functional_button.grid(row=3, column=2, columnspan=2, sticky="ne", padx=[5, 30], pady=[3, 30])


    # Methods
    def rename(self) -> NoReturn:
        new_name = self.rename_entry.get().strip()
        if new_name != self.choice_type[1] and new_name != "":
            dbh.rename_topic(self.choice_type[0], new_name)
            self.choice_type = (self.choice_type[0], new_name)
            self.rename_entry.configure(fg_color="#d9ffdf")


    def delete_type(self) -> NoReturn:
        self.delete_type_count += 1
        if self.delete_type_count >= 5:
            dbh.delete_topic(self.choice_type[0])
            self.destroy()

            import frames.TopicList

            topic_frame = frames.TopicList.TopicList(self.window_attribute, self.columns_names,
                                border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)

    def change(self):
        self.change_count += 1

        if self.change_count % 3 == 0:
            # Add new tasks
            self.functional_button.configure(text="Добавить новые задачи",
                                             command=self.go_to_add_tasks, fg_color="#009900",
                                             border_color="#006600", hover_color="#007D00")

        elif self.change_count % 3 == 1:
            # Delete tasks
            self.functional_button.configure(text="Удалить задачи (наж. 5 раз)",
                                             command=self.delete_selected_tasks, fg_color="#f01120",
                                             border_color="#000", hover_color="#d11320")
            self.delete_tasks_count = 0

        elif self.change_count % 3 == 2:
            # Delete types button
            self.functional_button.configure(text="Удалить тип (нажать 5 раз)",
                                             command=self.delete_type, fg_color="#bd0f1b",
                                             border_color="#000", hover_color="#9e020c")
            self.delete_type_count = 0


    def go_to_add_tasks(self):
        self.destroy()

        import frames.NewTasks

        editor_frame = frames.NewTasks.NewTasks(self.window_attribute, self.columns_names, self.choice_type,
                              border_width=15, border_color="#006600", fg_color="#FFFFFF",
                              corner_radius=30)


    def delete_selected_tasks(self):
        self.delete_tasks_count += 1
        if self.delete_tasks_count >= 5:
            ids = self.task_table.get_selected_ids()
            if not (ids is None):
                dbh.delete_tasks(ids)
                self.destroy()

                editor_frame = Editor(self.window_attribute, self.columns_names, self.choice_type,
                                                    border_width=15, border_color="#006600", fg_color="#FFFFFF",
                                                    corner_radius=30)


    def back_to_topic(self) -> NoReturn:
        self.destroy()

        import frames.TopicList

        topic_frame = frames.TopicList.TopicList(self.window_attribute, self.columns_names, border_width=15, border_color="#006600",
                                               fg_color="#FFFFFF", corner_radius=30)