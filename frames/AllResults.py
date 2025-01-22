import customtkinter as ctk
import global_variable as gv
from functions import handlers as hd
from functions import db_handlers as dbh
from tkinter import ttk
import image_initialization as ii
from typing import Any, NoReturn


class AllResults(ctk.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create attribute from window
        self.window_attribute = master

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
        self.frame1.pack(expand=True, fill="both")
        self.frame2.pack(expand=True, fill="both")

        # Grid setting
        self.frame1.rowconfigure(index=0, weight=1)
        self.frame1.columnconfigure(index=0, weight=1)

        self.frame2.rowconfigure(index=0, weight=1)
        self.frame2.columnconfigure(index=0, weight=1)

        global n_star, n_trophy
        n_star = ii.get_notebook_star_image()
        n_trophy = ii.get_notebook_trophy_image()

        self.tabs.add(child=self.frame1, text="Все результаты", image=n_star, compound="left")
        self.tabs.add(child=self.frame2, text="Лучшие результаты", image=n_trophy, compound="left")

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
                                   relief="flat", font=("Fira Sans SemiBold", 23))
        self.table_style.map("2.Treeview.Heading", background=[('active', '#5cd649')])

        # Information loading to frame1 and frame2
        # Treeview and Scrollbar creating №1
        self.all_result_table = ttk.Treeview(self.frame1, style="2.Treeview", columns=gv.columns_all_result,
                                             show="headings", selectmode="extended")
        self.all_result_table_scrollbar = ctk.CTkScrollbar(self.frame1, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf", button_color="#169c02",
                                                           orientation="vertical", command=self.all_result_table.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.all_result_table_scrollbar.grid(row=0, column=1, sticky="ns", pady=0)
        self.all_result_table.configure(yscrollcommand=self.all_result_table_scrollbar.set)


        # Tag create
        self.all_result_table.tag_configure("all_result_table_tag_1", font=("Fira Sans SemiBold", 19))
        self.all_result_table.tag_configure("all_result_table_tag_2", font=("Fira Sans SemiBold", 19), background="#e6ffd4")

        # Setting columns
        self.all_result_table.heading(gv.columns_all_result[0], text='№', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[1], text='Имя', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[2], text='Тип', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[3], text='Результат', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[4], text='Качество', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[5], text='Подряд', anchor="c")

        self.all_result_table.column(column=gv.columns_all_result[0], width=30)
        self.all_result_table.column(column=gv.columns_all_result[1], width=150)
        self.all_result_table.column(column=gv.columns_all_result[2], width=250)
        self.all_result_table.column(column=gv.columns_all_result[3], width=100)
        self.all_result_table.column(column=gv.columns_all_result[4], width=90)
        self.all_result_table.column(column=gv.columns_all_result[5], width=80)

        self.all_result_table.grid(row=0, column=0, sticky="nsew", pady=0)

        # Treeview and Scrollbar creating №2
        self.max_result_table = ttk.Treeview(self.frame2, style="2.Treeview", columns=gv.columns_max_result,
                                             show="headings", selectmode="extended")
        self.max_result_table_scrollbar = ctk.CTkScrollbar(self.frame2, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.max_result_table.yview,
                                                           width=25, hover=True, button_hover_color="#007D00")
        self.max_result_table_scrollbar.grid(row=0, column=1, sticky="ns", pady=0)
        self.max_result_table.configure(yscrollcommand=self.max_result_table_scrollbar.set)

        # Tag create
        self.max_result_table.tag_configure("max_result_table_tag_1", font=("Fira Sans SemiBold", 20))
        self.max_result_table.tag_configure("max_result_table_tag_2", font=("Fira Sans SemiBold", 20), background="#e6ffd4")

        # Setting columns
        self.max_result_table.heading(gv.columns_max_result[0], text='№', anchor="c")
        self.max_result_table.heading(gv.columns_max_result[1], text='Имя', anchor="c")
        self.max_result_table.heading(gv.columns_max_result[2], text='Тип', anchor="c")
        self.max_result_table.heading(gv.columns_max_result[3], text='Подряд', anchor="c")

        self.max_result_table.column(column=gv.columns_max_result[0], width=100)
        self.max_result_table.column(column=gv.columns_max_result[1], width=200)
        self.max_result_table.column(column=gv.columns_max_result[2], width=350)
        self.max_result_table.column(column=gv.columns_max_result[3], width=150)

        self.max_result_table.grid(row=0, column=0, sticky="nsew", pady=0)

        # Button
        self.back_button = ctk.CTkButton(self, command=self.back_to_result, text="Назад",
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

        # Row insert
        self.k = 1
        for row in dbh.get_rows("all_result_table"):
            if self.k % 2 == 0:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_1")
            else:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_2")
            self.k += 1

        self.k = 1
        for row in dbh.get_rows("max_result_table"):
            if self.k % 2 == 0:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_1")
            else:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_2")
            self.k += 1


    # Methods
    def back_to_result(self) -> NoReturn:
        self.destroy()

        import frames.Result
        result_frame = frames.Result.Result(self.window_attribute, border_width=15, border_color="#006600",
                                                       fg_color="#FFFFFF", corner_radius=30)
