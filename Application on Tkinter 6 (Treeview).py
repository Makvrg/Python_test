
from tkinter import *
from tkinter import ttk # Подключаем пакет ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText # Виджет Text с готовой вертикальной прокруткой

root = Tk()
root.title("Приложение на Tkinter 3") # Установка заголовка окна
root.geometry('400x187+750+350') # устанавливаем размеры окна и его позицию
icon = PhotoImage(file = 'Voiceless_palato-alveolar_fricative_(vector).svg.png') # Объект класса PhotoImage
root.iconphoto(False, icon) # Задаем иконку для окна, по умолчанию - перо. Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения

# Функции
def finish():
    root.destroy() # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')
    
def new_extend(beginning, literables):
        beginning.extend(literables)
        return beginning
        
def table_sort(reverse, *,  all_territory=False, col=''): # Сортировка таблицы по столбцам или всю сразу
    if all_territory == True:
        content = [new_extend([iid], table.item(iid)['values']) for iid in table.get_children('')]
    else:
        content = [new_extend([iid], [table.set(iid, col)]) for iid in table.get_children('')]
    content.sort(reverse=reverse, key=lambda x: x[1:])
    for k, (iid, *args) in enumerate(content):
        table.move(item=iid, parent='', index=k)
    if col != '':
        table.heading(col, command=lambda: table_sort(not reverse, col=col))
    else:
        sort_button['command'] = lambda: table_sort(not reverse, all_territory=True)

def treeview_select(event): # Обработка выбора строчек в таблице
    select_people = []
    for iid in table.selection():
        person = map(str, table.item(iid)['values']) # .item() возвращает словарь
        select_people.append(", ".join(person))
    print(f'Вы выбрали: {" | ".join(select_people)}')

# Создание Treeview
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)

    # Определяем данные таблицы
people = [
    ('Mike', 34, 'fan@gmail.com'), ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ]
    # Определяем столбцы
columns = ("name", "age", "email")

table = ttk.Treeview(columns=columns, show='headings', selectmode='extended')
#table.pack(fill=BOTH, padx=4, pady=4, expand=1)
table.grid(row=0, column=0, sticky='nsew')
table.bind('<<TreeviewSelect>>', treeview_select)

    # Добавляем прокрутку
scroll = ttk.Scrollbar(orient='vertical', command=table.yview)
table.configure(yscroll=scroll.set)
scroll.grid(row=0, column=1, sticky='ns')

    # Определяем и настраиваем заголовки
python_logo = PhotoImage(file='Python photo.png')
table.heading('name', text='Имя', image=python_logo, anchor=W, command=lambda: table_sort(False, col=0)) # Можно просто по номеру столбца
table.heading('age', text='Возраст', anchor=W, command=lambda: table_sort(False, col=1))
table.heading('email', text='Email', anchor=W, command=lambda: table_sort(False, col=2))

 # Настройка столбцов
table.column(column='#1', width=50, minwidth=40)
table.column(column='#2', width=40, minwidth=30)
table.column(column='#3', width=100, minwidth=60)

    # Добавляем данные
for person in people:
    table.insert(parent='', index='end', values=person) # метод возвращает свой индентификатор iid и добаляет строку данных

    # Кнопка полной сортировки
sort_button = ttk.Button(text='Сортировка повсем столбцам', command=lambda: table_sort(False, all_territory=True))
sort_button.grid(row=1, column=0, sticky=W)

#print([new_extend([iid], table.item(iid)['values']) for iid in table.get_children('')])
#print([new_extend([iid], [table.set(iid, 0)]) for iid in table.get_children('')])


# Протокол удаления
root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()
