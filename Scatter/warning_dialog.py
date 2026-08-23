from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

class WarningDialog(QDialog):
    def __init__(self, title: str, message: str):
        super().__init__()

        self._title = title
        self._message = message

        self.setWindowTitle(self._title)
        QBtn = (
            QDialogButtonBox.Ok
        )
        self.btn_box = QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel(self._message)
        layout.addWidget(message)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)