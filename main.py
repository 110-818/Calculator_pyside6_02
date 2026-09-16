import sys
from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from main_window import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(10):
            button = getattr(self.ui, f"pushButton_{i}")
            button.clicked.connect(partial(self.add_num, str(i)))

        operators = {
            "plus": "+",
            "substract": "-",
            "multiply": "×",
            "divide": "÷"
        }
        for name, symbol in operators.items():
            button = getattr(self.ui, f"pushButton_{name}")
            button.clicked.connect(partial(self.set_operator, symbol))

        self.ui.pushButton_equal.clicked.connect(self.equaling)
        self.ui.pushButton_clear.clicked.connect(self.clear)

        self.total = 0
        self.operator = ''
        self.text_line = ''

    def add_num(self, text):
        current = self.ui.lineEdit_result.text()
        self.ui.lineEdit_result.setText(current + text)

    def set_operator(self, symbol):
        self.text_line = self.ui.lineEdit_result.text()
        self.operator = symbol
        self.ui.lineEdit_result.setText("")

    def equaling(self):
        second_text = self.ui.lineEdit_result.text()
        if second_text == "":
            QMessageBox.warning(self, "خطا", "لطفاً عدد دوم را وارد کنید!")
            return

        if self.operator == "":
            QMessageBox.warning(self, "خطا", "لطفاً یک عملگر انتخاب کنید!")
            return

        try:
            first = float(self.text_line)
            second = float(second_text)

            if self.operator == '+':
                result = first + second
            elif self.operator == '-':
                result = first - second
            elif self.operator == '×':
                result = first * second
            elif self.operator == '÷':
                if second == 0:
                    QMessageBox.warning(self, "خطا", "تقسیم بر صفر ممکن نیست!")
                    return
                result = first / second
            else:
                return

            if result == int(result):
                self.ui.lineEdit_result.setText(str(int(result)))
            else:
                self.ui.lineEdit_result.setText(str(result))

            self.operator = ''
            self.text_line = ''

        except ValueError:
            QMessageBox.warning(self, "خطا", "لطفاً فقط عدد وارد کنید!")
            self.clear()

    def clear(self):
        self.ui.lineEdit_result.setText("")
        self.operator = ''
        self.text_line = ''


app = QApplication(sys.argv)
main = Main()
main.show()
app.exec()
