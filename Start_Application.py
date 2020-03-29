from src.CreateMainWindow import CreateMainWindow
from src.CreateResultWindow import CreateResultWindow
from src.ConnectToSQLdb import ConnectToSQLdb
from src.ConnectToDB import ConnectToDB


if __name__ == '__main__':
    window = CreateMainWindow()
    window.start_app()

    # window1 = CreateResultWindow()
    # window1.start_app()

