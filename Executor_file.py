from Handlers import finish
import Classes.Class_App


if __name__ == "__main__":
    app = Classes.Class_App.App()
    app.protocol('WM_DELETE_WINDOW', lambda: finish(app))
    app.mainloop()
