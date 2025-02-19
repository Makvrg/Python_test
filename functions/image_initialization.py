import customtkinter as ctk
from PIL import Image, ImageTk
import importlib.resources
from io import BytesIO


# App (First display)
def get_first_display_image() -> ctk.CTkImage:
    try:
        first_d = Image.open("images/first_display.png")
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'first_display.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        first_d = Image.open(BytesIO(img_data))

    first_display_image = ctk.CTkImage(first_d, size=(914, 333))

    return first_display_image


# Task
def get_button_save_image() -> ctk.CTkImage:
    try:
        button_save = Image.open("images/save.png")
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'save.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        button_save = Image.open(BytesIO(img_data))

    button_save_image = ctk.CTkImage(button_save, size=(59, 59))

    return button_save_image


# AllResults
def get_notebook_star_image() -> ImageTk.PhotoImage:
    try:
        notebook_star = Image.open("images/notebook_star.png")
        notebook_star.thumbnail(size=(29, 28))
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'notebook_star.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        notebook_star = Image.open(BytesIO(img_data))
        notebook_star.thumbnail(size=(29, 28))

    notebook_star_image = ImageTk.PhotoImage(notebook_star)

    return notebook_star_image

def get_notebook_trophy_image() -> ImageTk.PhotoImage:
    try:
        notebook_trophy = Image.open("images/notebook_trophy.png")
        notebook_trophy.thumbnail(size=(24, 28))
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'notebook_trophy.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        notebook_trophy = Image.open(BytesIO(img_data))
        notebook_trophy.thumbnail(size=(24, 28))

    notebook_trophy_image = ImageTk.PhotoImage(notebook_trophy)

    return notebook_trophy_image
