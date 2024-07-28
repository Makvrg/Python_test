
from tkinter import *
from tkinter import ttk # Подключаем пакет ttk

def finish():
    root.destroy() # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

root = Tk() # Создание корневого объекта - окно
root.title("Приложение на Tkinter") # Установка заголовка окна
root.geometry('250x200+800+300') # устанавливаем размеры окна и его позицию
#root.iconbitmap(default='Иконка функции.ico') # Задаем иконку для окна, по умолчанию - перо
# Или же вариант НЕ с расширением .ico
icon = PhotoImage(file = 'Voiceless_palato-alveolar_fricative_(vector).svg.png') # Объект класса PhotoImage
root.iconphoto(False, icon) # Задаем иконку для окна, по умолчанию - перо. Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения


#root.update_idletasks() # Приложение применяет размеры к окну раньше, чем mainloop()
#print(root.geometry()) # Получение данных о размере и позиции окна

#root.resizable(False, False) # Делает окно фиксированным по размеру: первый параметр - можно ли пользователю растягивать окно по ширине, а второй - по высоте
#root.minsize(200, 150) # минимальные размеры окна: ширина - 200, высота - 150
#root.maxsize(400, 300) # максимальные размеры окна: ширина - 400, высота - 300

#label = Label(text='Hello METANIT.COM') # создаем текстовую метку (надпись)
#label.pack() # размещаем метку

btn = ttk.Button(text='Click') # Создаем кнопку из пакета ttk
btn.pack()
btn['text'] = 'Send' # Обращаться к параметрам можно и вне конструктора, используя имя переменной виджета и синтаксис словарей
btnText = btn['text']
#print(btnText) # Получаем значение параметра text
# Для изменения параметров виджета также можно использовать метод config(), в который передаются параметры и их значения
btn.config(text='Send Email')

#print(btn.winfo_class()) # Возвращает класс виджета

def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x() # Координаты относительно родительского элемента
    widget_y = widget.winfo_y()
    print('   ' * depth + f'{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}')
    for child in widget.winfo_children():
        print_info(child, depth + 1)

root.update() # Обновление информации о виджетах до mainloop()

#print_info(root) # Вывод информации о виджетах окна

clicks = 0

def click_func(wiget): # event для .bind() учитываем для лямбда-функции
    global clicks
    clicks += 1
    wiget['text'] = f'Количество кликов - {clicks}'
    print(clicks)
def doubleclick_func(wiget): # event для .bind() учитываем в лямбда-функции
    global clicks
    clicks += 10
    wiget['text'] = f'Количество кликов - {clicks}'
    print(clicks)
    
btn.destroy()
btn1 = ttk.Button(text='Кликни', command=lambda: click_func(btn1)) # Кнопка - кликер
#btn1.pack(anchor='nw', expand=True, fill=X, padx=[30,70], pady=[15, 60], ipadx = 15, ipady=10) # Помещение кнопки в северо-западный угол (верхний левый угол) и отступ от него, а также отступы содержимого виджета от своих границ
#btn1.pack(fill=BOTH, expand=True)
btn1.place(relx=0.5, rely=0.9, anchor='c', bordermode=OUTSIDE)
#btn1.destroy()

for j in range(2):
    root.columnconfigure(weight=1, index=j) # Настройка столбцов по всей ширине контейнера
for i in range(2):
    root.rowconfigure(weight=1, index=i) # Настройка строк по всей длине контейнера

#for i in range(3): # Создание таблицы (грида)
#    for j in range(3):
#        btn = ttk.Button(text=f'({i},{j})')
#        btn.grid(row=i, column=j, ipadx=6, ipady=6, padx=4, pady=4)

#btn1 = ttk.Button(text="button 1")
#btn1.grid(row=0, column=0, ipadx=10, ipady=5, padx=7, pady=7, sticky='nw')

#btn2 = ttk.Button(text="button 2")
#btn2.grid(row=0, column=1, ipadx=10, ipady=5, padx=7, pady=7, sticky='nsew')

#btn3 = ttk.Button(text="button 3")
#btn3.grid(row=1, column=0, columnspan=2, ipadx=70, ipady=10, padx=7, pady=7, sticky='ew')

btn1.bind('<KeyPress-Right>', lambda event: click_func(btn1)) # Обработка событий
btn1.bind('<Double-KeyPress-Left>', lambda event: doubleclick_func(btn1))
root.bind_class('TButton', "<Double-ButtonPress-3>", lambda event: doubleclick_func(btn1)) # Привязка ко всему классу кнопок из пакета ttk в данном контейнере (root)

btn1.unbind('<Double-KeyPress-Left>') # Открепление обычного .bind() от виджета

picture = PhotoImage(file='Скала мем.png')
label = ttk.Label(text='Текстовая метка', font=('Fira Sans', 16), image=picture, compound='top', background="#FFCDD2", foreground="#BAB652", padding=6, relief='solid')
#label.place(relx=0.5, rely=0.1, anchor='c', relheight=0.6, relwidth=0.9)

def mas():
    print(entry1.get().split())
#entry = ttk.Entry(font=('Fira Sans', 16), width=10) # Создание поля для ввода
#entry.pack(anchor=N, padx=6, pady=6, expand=True)
btn1.bind("<ButtonPress-1>", lambda event: mas())

def print_b():
    label1['text'] = entry.get()
def delete_b():
    entry.delete(0, END)
    label1['text'] = ''

#entry.insert(4, 'Привет!')
#label1 = ttk.Label(font=('Fira Sans', 16), background="#FFCDD2", foreground="#BAB652", padding=6, relief='solid')
#label1.pack(anchor=N, padx=6, pady=4, expand=True)
#print_button = ttk.Button(text='Вывод', command=print_b)
#print_button.place(relx=0.2, rely=0.3, anchor='c', relheight=0.15, relwidth=0.3)
#clear_button = ttk.Button(text='Очистить', command=delete_b)
#clear_button.place(relx=0.8, rely=0.3, anchor='c', relheight=0.15, relwidth=0.3)

name = StringVar()
result_name = StringVar()
entry1 = ttk.Entry(font=('Fira Sans', 16), width=10, textvariable=name) # Связываем StringVar и Entry
entry1.pack(anchor=N, expand=1)
label2 = ttk.Label(textvariable=result_name, font=('Fira Sans', 16), justify=CENTER)
label2.pack(anchor=N, expand=1)
def check(*args):
    print(name.get())
    if name.get() == 'admin':
        result_name.set('Запрещённое имя')
    else:
        result_name.set('Имя разрешено')
name.trace_add('write', check) # Проверка на изменение значения у StringVar, также есть чтение и удаление

root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()

