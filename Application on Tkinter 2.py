from tkinter import *
from tkinter import ttk # Подключаем пакет ttk
from tkinter.messagebox import showinfo

root = Tk()
root.title("Приложение на Tkinter 2") # Установка заголовка окна
root.geometry('250x200+800+300') # устанавливаем размеры окна и его позицию
icon = PhotoImage(file = 'Voiceless_palato-alveolar_fricative_(vector).svg.png') # Объект класса PhotoImage
root.iconphoto(False, icon) # Задаем иконку для окна, по умолчанию - перо. Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения

def finish():
    root.destroy() # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

#enabled = IntVar()
#def changet():
#    if enabled.get() == 1:
#        showinfo(title="Info", message="Включено")
#    else:
#        showinfo(title="Info", message="Отключено")

#enabled_checkbutton = ttk.Checkbutton(text='Даю согласие', variable=enabled, command=changet) # Создание флажка (квадратик с галочкой)
#enabled_on = 'Включено'
#enabled_off = 'Выключено'
#enabled = StringVar(value=enabled_off) # Установка значения по умолчанию
#enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
#enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

#enabled_label = ttk.Label(textvariable=enabled)
#enabled_label.pack(padx=6, pady=6, anchor=NW)

#def select():
#    result = "Выбрано: "
#    if python.get() == 1: result = f"{result} Python"
#    if javascript.get() == 1: result = f"{result} JavaScript"
#    if java.get() == 1: result = f"{result} Java"
#    languages.set(result)
 
#position = {"padx":6, "pady":6, "anchor":NW}
 
#languages = StringVar()
#languages_label = ttk.Label(textvariable=languages)
#languages_label.pack(**position)
 
#python = IntVar()
#python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
#python_checkbutton.pack(**position)
 
#javascript = IntVar()
#javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
#javascript_checkbutton.pack(**position)
 
#java = IntVar()
#java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
#java_checkbutton.pack(**position)

position = {"padx":6, "pady":6, "anchor":NW}
param = [{'name': '6'}, {'name': 'Да'}, {'name': 'Не знаю'}, {'name': 'Тщту'}, {'name': 'Нет'},]
lang = StringVar()
def select():
    if lang.get() == 'Да':
        total['text'] = 'Верно! Молодец!'
    else:
        total['text'] = 'Неверно попробуй ещё раз'

frame = ttk.Frame(borderwidth=2, relief=SOLID, padding=[8, 8], width=100)
total = ttk.Label(master=frame, text='У слона 4 ноги?', font=('Fira Sans', 16))
total.pack(padx=6, pady=6)
for i in param:
    btn = ttk.Radiobutton(master=frame, text=i['name'], variable=lang, value=i['name'], command=select)
    btn.pack(**position)
frame.pack(padx=5, pady=5)
ttk.Label(text='Надпись вне фрейма', font=('Fira Sans', 16)).pack()

 
root.protocol('WM_DELETE_WINDOW', finish) # Первый параметр - имя события, а второй параметр - функция, которая вызывается при возникновении события






























root.mainloop()


