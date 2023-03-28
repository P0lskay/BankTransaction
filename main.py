from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QListWidget, QListWidgetItem
from Transaction import Transaction
from AddTransaction import AddTransaction
from GetTransactions import GetTransactions
from GetHistory import GetHistory


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Банк")

        self.transaction_object = Transaction()

        self.list_counts = QListWidget(self)
        self.refresh_transactions_list()

        add_transaction = QPushButton("Создать транзакцию")
        add_transaction.clicked.connect(self.on_addButton_clicked)

        get_transaction = QPushButton("Получить транзакции")
        get_transaction.clicked.connect(self.on_getButton_clicked)

        get_history = QPushButton("История по текущему счету")
        get_history.clicked.connect(self.on_historyButton_clicked)

        get_max_use = QPushButton("Отчет по наибольшим взаимодействиям между счетами")

        layout = QGridLayout()
        layout.addWidget(self.list_counts, 0, 0, 2, 2)
        layout.addWidget(add_transaction, 3, 0)
        layout.addWidget(get_transaction, 3, 1)
        layout.addWidget(get_history, 4, 0)
        layout.addWidget(get_max_use, 4, 1)
        self.setLayout(layout)

    def on_addButton_clicked(self):
        self.add_w = AddTransaction(self)
        self.add_w.show()

    def on_getButton_clicked(self):
        self.get_w = GetTransactions(self)
        self.get_w.show()

    def on_historyButton_clicked(self):
        self.get_w = GetHistory(self)
        self.get_w.show()

    def refresh_transactions_list(self):
        self.list_counts.clear()
        all_counts = self.transaction_object.get_balance_for_all()
        row = 0
        for k, v in all_counts.items():
            newItem = QListWidgetItem()
            newItem.setText("Счёт: " + str(k) + ". Сумма: " + str(v))
            self.list_counts.insertItem(row, newItem)
            row += 1

    def input_new_transaction(self, new_transaction: list, is_operation: bool):
        new_transaction_lst = new_transaction.split()
        if is_operation:
            self.transaction_object.add_operation(new_transaction_lst[0], new_transaction_lst[1],
                                                  new_transaction_lst[2],
                                                  new_transaction_lst[3],
                                                  ("", ' '.join(new_transaction_lst[4:]))[len(new_transaction_lst) > 4])
        else:
            self.transaction_object.add_count(new_transaction_lst[0], new_transaction_lst[1], new_transaction_lst[2])
        self.refresh_transactions_list()

    def get_transactions_with_word(self, search_word):
        return Transaction.get_transaction_with_word(Transaction,search_word)

    def get_transactions_per_date(self, search_date):
        return Transaction.get_transaction_per_date(Transaction, str(search_date))

    def get_history_transactions(self, count, start_date, end_date):
        return Transaction.get_history_for_count(Transaction, str(count), str(start_date), str(end_date))


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
