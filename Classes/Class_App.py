import customtkinter as ctk
import Image_initialization as Ii
from Classes.Class_InfoFrame import InfoFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Математический тренажер")
        self.geometry("1000x700+360+150")
        self.configure(fg_color="#CCFFCC")

        # Theme and mode setting
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("light")

        self.main_frame = ctk.CTkFrame(self, border_width=15, border_color="#006600",
                                       fg_color="#FFFFFF", corner_radius=30)
        self.main_frame.pack(anchor="center", expand=True, fill="both", padx=15, pady=10)

        self.hallo_label = ctk.CTkLabel(self.main_frame, image=Ii.get_first_display_image(),
                                        fg_color="#FFFFFF", text="")
        self.hallo_label.pack(side="top", pady=[50, 0])
        self.go_button = ctk.CTkButton(self.main_frame, command=self.goto_info,
                                       fg_color="#009900", height=95, width=400,
                                       border_width=3, border_color="#006600", corner_radius=5,
                                       image=Ii.get_button_1_image(), text="", hover_color="#007D00")
        self.go_button.pack(side="bottom", pady=[0, 150])

    def goto_info(self):
        self.main_frame.destroy()
        self.info_frame = InfoFrame(self, border_width=15, border_color="#006600", fg_color="#FFFFFF", corner_radius=30)