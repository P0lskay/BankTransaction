from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QListWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Банк")

        list_counts = QListWidget(self)

        add_transaction = QPushButton("Создать транзакцию")
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


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
