from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem, QGridLayout, QWidget, QRadioButton, \
    QButtonGroup, QVBoxLayout, QDateEdit, QLineEdit, QLabel, QHBoxLayout




class AddTransaction(QWidget):
    def _on_radio_button_clicked(self):
        if self.rb_create_operation.isChecked():
            self.count_in.setVisible(True)
            self.count_in_label.setVisible(True)
            self.comment.setVisible(True)
            self.comment_label.setVisible(True)
            self.count_in_label.setVisible(True)

            self.count_out_label.setText("От: ")
        elif self.rb_create_count.isChecked():
            self.count_in.setVisible(False)
            self.count_in_label.setVisible(False)
            self.comment.setVisible(False)
            self.count_in_label.setVisible(False)
            self.comment_label.setVisible(False)

            self.count_out_label.setText("Номер счета: ")

    def _on_save_btn_clicked(self):
        if self.rb_create_operation.isChecked() and self.count_out.text() != "" and self.count_in.text() != "" \
                and self.sum.text() != "":
            new_operation = str(self.date_input.text()) + " " + self.count_out.text() + " " + self.count_in.text() \
                            + " " + self.sum.text() + " " + self.comment.text()
            self.parent().input_new_transaction(new_operation, True)
            self.close()
        elif self.rb_create_count.isChecked() and self.count_out.text() != "" and self.sum.text() != "":
            new_count = str(self.date_input.text()) + " " + self.count_out.text() + " " + self.sum.text()
            self.parent().input_new_transaction(new_count, False)
            self.close()


    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        layout = QGridLayout()
        self.rb_create_count = QRadioButton('Создать счёт')

        self.rb_create_operation = QRadioButton('Создать операцию')
        self.rb_create_operation.setChecked(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.rb_create_count)
        self.button_group.addButton(self.rb_create_operation)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        button_group_layout = QVBoxLayout()
        button_group_layout.addWidget(self.rb_create_count)
        button_group_layout.addWidget(self.rb_create_operation)

        self.save_btn = QPushButton("Сохранить и закрыть")
        self.save_btn.clicked.connect(self._on_save_btn_clicked)
        self.date_input = QDateEdit()

        self.count_out_label = QLabel("От: ")
        self.count_out = QLineEdit()
        self.count_in_label = QLabel("Кому: ")
        self.count_in = QLineEdit()

        count_layout = QHBoxLayout()
        count_layout.addWidget(self.count_out_label)
        count_layout.addWidget(self.count_out)
        count_layout.addWidget(self.count_in_label)
        count_layout.addWidget(self.count_in)

        self.sum_label = QLabel("Сумма: ")
        self.sum = QLineEdit()

        sum_layout = QHBoxLayout()
        sum_layout.addWidget(self.sum_label)
        sum_layout.addWidget(self.sum)

        self.comment_label = QLabel("Примечание: ")
        self.comment = QLineEdit()

        comment_layout = QHBoxLayout()
        comment_layout.addWidget(self.comment_label)
        comment_layout.addWidget(self.comment)

        layout.addLayout(button_group_layout, 0, 0)
        layout.addWidget(self.save_btn, 0, 1)
        layout.addWidget(self.date_input, 1, 0)
        layout.addLayout(count_layout, 2, 0)
        layout.addLayout(sum_layout, 3, 0)
        layout.addLayout(comment_layout, 5, 0)

        self.setLayout(layout)
