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

def get_admin_image() -> ctk.CTkImage:
    try:
        admin_im = Image.open("images/admin.png")
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'admin.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        admin_im = Image.open(BytesIO(img_data))

    first_display_image = ctk.CTkImage(admin_im, size=(82, 82))

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


# AllResults and AdminAllResults
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

def get_wrong_error_image() -> ImageTk.PhotoImage:
    try:
        notebook_wrong_error = Image.open("images/wrong_error.png")
        notebook_wrong_error.thumbnail(size=(24, 28))
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'wrong_error.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        notebook_wrong_error = Image.open(BytesIO(img_data))
        notebook_wrong_error.thumbnail(size=(26, 28))

    notebook_wrong_error_image = ImageTk.PhotoImage(notebook_wrong_error)

    return notebook_wrong_error_image

# Editor
def get_change_image() -> ctk.CTkImage:
    try:
        chg = Image.open("images/change.png")
    except FileNotFoundError:
        # Opening the resource as binary data
        with importlib.resources.open_binary('images', 'change.png') as resource_file:
            img_data = resource_file.read()

        # Loading an image from bytes
        chg = Image.open(BytesIO(img_data))

    change_image = ctk.CTkImage(chg, size=(55, 55))

    return change_image
