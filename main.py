from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QListWidget, QListWidgetItem
from Transaction import Transaction
from AddTransaction import AddTransaction
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Банк")

        transaction_object = Transaction()
        all_counts = transaction_object.get_balance_for_all()

        list_counts = QListWidget(self)
        row = 0
        for k, v in all_counts.items():
            newItem = QListWidgetItem()
            newItem.setText("Счёт: " + str(k) + ". Сумма: " + str(v))
            list_counts.insertItem(row, newItem)
            row += 1


        add_transaction = QPushButton("Создать транзакцию")

        add_transaction.clicked.connect(self.on_pushButton_clicked)


        get_transaction = QPushButton("Получить транзакции")
        get_history = QPushButton("История по текущему счету")
        get_max_use = QPushButton("Отчет по наибольшим взаимодействиям между счетами")

        layout = QGridLayout()
        layout.addWidget(list_counts, 0, 0, 2, 2)
        layout.addWidget(add_transaction , 3, 0)
        layout.addWidget(get_transaction , 3, 1)
        layout.addWidget(get_history , 4, 0)
        layout.addWidget(get_max_use , 4, 1)
        self.setLayout(layout)

    def on_pushButton_clicked(self):
        self.w = AddTransaction()
        self.w.show()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
