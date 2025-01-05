import customtkinter as ctk
import Global_variable as gv
import Handlers as hd
from tkinter import ttk
import Image_initialization as Ii


class AllResultsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Create style
        self.notebook_style = ttk.Style()  # Need refactor
        self.notebook_style.theme_use("default")
        self.notebook_style.configure("1.TNotebook",
                                      background="#FFFFFF", foreground="#FFFFFF",
                                      fieldbackground="white",
                                      bordercolor="#FFFFFF", relief="flat")
        self.notebook_style.configure('1.TNotebook.Tab', background='#73cf48', foreground='black',
                                      font=("Calibri", 18, "bold"))
        self.notebook_style.map('1.TNotebook.Tab', background=[("selected", '#319602')])

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

        global c_star, c_trophy
        c_star = Ii.get_column_star_image()
        c_trophy = Ii.get_column_trophy_image()

        self.tabs.add(child=self.frame1, image=c_star)
        self.tabs.add(child=self.frame2, image=c_trophy)

        # Create style
        self.table_style = ttk.Style() # Need refactor
        self.table_style.theme_use("default")
        self.table_style.configure("2.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('2.Treeview', background=[('selected', '#f1ff94')], foreground=[("selected", "black")])
        self.table_style.configure("2.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Calibri", 25, "bold"))
        self.table_style.map("2.Treeview.Heading", background=[('active', '#5cd649')])

        # Information loading to frame1 and frame2
        # Treeview and Scrollbar creating №1
        self.all_result_table = ttk.Treeview(self.frame1, style="2.Treeview", columns=gv.columns_all_result,
                                             show="headings", selectmode="extended")
        self.all_result_table_scrollbar = ctk.CTkScrollbar(self.frame1, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf", button_color="#169c02",
                                                           orientation="vertical", command=self.all_result_table.yview,
                                                           width=25, hover=False)
        self.all_result_table_scrollbar.grid(row=0, column=2, sticky="nsew", pady=0)
        self.all_result_table.configure(yscrollcommand=self.all_result_table_scrollbar.set)


        # Tag create
        self.all_result_table.tag_configure("all_result_table_tag_1", font=("Calibri", 20, "bold"))
        self.all_result_table.tag_configure("all_result_table_tag_2", font=("Calibri", 20, "bold"), background="#e6ffd4")

        # Setting columns
        self.all_result_table.heading(gv.columns_all_result[0], text='№', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[1], text='Имя', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[2], text='Тип', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[3], text='Результат', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[4], text='Качество', anchor="c")
        self.all_result_table.heading(gv.columns_all_result[5], text='Подряд', anchor="c")

        self.all_result_table.column(column=gv.columns_all_result[0], width=30)
        self.all_result_table.column(column=gv.columns_all_result[1], width=150)
        self.all_result_table.column(column=gv.columns_all_result[2], width=300)
        self.all_result_table.column(column=gv.columns_all_result[3], width=95)
        self.all_result_table.column(column=gv.columns_all_result[4], width=80)
        self.all_result_table.column(column=gv.columns_all_result[5], width=80)

        self.all_result_table.grid(row=0, column=0, sticky="nsew", pady=0)

        # Treeview and Scrollbar creating №2
        self.max_result_table = ttk.Treeview(self.frame2, style="2.Treeview", columns=gv.columns_max_result,
                                             show="headings", selectmode="extended")
        self.max_result_table_scrollbar = ctk.CTkScrollbar(self.frame2, border_spacing=6, minimum_pixel_length=100,
                                                           bg_color="transparent", fg_color="#e4ffcf",
                                                           button_color="#169c02",
                                                           orientation="vertical", command=self.max_result_table.yview,
                                                           width=25, hover=False)
        self.max_result_table_scrollbar.grid(row=0, column=2, sticky="nsew", pady=0)
        self.max_result_table.configure(yscrollcommand=self.max_result_table_scrollbar.set)

        # Tag create
        self.max_result_table.tag_configure("max_result_table_tag_1", font=("Calibri", 20, "bold"))
        self.max_result_table.tag_configure("max_result_table_tag_2", font=("Calibri", 20, "bold"), background="#e6ffd4")

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
        self.back_button = ctk.CTkButton(self, command=self.back_to_result, text="",
                                         fg_color="#009900", height=50, width=330,
                                         image=Ii.get_taskframe_button_previous_image(), border_width=3,
                                         border_color="#006600", corner_radius=5, hover_color="#007D00")
        self.back_button.grid(row=1, column=0, sticky="nw", padx=20, pady=[8, 6])

        self.close_program_button_1 = ctk.CTkButton(self, command=finish, text="",
                                                    fg_color="#009900", height=50, width=330,
                                                    image=Ii.get_button_finish_image(), border_width=3,
                                                    border_color="#006600", corner_radius=5, hover_color="#007D00")
        self.close_program_button_1.grid(row=1, column=1, columnspan=2, sticky="ne", padx=20, pady=[8, 6])

        # Row insert
        self.k = 1
        for row in hd.get_rows("all_result_table"):
            if self.k % 2 == 0:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_1")
            else:
                self.all_result_table.insert("", "end", values=row, tags="all_result_table_tag_2")
            self.k += 1

        self.k = 1
        for row in hd.get_rows("max_result_table"):
            if self.k % 2 == 0:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_1")
            else:
                self.max_result_table.insert("", "end", values=row, tags="max_result_table_tag_2")
            self.k += 1


    # Methods
    def back_to_result(self):
        self.destroy()
        self.result_frame = ResultFrame(app, border_width=15, border_color="#006600",
                                        fg_color="#FFFFFF", corner_radius=30)
