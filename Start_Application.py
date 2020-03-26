from src.CreateMainWindow import CreateMainWindow
from src.CreateResultWindow import CreateResultWindow


if __name__ == '__main__':
    window = CreateMainWindow()
    window.start_app()

    window1 = CreateResultWindow()
    window1.start_app()

