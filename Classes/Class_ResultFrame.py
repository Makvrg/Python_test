import customtkinter as ctk
import Global_variable as gv
from tkinter import ttk
import Image_initialization as Ii


class ResultFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        # Grid configuration
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=2)
        self.rowconfigure(index=2, weight=100)
        self.rowconfigure(index=3, weight=2)
        self.rowconfigure(index=4, weight=2)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.title_label = ctk.CTkLabel(self, image=Ii.get_hallo_label_image(), text="")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="sw", padx=30, pady=[19, 13])

        self.result_label = ctk.CTkLabel(self, text=f"Вы решили {sum(gv.result)} из {gv.count_tasks} задач",
                                         font=("Arial", 35, "bold"), text_color="#000000",
                                         height=45, corner_radius=10, width=390, fg_color="#a5faa5")
        self.result_label.grid(row=1, column=0, columnspan=2, sticky="n", padx=30, pady=[0, 10])

        # Create style
        self.table_style = ttk.Style()  # Need refactor
        self.table_style.theme_use("default")
        self.table_style.configure("1.Treeview",
                                   background="#fcfffa", foreground="black",
                                   rowheight=45, fieldbackground="white",
                                   bordercolor="#3a5e29", relief="flat",
                                   borderwidth=1)
        self.table_style.map('1.Treeview', background=[('selected', '#f1ff94')], foreground=[("selected", "black")])
        self.table_style.configure("1.Treeview.Heading",
                                   background="#4bb519", foreground="black",
                                   relief="flat", font=("Calibri", 28, "bold"))
        self.table_style.map("1.Treeview.Heading", background=[('active', '#5cd649')])

        # Treeview creating
        self.result_table = ttk.Treeview(self, style="1.Treeview", columns=gv.columns,
                                         show="headings", selectmode="extended")
        # Tag create
        self.result_table.tag_configure("table_tag_true", font=("Calibri", 23, "bold"), background="#c5faac")
        self.result_table.tag_configure("table_tag_false", font=("Calibri", 23, "bold"), background="#fca4a4")

        # Setting columns
        global i1, i2, i3
        i1 = Ii.get_column_task_image()
        i2 = Ii.get_column_your_answer_image()
        i3 = Ii.get_column_true_answer_image()
        self.result_table.heading(gv.columns[0], image=i1)
        self.result_table.heading(gv.columns[1], image=i2)
        self.result_table.heading(gv.columns[2], image=i3)

        self.result_table.column(column=gv.columns[0], width=100)
        self.result_table.column(column=gv.columns[1], width=300)
        self.result_table.column(column=gv.columns[2], width=300)

        self.result_table.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=30, pady=(0, 25))

        # Insert rows
        for num in range(1, gv.count_tasks + 1):
            if gv.result[num - 1] == 1:  # True answer, so table row - green (use tags="table_tag_true")
                self.result_table.insert("", "end",
                                         values=(num, gv.answer[num], ", ".join(map(str, sorted(list(gv.officer_task_dict[num][1]))))),
                                         tags="table_tag_true")
            else:  # False answer, so table row - red (use tags="table_tag_false")
                self.result_table.insert("", "end",
                                         values=(num, gv.answer[num], ", ".join(map(str, sorted(list(gv.officer_task_dict[num][1]))))),
                                         tags="table_tag_false")

        # Label congratulations on new record
        if gv.new_record_flag is True:
            self.new_record_label = ctk.CTkLabel(self, text=f"Поздравляю! Вы побили свой рекорд по решённым\nподряд заданиям: {gv.old_true_in_a_row} >>> {gv.true_in_a_row}",
                                             font=("Arial", 33, "bold"), text_color="#000000",
                                             height=45, corner_radius=7, width=390, fg_color="#a5faa5")
            self.new_record_label.grid(row=3, column=0, columnspan=2, sticky="s", padx=35, pady=[0, 5])

        # Final button
        self.all_results_button = ctk.CTkButton(self, command=self.go_to_all_results, text="",
                                                fg_color="#009900", height=60, width=330, border_width=3,
                                                border_color="#006600", corner_radius=5,
                                                image=Ii.get_button_all_results_image(), hover_color="#007D00")
        self.all_results_button.grid(row=4, column=0, sticky="nw", padx=30, pady=[14, 28])

        self. close_program_button = ctk.CTkButton(self, command=finish, text="",
                                                   fg_color="#009900", height=60, width=330, border_width=3,
                                                   border_color="#006600", corner_radius=5,
                                                   image=Ii.get_button_finish_image(), hover_color="#007D00")
        self.close_program_button.grid(row=4, column=1, sticky="ne", padx=30, pady=[14, 28])

    def go_to_all_results(self):
        self.destroy()
        self.all_results_frame = AllResultsFrame(app, border_width=15, border_color="#006600",
                                                 fg_color="#FFFFFF", corner_radius=30)
