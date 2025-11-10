from PySide6.QtWidgets import QHBoxLayout
import sys

from table_view_controller import TableViewController
from chart_view import ChartView

class WinViewController:
    def __init__(self, loader, win):
        self.loader = loader 
        self.win = win 

        self.win.resize(1000, 800)

        self.table_view = None 
        self.table_controller = None 
        self.chart_view = None 

        self.setup_ui()

    def setup_ui(self):
        self.table_view = self.loader.load("./resources/views/table_view.ui")
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

    
    def plot_data(self):
        x, y = self.table_controller.extract_data()
        self.chart_view.plot(x, y) 

    def close(self):
        sys.exit()
    
    def show_help(self):
        pass 