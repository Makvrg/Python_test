#from Classes.Class_App import App
#from Classes.Class_InfoFrame import InfoFrame


def finish():
    app.destroy()  # Ручное закрытие окна и всего приложения
    print('Закрытие приложения')

if __name__ == "__main__":
    import Classes.Class_App
    app = Classes.Class_App.App()
    app.protocol('WM_DELETE_WINDOW', finish)
    app.mainloop()
