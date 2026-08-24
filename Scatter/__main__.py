#!./venv/bin/python
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import sys 
from pathlib import Path


from . import WinViewController

if __name__ == "__main__":
    """
    Main entry, setup app, loader and exec.
    """
    app = QApplication(sys.argv)
    loader = QUiLoader()

    ui_path = Path(__file__).parent / "resources" / "views" / "display.ui"
    window = loader.load(str(ui_path))
    WinViewController(loader, window)
    window.show()

    app.exec()