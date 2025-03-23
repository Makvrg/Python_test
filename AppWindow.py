import customtkinter as ctk
import functions.image_initialization as ii

import frames.First

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("On The Platform")
        #self.iconphoto(False, ii.get_main_icon_image())
        self.geometry("1000x700+360+150")
        self.resizable(False, False)
        self.configure(fg_color="#CCFFCC")

        # Theme and mode setting
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode("light")

        # Create frames
        first_frame = frames.First.First(self, border_width=15, border_color="#006600",
                                       fg_color="#FFFFFF", corner_radius=30)