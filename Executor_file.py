from Classes.Class_App import App



def finish():
    app.destroy()  # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

if __name__ == "__main__":
    app = App()
    app.protocol('WM_DELETE_WINDOW', finish)
    app.mainloop()
