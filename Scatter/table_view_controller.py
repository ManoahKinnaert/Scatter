from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtGui import QDoubleValidator


class NumericalDelegate(QStyledItemDelegate):
    """
    Validator that allows only for double values to be entered in the table.
    """
    def createEditor(self, parent, *args):
        editor = QLineEdit(parent)
        validator = QDoubleValidator()
        editor.setValidator(validator)
        return editor 
    
    def setEditorData(self, editor, index):
        value = index.model().data(index)
        if value is None or value == "":
            editor.setText("0")

class TableViewController:
    """
    TableViewController class for controlling the data table.
    It sets up button events and handles everything from manipulating the data,
    to extracting the data.
    """
    def __init__(self, table):
        """
        Initializer method.
        """
        self.view = table 
        self.table = self.view.table
        # restrict input values to be numerical only
        self.table.setItemDelegate(NumericalDelegate(self.table))

        self.setup_ui()

    def setup_ui(self):
        """
        Setup button events.
        """
        self.view.add_row_btn.clicked.connect(lambda: self.add_row())
        self.view.delete_row_btn.clicked.connect(lambda: self.table.removeRow(self.table.rowCount() - 1))
        self.view.clear_table_btn.clicked.connect(lambda: self.table.setRowCount(0))
        self.view.clear_values_btn.clicked.connect(lambda: self.clear_values())

    def add_row(self):
        """
        Method for adding a table row.
        """
        rows = self.table.rowCount()
        self.table.insertRow(rows)
        self.set_row_values(rows, 0, 0)

    def clear_values(self):
        """
        Method for clearing all values in the table.
        """
        rows = self.table.rowCount()
        for row in range(rows): self.set_row_values(row, 0, 0)
    
    def set_row_values(self, row, x: float, y: float):
        """
        Method to set the numerical value of a given row.
        """
        self.table.setItem(row, 0, QTableWidgetItem(str(x)))
        self.table.setItem(row, 1, QTableWidgetItem(str(y)))

    def extract_data(self):
        """
        Method for extracting the table data to the required format for use in matplotlib.
        It returns a list of all x values and a list of all y values.
        """
        x, y = [], []
        for row in range(self.table.rowCount()):
            x.append(float(self.table.item(row, 0).text().replace(",", ".")))
            y.append(float(self.table.item(row, 1).text()))
        return x, y