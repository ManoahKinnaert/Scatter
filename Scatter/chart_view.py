from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

from PySide6.QtWidgets import QMessageBox, QFileDialog

class ChartView(FigureCanvas):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent 

        plt.style.use("dark_background")
        self.fig = Figure(figsize=(7, 6), dpi=100)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig, *args, **kwargs)

    def plot(self, x: list, y: list):
        # first clear the plot 
        self.axes.clear()
        sizes = np.random.uniform(15, 80, len(x))
        try: self.axes.scatter(x, y, s=sizes, c="cyan", vmin=0, vmax=100)
        except: pass
        # try to calculate the linreg
        try:
            slope, intercept, r, p, std_err = stats.linregress(x, y)
            # plot the linreg
            def linear_eq(xin):
                return slope * xin + intercept
            self.axes.plot(x, list(map(linear_eq, x)), c="orange")
        except Exception as e: # show error dialog
            print("[Exception]:", e)
            dlg = QMessageBox(self.parent)
            dlg.setStyleSheet("background-color: rgb(0, 0, 0);")
            dlg.setWindowTitle("Error!")
            dlg.setText("There must be at least two unique x values\nto be able to perform linear regression!")
            dlg.setIcon(QMessageBox.Critical)
        self.draw()

    # open dialog to choose the file location and name 
    def export(self):
        filename, _ = self.choose_file_location()
        self.fig.savefig(filename, format="pdf")
    
    # opens simple dialog to select path for the file
    def choose_file_location(self):
        dialog = QFileDialog()
        #dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setWindowTitle("Save your chart.")
        filename = dialog.getSaveFileName(self.parent, "Save chart", "", "PDF Files (*.pdf)")
        return filename
