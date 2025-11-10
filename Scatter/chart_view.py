from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

from PySide6.QtWidgets import QMessageBox, QFileDialog, QDialog
from pathlib import Path

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
        except: # show error dialog
            dlg = QMessageBox(self.parent)
            dlg.setStyleSheet("background-color: rgb(0, 0, 0);")
            dlg.setWindowTitle("Error!")
            dlg.setText("There must be at least two unique x values\nto be able to perform linear regression!")
            dlg.setIcon(QMessageBox.Critical)
        self.draw()


    def export(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setWindowTitle("Save your chart.")
        filename = ""
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames: filename = filenames[0]
        # save the chart
        # TODO: allow user to pick the name of the file
        self.fig.savefig(filename + "/mychart.pdf", format="pdf")
