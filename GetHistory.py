from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem, QGridLayout, QWidget, QRadioButton, \
    QButtonGroup, QVBoxLayout, QDateEdit, QLineEdit, QLabel, QHBoxLayout, QListWidget


class GetHistory(QWidget):

    def _on_search_btn_clicked(self):
        operations = self.parent().get_history_transactions(self.curr_count,
                                                            self.start_date_input.text(),
                                                            self.end_date_input.text())
        self.list_operations.clear()
        row = 0
        for i in operations:
            newItem = QListWidgetItem()
            newItem.setText(i)
            self.list_operations.insertItem(row, newItem)
            row += 1


    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        layout = QGridLayout()

        curr_count_with_point = self.parent().list_counts.currentItem().text().split()[1]
        self.curr_count = curr_count_with_point[:len(curr_count_with_point) - 1]
        self.start_date_input_label = QLabel("Дата начала: ")
        self.start_date_input = QDateEdit()
        self.end_date_input_label = QLabel("Дата окончания: ")
        self.end_date_input = QDateEdit()
        date_layout = QHBoxLayout()
        date_layout.addWidget(self.start_date_input_label)
        date_layout.addWidget(self.start_date_input)
        date_layout.addWidget(self.end_date_input_label)
        date_layout.addWidget(self.end_date_input)

        self.search_btn = QPushButton("Поиск")
        self.search_btn.clicked.connect(self._on_search_btn_clicked)

        self.list_operations = QListWidget(self)

        layout.addLayout(date_layout, 0, 0)
        layout.addWidget(self.search_btn, 0, 1)
        layout.addWidget(self.list_operations, 1, 0, 3, 3)


        self.setLayout(layout)
