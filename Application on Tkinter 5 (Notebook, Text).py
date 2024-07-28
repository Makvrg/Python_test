
from tkinter import *
from tkinter import ttk # Подключаем пакет ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText # Виджет Text с готовой вертикальной прокруткой

root = Tk()
root.title("Приложение на Tkinter 3") # Установка заголовка окна
root.geometry('300x300+750+350') # устанавливаем размеры окна и его позицию
icon = PhotoImage(file = 'Voiceless_palato-alveolar_fricative_(vector).svg.png') # Объект класса PhotoImage
root.iconphoto(False, icon) # Задаем иконку для окна, по умолчанию - перо. Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения

def finish():
    root.destroy() # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

# Создание набора вкладок
note = ttk.Notebook()
note.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Создание фреймов
frame1 = ttk.Frame(master=note, borderwidth=1, relief=SOLID)
frame2 = ttk.Frame(master=note, borderwidth=1, relief=SOLID)
frame3 = ttk.Frame(master=note, borderwidth=1, relief=SOLID)

frame1.pack(fill=BOTH, expand=True, padx=5, pady=5)
frame2.pack(fill=BOTH, expand=True, padx=5, pady=5)
frame3.pack(fill=BOTH, expand=True, padx=5, pady=5)
en = ttk.Entry(master=frame1)
en.pack(padx=5, pady=5)

# Добавляем фреймы в качестве вкладок
python_logo = PhotoImage(file='Python photo.png')#, height=1000, width=1000)
note.add(child=frame1, text='Поле и текст', image=python_logo, compound=LEFT)
note.add(child=frame2, text='Текст')
note.add(child=frame3, text='Назад/вперёд')

# Создание многострочного поля для ввода Text и ползунков к нему
frame2.columnconfigure(index=0, weight=1)
frame2.rowconfigure(index=0, weight=1)

editor = Text(master=frame2, font=('Fira Sans', 16, 'bold'), wrap='none', height=5)
editor.grid(column=0, row=0, sticky=NSEW) #pack(fill=BOTH, expand=1, padx=2, pady=2)

ys = ttk.Scrollbar(master=frame2, orient='vertical', command=editor.yview)
ys.grid(column=1, row=0, sticky=NS) #pack(side=RIGHT, fill=Y)
xs = ttk.Scrollbar(master=frame2, orient='horizontal', command=editor.xview)
xs.grid(column=0, row=1, sticky=EW) #pack(side=BOTTOM, fill=X)

editor['yscrollcommand'] = ys.set
editor['xscrollcommand'] = xs.set

# Добавление текста в виджет Text
editor.insert('1.0', 'Привет, мир!\n') # Вставка в самое начало: первый пар. - номера строки и символа
editor.insert('2.0', 'Hallo, world!') # Номера строк идут с 1, а символов - с 0
editor.insert(END, '\nTkinter')
editor.delete('1.2', '1.6') # Удаление символов
editor.replace('1.0', '1.2', 'Hahahaha') # Замена символов
def get_text():
    get_label['text'] = editor.get('1.0', END)
    
get_button = ttk.Button(master=frame2, text='Получить текст', command=get_text)
get_button.grid(column=0, row=2)
get_label = ttk.Label(master=frame2)
get_label.grid(column=1, row=2)

# Создание кнопок для отката/повторения операций с текстом, работа с выделением
frame3.rowconfigure(index=0, weight=1)
#frame3.rowconfigure(index=1, weight=1)
frame3.columnconfigure(index=0, weight=1)
frame3.columnconfigure(index=1, weight=1)
frame3.columnconfigure(index=2, weight=1)
frame3.columnconfigure(index=3, weight=1)

new_editor = Text(master=frame3, font=('Fira Sans', 18), wrap='word', undo=True) # undo нужен для разрешения отката/повтора операций
new_editor.grid(row=0, column=0, columnspan=4, padx=7, pady=7)

btn_undo = ttk.Button(master=frame3, text='Отменить', command=lambda: new_editor.edit_undo()) # Метод отката операции
btn_undo.grid(row=1, column=0, padx=7, pady=7)

btn_undo = ttk.Button(master=frame3, text='Повторить', command=lambda: new_editor.edit_redo()) # Метод повторения операции
btn_undo.grid(row=1, column=3, padx=7, pady=7)

btn_sel_get = ttk.Button(master=frame3, text='Получить', command=lambda: print(new_editor.selection_get())) # Метод для получения выделенного текста
btn_sel_get.grid(row=1, column=1, padx=7, pady=7)

btn_sel_get = ttk.Button(master=frame3, text='Снять', command=lambda: new_editor.selection_clear()) # Метод для снятия выделения
btn_sel_get.grid(row=1, column=2, padx=7, pady=7)

# Готовый виджет Text с вертикальной прокруткой из дополнительного пакета
st = ScrolledText(master=frame1, width=50, height=10, wrap='word')
st.pack(fill=BOTH, expand=True)

# Обработка событий у виджета Text
text_var = StringVar()
en['textvariable'] = text_var

def text_modified(event):
    text_var.set(value=st.get('1.0', END))

st.bind('<KeyRelease>', text_modified)

# Теги, стилизация
editor.tag_add('tag1', '1.0', '1.5') # Создание тега tag1
editor.tag_configure('tag1', background='#ffbaba', foreground='#c40ca6', font=('Arial', 17), relief='raised') # Конфигурация тега
editor.insert('end', '\nChecking tags works', 'tag1') # Применение уже созданного тега
#editor.tag_remove('tag1', '1.0', END) # Удаление определённого тега с определённой области
#editor.tag_delete('tag1') # Удаление определённого тега со всега виджета

    # Вставка фотографий
rock_img = PhotoImage(file='Скала мем.png')
editor.image_create('1.0', image=rock_img) # Вставка фотографии на определённое место
editor.image_create('3.3', image=rock_img) # Вставка фотографии на определённое место
    # Вставка других виджетов
btn = ttk.Button(text='He-he-hee', image=python_logo, compound='left')
editor.window_create(END, window=btn)

# Протокол удаления
root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()
