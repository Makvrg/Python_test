from global_variables import for_data_base
from functions.path_handlers import get_path
from functions.handlers import finish
import AppWindow


if __name__ == "__main__":
    app = AppWindow.AppWindow()
    for_data_base.database_abs_path = get_path() / 'math_simulator_database.db'

    app.protocol('WM_DELETE_WINDOW', lambda: finish(app))
    app.mainloop()
