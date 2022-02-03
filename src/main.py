import sys

from PyQt6.QtWidgets import QApplication

from src.gryphonui.main_window import MainWindow


def main():
    app = QApplication([])
    MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit()
