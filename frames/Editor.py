import customtkinter as ctk
from typing import Any, NoReturn
import tables.TopicTable


class Editor(ctk.CTkFrame):
    def __init__(self, master: Any, columns_names, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = columns_names

        self.editor_table = tables.TopicTable.TopicTable(self, self, style="2.Treeview",
                                                                     columns=self.columns_names.columns_max_result,
                                                                     show="headings",
                                                                     selectmode="extended")  # it is corresponding to tables  in database
        self.max_result_table.grid(row=0, column=0, sticky="nsew", pady=0)

        self.max_result_table.tag_configure("max_result_table_tag_1", font=("Fira Sans SemiBold", 20))
        self.max_result_table.tag_configure("max_result_table_tag_2", font=("Fira Sans SemiBold", 20),
                                            background="#e6ffd4")


    # Methods
    def back_to_admin_menu(self) -> NoReturn:
        self.destroy()

        import frames.AdminMenu

        first_frame = frames.AdminMenu.AdminMenu(self.window_attribute, border_width=15, border_color="#006600",
                                               fg_color="#FFFFFF", corner_radius=30)
