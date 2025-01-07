from Handlers import finish


if __name__ == "__main__":
    import Classes.Class_App
    app = Classes.Class_App.App()
    app.protocol('WM_DELETE_WINDOW', lambda: finish(app))
    app.mainloop()
