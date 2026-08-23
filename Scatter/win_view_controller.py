from PySide6.QtWidgets import QHBoxLayout
import sys

from table_view_controller import TableViewController
from chart_view import ChartView
from warning_dialog import WarningDialog

class WinViewController:
    """
    WinViewController class, to handle setting up the ui from a ui file and setup buttons events and so on.
    """
    def __init__(self, loader, win):
        """
        Initializer to setup loader, window, window size and other stuff.
        """
        self.loader = loader 
        self.win = win 

        self.win.resize(1000, 800)

        self.table_view = None 
        self.table_controller = None 
        self.chart_view = None 

        self.setup_ui()

    def setup_ui(self):
        """
        Method for setting up the ui, it should only be called once. It loads
        the ui from a ui file and puts the chartview in the right place. On top of that it sets up
        the button events.
        """
        self.table_view = self.loader.load("./Scatter/resources/views/table_view.ui")
        self.table_controller = TableViewController(self.table_view)
        table_layout = QHBoxLayout()
        self.win.table_frame.setLayout(table_layout)
        table_layout.addWidget(self.table_view)

        self.chart_view = ChartView(parent=self.win)
        chart_layout = QHBoxLayout()
        self.win.chart_container.setLayout(chart_layout)
        chart_layout.addWidget(self.chart_view)
        
        self.win.close_btn.clicked.connect(lambda: self.close())
        self.win.help_btn.clicked.connect(lambda: self.show_help())
        self.win.plot_btn.clicked.connect(lambda: self.plot_data())
        self.win.export_btn.clicked.connect(lambda: self.chart_view.export())
        self.win.chart_settings_btn.clicked.connect(lambda: self.chart_view.settings())
    
    def plot_data(self):
        """
        Method for extracting the data and plotting the extracted data 
        on a matplotlib plot (ChartView).
        """
        x, y = self.table_controller.extract_data()
        if x != [] and y != []: self.chart_view.plot(x, y)
        else: WarningDialog("Warning!", "You must enter data for it to be plotted!").exec()

    def close(self):
        """
        Method for closing the application.
        """
        sys.exit()
    
    def show_help(self):
        """
        Method for showing a help dialog.
        TODO: To be implemented
        """
        pass 