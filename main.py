from decimal import Decimal

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

from balance import Balance

NUMBER_REGEX = QRegExp(r'^\d+(.\d\d)?$')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._balance = Balance()
        self.value_field = None
        self.balance_value = None
        self.init_ui()

    def init_ui(self):
        with open('app.css', 'r') as file:
            self.setStyleSheet(file.read())

        balance_caption = QLabel('Баланс')
        balance_caption.setProperty('class', 'caption')

        balance_value = QLabel(self.get_balance_text())
        balance_value.setProperty('class', 'primary')
        self.balance_value = balance_value

        update_btn = QPushButton('Обновить')
        update_btn.clicked.connect(self.update_balance)

        value_field = QLineEdit()
        value_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        value_field.setValidator(QRegExpValidator(NUMBER_REGEX))
        self.value_field = value_field

        balance_layout = QVBoxLayout()
        balance_layout.setContentsMargins(0, 0, 0, 8)
        balance_layout.setSpacing(0)
        balance_layout.addWidget(balance_caption)
        balance_layout.addWidget(balance_value)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(8)
        main_layout.addLayout(balance_layout)
        main_layout.addWidget(value_field)
        main_layout.addWidget(update_btn)

        self.setLayout(main_layout)
        self.show()

    def update_balance(self):
        self._balance.usd = Decimal(self.value_field.text())
        self.balance_value.setText(self.get_balance_text())

    def get_balance_text(self):
        return '$ {0:.2f}'.format(self._balance.usd)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
