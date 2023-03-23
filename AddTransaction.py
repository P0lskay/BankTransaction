from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem, QGridLayout, QWidget


class AddTransaction(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.setLayout(layout)

