import customtkinter as ctk
from PIL import Image


# All frame
def get_empty_plug_image():
    empty_plug = Image.open("Image/Empty_plug.png")
    empty_plug_image = ctk.CTkImage(empty_plug, size=(1, 1))
    return empty_plug_image

# App (First display)
def get_first_display_image():
    first_d = Image.open("Image/First_display.png")
    first_display_image = ctk.CTkImage(first_d, size=(914, 333))
    return first_display_image

def get_button_1_image():
    button_1 = Image.open("Image/Button_1.png")
    button_1_image = ctk.CTkImage(button_1, size=(340, 85))
    return button_1_image

# InfoFrame
def get_label_flag_1_image():
    label_flag_1 = Image.open("Image/InfoFrame_Label_flag_1.png")
    label_flag_1_image = ctk.CTkImage(label_flag_1, size=(340, 43))
    return label_flag_1_image

def get_label_flag_2_image():
    label_flag_2 = Image.open("Image/InfoFrame_Label_flag_2.png")
    label_flag_2_image = ctk.CTkImage(label_flag_2, size=(360, 45))
    return label_flag_2_image

def get_label_name_image():
    label_name = Image.open("Image/InfoFrame_Label_name.png")
    label_name_image = ctk.CTkImage(label_name, size=(284, 28))
    return label_name_image

def get_label_type_image():
    label_type = Image.open("Image/InfoFrame_Label_type.png")
    label_type_image = ctk.CTkImage(label_type, size=(290, 31))
    return label_type_image

def get_label_count_image():
    label_count = Image.open("Image/InfoFrame_Label_count.png")
    label_count_image = ctk.CTkImage(label_count, size=(424, 29))
    return label_count_image

def get_label_button_image():
    label_button = Image.open("Image/InfoFrame_Label_button.png")
    label_button_image = ctk.CTkImage(label_button, size=(500, 51))
    return label_button_image

def get_label_error_name_image():
    label_error_name = Image.open("Image/InfoFrame_Label_error_name.png")
    label_error_name_image = ctk.CTkImage(label_error_name, size=(300, 48))
    return label_error_name_image

def get_label_error_type_1_image():
    label_error_type_1 = Image.open("Image/InfoFrame_Label_error_type_1.png")
    label_error_type_1_image = ctk.CTkImage(label_error_type_1, size=(310, 49))
    return label_error_type_1_image

def get_label_error_type_2_image():
    label_error_type_2 = Image.open("Image/InfoFrame_Label_error_type_2.png")
    label_error_type_2_image = ctk.CTkImage(label_error_type_2, size=(310, 46))
    return label_error_type_2_image

# TaskFrame
def get_label_exercise_1_image():
    label_exercise_1 = Image.open("Image/TaskFrame_label_exercise_1.png")
    label_exercise_1_image = ctk.CTkImage(label_exercise_1, size=(700, 39))
    return label_exercise_1_image

def get_label_explanation_image():
    label_explanation = Image.open("Image/TaskFrame_label_explanation.png")
    label_explanation_image = ctk.CTkImage(label_explanation, size=(550, 35))
    return label_explanation_image

def get_button_save_image():
    button_save = Image.open("Image/save.png")
    button_save_image = ctk.CTkImage(button_save, size=(59, 59))
    return button_save_image

def get_taskframe_button_previous_image():
    button_previous = Image.open("Image/TaskFrame_button_previous.png")
    taskframe_button_previous_image = ctk.CTkImage(button_previous, size=(161, 43))
    return taskframe_button_previous_image

def get_taskframe_button_compete_image():
    button_complete = Image.open("Image/TaskFrame_button_complete.png")
    taskframe_button_complete_image = ctk.CTkImage(button_complete, size=(248, 43))
    return taskframe_button_complete_image

def get_taskframe_button_next_image():
    button_next = Image.open("Image/TaskFrame_button_next.png")
    taskframe_button_next_image = ctk.CTkImage(button_next, size=(153, 43))
    return taskframe_button_next_image

def get_taskframe_button_previous_disabled_image():
    button_previous_disabled = Image.open("Image/TaskFrame_button_previous_disabled.png")
    taskframe_button_previous_disabled_image = ctk.CTkImage(button_previous_disabled, size=(161, 43))
    return taskframe_button_previous_disabled_image
