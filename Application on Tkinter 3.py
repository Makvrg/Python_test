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

# Настройка ячеек
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=4)
root.rowconfigure(index=2, weight=1)

# Функции добавления и удаления
def add():
    lang_listbox.insert(END, lang_entry.get())
    lang_entry.delete(0, END)

def obj_delete():
    c = lang_listbox.curselection()
    if len(c) != 0:
        lang_listbox.delete(c[-1])
    else:
        a = lang_entry.get()
        a1 = lang_listbox.get(0, END)
        d = {}
        for i in range(len(a1)):
            d[a1[i]] = i
        if a in d:
            lang_listbox.delete(d[a])

def selected(event):
    sel = lang_listbox.curselection()
    if len(sel) == 0:
        lang_text.set('Ничего не выбрано')
    else:
        lang_text.set(f'Вы выбрали: {", ".join([lang_listbox.get(i) for i in sel])}')

# Текстовое поле
lang_entry = ttk.Entry(font=('Fira Sans', 12))
lang_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)

# Кнопка добавления
ttk.Button(text='Добавить', command=add).grid(column=1, row=0, padx=6, pady=6)

# Список
lang_listbox = Listbox(font=('Fira Sans', 12), selectmode=MULTIPLE)
lang_listbox.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky=NSEW)
lang_listbox.bind('<<ListboxSelect>>', selected) # При изменении списка выбраных элементов выполняется функция selected

# Кнопка удаления
ttk.Button(text='Удалить', command=obj_delete).grid(column=1, row=2, padx=6, pady=6)

# Надпись о списке выбранных элементов и переменная StringVar
lang_text = StringVar(value='Пока вы ничего не выбрали')
lang_label = ttk.Label(font=('Fira Sans', 10), textvariable=lang_text)
lang_label.grid(column=0, row=2, padx=6, pady=6)

# Добавление начальных значений
lang_listbox.insert(0, 'sqlite3')

# Добавление прокрутки
lang_scrollbar = ttk.Scrollbar(master=lang_listbox, orient='vertical', command=lang_listbox.yview)
lang_scrollbar.pack(side=RIGHT, fill=Y)

lang_listbox['yscrollcommand']=lang_scrollbar.set


# Протокол удаления
root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()
