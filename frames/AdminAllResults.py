import customtkinter as ctk
from functions import handlers as hd, image_initialization as ii
from functions import db_handlers as dbh
from tkinter import ttk
from typing import Any, NoReturn
import tables.AllResultTable, tables.MaxResultTable, tables.WrongResultTable


class AdminAllResults(ctk.CTkFrame):
    def __init__(self, master: Any, columns_names, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

        # Create attribute with columns_names
        self.columns_names = columns_names

        # Create style
        self.notebook_style = ttk.Style()
        self.notebook_style.theme_use("default")
        self.notebook_style.configure("1.TNotebook",
                                      background="#FFFFFF", foreground="#FFFFFF",
                                      fieldbackground="white",
                                      bordercolor="#FFFFFF", relief="flat")
        self.notebook_style.configure('1.TNotebook.Tab', background='#73cf48', foreground='black',
                                      font=("Fira Sans SemiBold", 16))
        self.notebook_style.map('1.TNotebook.Tab', background=[("selected", '#4bb519')])

        # Create Notebook
        self.rowconfigure(index=0, weight=100)
        self.rowconfigure(index=1, weight=10)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.tabs = ttk.Notebook(self, style="1.TNotebook")
        self.tabs.grid(sticky="nsew", row=0, column=0, columnspan=2, padx=19, pady=(19, 0))


        self.frame1 = ctk.CTkFrame(master=self.tabs, border_width=3, bg_color="transparent",
                                   fg_color="#FFFFFF", border_color="#FFFFFF")
        self.frame2 = ctk.CTkFrame(master=self.tabs, border_width=3, bg_color="transparent",
                                   fg_color="#FFFFFF", border_color="#FFFFFF")
        self.frame3 = ctk.CTkFrame(master=self.tabs, border_width=3, bg_color="transparent",
                                   fg_color="#FFFFFF", border_color="#FFFFFF")
        self.frame1.pack(expand=True, fill="both")
        self.frame2.pack(expand=True, fill="both")
        self.frame3.pack(expand=True, fill="both")

        # Grid setting
        self.frame1.rowconfigure(index=0, weight=1)
        self.frame1.columnconfigure(index=0, weight=1)

        self.frame2.rowconfigure(index=0, weight=1)
        self.frame2.columnconfigure(index=0, weight=1)

        self.frame3.rowconfigure(index=0, weight=1)
        self.frame3.columnconfigure(index=0, weight=1)

        # Image initialization
        global n_star, n_trophy, n_wrong_error
        n_star = ii.get_notebook_star_image()
        n_trophy = ii.get_notebook_trophy_image()
        n_wrong_error = ii.get_wrong_error_image()

        self.tabs.add(child=self.frame1, text="Все результаты", image=n_star, compound="left")
        self.tabs.add(child=self.frame2, text="Лучшие результаты", image=n_trophy, compound="left")
        self.tabs.add(child=self.frame3, text="Ошибки", image=n_wrong_error, compound="left")

        # Create style
        self.table_style = ttk.Style()
        self.table_style.theme_use("default")
        self.table_style.configure("2.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('2.Treeview', background=[('selected', '#f1ff94')], foreground=[("selected", "black")])
        self.table_style.configure("2.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Fira Sans SemiBold", 22))
        self.table_style.map("2.Treeview.Heading", background=[('active', '#5cd649')])

        # Information loading to frame1, frame2 and frame3
        # Treeview and Scrollbar creating №1
        self.all_result_table = tables.AllResultTable.AllResultTable(self.frame1, self, style="2.Treeview",
                                                                     columns=self.columns_names.columns_all_result,
                                                                     show="headings",
                                                                     selectmode="extended")  # it is corresponding to table "score" in database
        self.all_result_table.grid(row=0, column=0, sticky="nsew", pady=0)


        # Treeview and Scrollbar creating №2
        self.max_result_table = tables.MaxResultTable.MaxResultTable(self.frame2, self, style="2.Treeview",
                                                                     columns=self.columns_names.columns_max_result,
                                                                     show="headings",
                                                                     selectmode="extended")  # it is corresponding to table "max_score" in database
        self.max_result_table.grid(row=0, column=0, sticky="nsew", pady=0)

        # Treeview and Scrollbar creating №3
        self.wrong_result_table = tables.WrongResultTable.WrongResultTable(self.frame3, self, style="2.Treeview",
                                             columns=self.columns_names.columns_wrong_result,
                                             show="headings",
                                             selectmode="extended")  # it is corresponding to table "errors_and_wrong" in database
        self.wrong_result_table.grid(row=0, column=0, sticky="nsew", pady=0)


        # Tag create
        self.all_result_table.tag_configure("all_result_table_tag_1", font=("Fira Sans SemiBold", 19))
        self.all_result_table.tag_configure("all_result_table_tag_2", font=("Fira Sans SemiBold", 19),
                           background="#e6ffd4")

        self.max_result_table.tag_configure("max_result_table_tag_1", font=("Fira Sans SemiBold", 20))
        self.max_result_table.tag_configure("max_result_table_tag_2", font=("Fira Sans SemiBold", 20),
                           background="#e6ffd4")

        self.wrong_result_table.tag_configure("wrong_result_table_tag_1", font=("Fira Sans SemiBold", 18))
        self.wrong_result_table.tag_configure("wrong_result_table_tag_2", font=("Fira Sans SemiBold", 18),
                           background="#e6ffd4")


        # Button
        self.back_button = ctk.CTkButton(self, command=self.back_to_admin_menu, text="Назад",
                                         fg_color="#009900", height=50, width=330,
                                         font=("Fira Sans Bold", 40), border_width=3,
                                         border_color="#006600", corner_radius=5,
                                         hover_color="#007D00", text_color="#FFF")
        self.back_button.grid(row=1, column=0, sticky="nw", padx=20, pady=[8, 6])

        self.close_program_button_1 = ctk.CTkButton(self, command=lambda: hd.finish(self.window_attribute),
                                                    text="Выйти", text_color="#FFF", fg_color="#009900",
                                                    height=50, width=330, border_width=3,
                                                    border_color="#006600", corner_radius=5,
                                                    hover_color="#007D00", font=("Fira Sans Bold", 40))
        self.close_program_button_1.grid(row=1, column=1, columnspan=2, sticky="ne", padx=20, pady=[8, 6])

        # Filling all_result_table
        self.k = 1
        for row in dbh.get_rows("all_result_table"):
            if self.k % 2 == 0:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_1")
            else:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_2")
            self.k += 1

        # Filling max_result_table
        self.k = 1
        for row in dbh.get_rows("max_result_table"):
            if self.k % 2 == 0:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_1")
            else:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_2")
            self.k += 1

        # Filling wrong_result_table
        self.k = 1
        for row in dbh.get_rows("wrong_result_table"):
            if self.k % 2 == 0:
                self.wrong_result_table.insert("", "end", values=row, tags="wrong_result_table_tag_1")
            else:
                self.wrong_result_table.insert("", "end", values=row, tags="wrong_result_table_tag_2")
            self.k += 1


    # Methods
    def back_to_admin_menu(self) -> NoReturn:
        self.destroy()

        import frames.AdminMenu

        admin_frame = frames.AdminMenu.AdminMenu(self.window_attribute, border_width=15, border_color="#006600",
                                                       fg_color="#FFFFFF", corner_radius=30)
