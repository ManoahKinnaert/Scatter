from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

class MessageDialog(QDialog):
   def __init__(self, title: str, message: str):
        super().__init__()

        self.setWindowTitle(title)
        QBtn = (
            QDialogButtonBox.Ok
        )
        self.btn_box = QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message_widget = QLabel(message)
        layout.addWidget(message_widget)
        layout.addWidget(self.btn_box)
        self.setLayout(layout) 

class WarningDialog(MessageDialog):
    def __init__(self, message: str):
        super().__init__("Warning!", message)

class HelpDialog(QDialog):
    def __init__(self, message: str):
        super().__init__("Info", message)
