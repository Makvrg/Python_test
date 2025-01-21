import global_variable as gv
from functions.path_handlers import get_path
from functions.handlers import finish
import frames.App


if __name__ == "__main__":
    app = frames.App.App()
    gv.database_abs_path = get_path() / 'math_simulator_database.db'
    app.protocol('WM_DELETE_WINDOW', lambda: finish(app))
    app.mainloop()
