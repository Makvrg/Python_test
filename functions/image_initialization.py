import customtkinter as ctk
from PIL import Image, ImageTk


# App (First display)
def get_first_display_image() -> ctk.CTkImage:
    first_d = Image.open("../image/first_display.png")
    first_display_image = ctk.CTkImage(first_d, size=(914, 333))
    return first_display_image


# Task
def get_button_save_image() -> ctk.CTkImage:
    button_save = Image.open("../image/save.png")
    button_save_image = ctk.CTkImage(button_save, size=(59, 59))
    return button_save_image


# AllResults
def get_notebook_star_image() -> ImageTk.PhotoImage:
    notebook_star = Image.open("../image/notebook_star.png")
    notebook_star.thumbnail(size=(29, 28))
    notebook_star_image = ImageTk.PhotoImage(notebook_star)
    return notebook_star_image

def get_notebook_trophy_image() -> ImageTk.PhotoImage:
    notebook_trophy = Image.open("../image/notebook_trophy.png")
    notebook_trophy.thumbnail(size=(24, 28))
    notebook_trophy_image = ImageTk.PhotoImage(notebook_trophy)
    return notebook_trophy_image
