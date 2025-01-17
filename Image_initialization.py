import customtkinter as ctk
from PIL import Image, ImageTk


# App (First display)
def get_first_display_image():
    first_d = Image.open("Image/First_display.png")
    first_display_image = ctk.CTkImage(first_d, size=(914, 333))
    return first_display_image


# TaskFrame
def get_button_save_image():
    button_save = Image.open("Image/save.png")
    button_save_image = ctk.CTkImage(button_save, size=(59, 59))
    return button_save_image


# AllResultsFrame
def get_notebook_star_image():
    notebook_star = Image.open("Image/notebook_star.png")
    notebook_star.thumbnail(size=(29, 28))
    notebook_star_image = ImageTk.PhotoImage(notebook_star)
    return notebook_star_image

def get_notebook_trophy_image():
    notebook_trophy = Image.open("Image/notebook_trophy.png")
    notebook_trophy.thumbnail(size=(24, 28))
    notebook_trophy_image = ImageTk.PhotoImage(notebook_trophy)
    return notebook_trophy_image
