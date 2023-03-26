from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem, QGridLayout, QWidget, QRadioButton, \
    QButtonGroup, QVBoxLayout, QDateEdit, QLineEdit, QLabel, QHBoxLayout, QListWidget


class GetTransactions(QWidget):
    def _on_radio_button_clicked(self):
        if self.rb_search_date.isChecked():
            self.date_input_label.setVisible(True)
            self.date_input.setVisible(True)
            self.word_label.setVisible(False)
            self.word.setVisible(False)
        elif self.rb_search_word.isChecked():
            self.date_input_label.setVisible(False)
            self.date_input.setVisible(False)
            self.word_label.setVisible(True)
            self.word.setVisible(True)

    def _on_search_btn_clicked(self):
        operations = []
        if self.rb_search_date.isChecked():
            operations = self.parent().get_transactions_per_date(self.date_input.text())
        elif self.rb_search_word.isChecked():
            operations = self.parent().get_transactions_with_word(self.word.text())
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
        self.rb_search_date = QRadioButton('Поиск по дате')
        self.rb_search_date.setChecked(True)
        self.rb_search_word = QRadioButton('Поиск по слову')


        self.button_group = QButtonGroup()
        self.button_group.addButton(self.rb_search_date)
        self.button_group.addButton(self.rb_search_word)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        button_group_layout = QVBoxLayout()
        button_group_layout.addWidget(self.rb_search_date)
        button_group_layout.addWidget(self.rb_search_word)

        self.save_btn = QPushButton("Поиск")
        self.save_btn.clicked.connect(self._on_search_btn_clicked)

        self.date_input_label = QLabel("Дата: ")
        self.date_input = QDateEdit()
        date_layout = QHBoxLayout()
        date_layout.addWidget(self.date_input_label)
        date_layout.addWidget(self.date_input)

        self.word_label = QLabel("Слово: ")
        self.word_label.setVisible(False)
        self.word = QLineEdit()
        self.word.setVisible(False)

        word_layout = QHBoxLayout()
        word_layout.addWidget(self.word_label)
        word_layout.addWidget(self.word)

        self.list_operations = QListWidget(self)

        layout.addLayout(button_group_layout, 0, 0)
        layout.addLayout(word_layout, 1, 0)
        layout.addLayout(date_layout, 1, 0)
        layout.addWidget(self.save_btn, 0, 1)
        layout.addWidget(self.list_operations, 2, 0, 4, 4)


        self.setLayout(layout)
