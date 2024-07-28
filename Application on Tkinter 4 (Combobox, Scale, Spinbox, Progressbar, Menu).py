
from tkinter import *
from tkinter import ttk # Подключаем пакет ttk
from tkinter.messagebox import showinfo

root = Tk()
root.title("Приложение на Tkinter 3") # Установка заголовка окна
root.geometry('300x300+750+350') # устанавливаем размеры окна и его позицию
icon = PhotoImage(file = 'Voiceless_palato-alveolar_fricative_(vector).svg.png') # Объект класса PhotoImage
root.iconphoto(False, icon) # Задаем иконку для окна, по умолчанию - перо. Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения

def finish():
    root.destroy() # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

select_alltime = []
def selected(event):
    select_alltime.append(lang_combobox.get())
    print('За всё время выбирали: ' +
          ', '.join(select_alltime))

languages = ['Python', 'C#', 'Java', 'JS']
lang_var = StringVar()

lang_label = ttk.Label(font=('Fira Sans', 10), textvariable=lang_var)
lang_label.pack(anchor=NW, padx=6, pady=6)

# Создание выпадающего списка Combobox
lang_combobox = ttk.Combobox(textvariable=lang_var, value=languages, font=('Fira Sans', 10), state='readonly')
lang_combobox.pack(anchor=NW, padx=6, pady=6)

lang_combobox.current(1) # Установка элемента по умолчанию из списка занчений
#lang_combobox.set('SQL') # Установка нового значения по умолчанию
print(lang_combobox.get(), lang_var.get())

lang_combobox.bind('<<ComboboxSelected>>', selected) # Функция на случай выбора элемента

# Создание ползунков
#double_var = DoubleVar() # Переменная с дробными числами
#ttk.Label(textvariable=double_var).pack()

def change(newVal): # Функция для ползунка должна принимать его новое значение в виде строкового представления дробного числа
    var_text.set(round(float(newVal)))
    # или так
    # label['text'] = scale.get()

def spin_change():
    var_text.set(round(float(spinbox.get())))

def start():
    progressbar.start(50) # +1 к прогрессу каждые 50 миллисекунд

def stop():
    progressbar.stop()

def extra():
    progressbar.step() # По умолчанию 1

var_text = IntVar(value=40)


sc_label = ttk.Label(text=40, textvariable=var_text)
sc_label.pack()

hor_scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=0.0, to=100.0, value=40, command=change, variable=var_text) # variable=double_var)
hor_scale.pack()

# Создание Spinbox
spinbox = ttk.Spinbox(textvariable=var_text, from_=0.0, to=100.0, state='readonly', increment=10.0, font=('Fira Sans', 10), wrap=True, command=spin_change)
spinbox.pack(anchor='n', expand=True, padx=6, pady=6)

spinbox2 = ttk.Spinbox(value=['SQL', 'Python', 'JS'], wrap=True, state='readonly')
spinbox2.pack(anchor='n', expand=True)

# Создание прогрессбара
progressbar = ttk.Progressbar(variable=var_text, orient='horizontal', length=200, mode='indeterminate')
progressbar.pack()

start_btn = ttk.Button(text='Старт', command=start)
start_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
stop_btn = ttk.Button(text='Стоп', command=stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)
extra_btn = ttk.Button(text='Ускорение', command=extra)
extra_btn.pack(anchor='c', padx=6, pady=6)

# Создание меню

def info_menu():
    showinfo('GUI Python', 'Нажата кнопка Save')

root.option_add('*tearOff', FALSE)

main_menu = Menu()
file_menu = Menu()
settings_menu = Menu()

settings_menu.add_command(label='Colour')
settings_menu.add_command(label='Size')
file_menu.add_cascade(label='Settings', menu=settings_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Save', command=info_menu)
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit')
main_menu.add_cascade(label='View')

    # Установка меню
root.config(menu=main_menu)

# Протокол удаления
root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()
