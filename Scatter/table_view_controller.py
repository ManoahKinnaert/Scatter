from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtGui import QDoubleValidator



class NumericalDelegate(QStyledItemDelegate):
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
    def __init__(self, table):
        self.view = table 
        self.table = self.view.table
        # restrict input values to be numerical only
        self.table.setItemDelegate(NumericalDelegate(self.table))

        self.setup_ui()

    def setup_ui(self):
        self.view.add_row_btn.clicked.connect(lambda: self.add_row())
        self.view.delete_row_btn.clicked.connect(lambda: self.table.removeRow(self.table.rowCount() - 1))
        self.view.clear_table_btn.clicked.connect(lambda: self.table.setRowCount(0))
        self.view.clear_values_btn.clicked.connect(lambda: self.clear_values())

    def add_row(self):
        rows = self.table.rowCount()
        self.table.insertRow(rows)
        self.set_row_values(rows, 0, 0)

    def clear_values(self):
        rows = self.table.rowCount()
        for row in range(rows): self.set_row_values(row, 0, 0)
    
    def set_row_values(self, row, x: float, y: float):
        self.table.setItem(row, 0, QTableWidgetItem(str(x)))
        self.table.setItem(row, 1, QTableWidgetItem(str(y)))

    # returns a list of all x values and a list of all y values
    def extract_data(self):
        x, y = [], []
        for row in range(self.table.rowCount()):
            x.append(float(self.table.item(row, 0).text().replace(",", ".")))
            y.append(float(self.table.item(row, 1).text()))
        return x, y