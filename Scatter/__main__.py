#!./venv/bin/python
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import sys 

from win_view_controller import WinViewController

if __name__ == "__main__":
    """
    Main entry, setup app, loader and exec.
    """
    app = QApplication(sys.argv)
    loader = QUiLoader()

    window = loader.load("./Scatter/resources/views/display.ui")
    WinViewController(loader, window)
    window.show()

    app.exec()