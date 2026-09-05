import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from window import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_0.clicked.connect(lambda:self.add_num('0'))
        self.ui.pushButton_1.clicked.connect(lambda:self.add_num('1'))
        self.ui.pushButton_2.clicked.connect(lambda:self.add_num('2'))
        self.ui.pushButton_3.clicked.connect(lambda:self.add_num('3'))
        self.ui.pushButton_4.clicked.connect(lambda:self.add_num('4'))
        self.ui.pushButton_5.clicked.connect(lambda:self.add_num('5'))
        self.ui.pushButton_6.clicked.connect(lambda:self.add_num('6'))
        self.ui.pushButton_7.clicked.connect(lambda:self.add_num('7'))
        self.ui.pushButton_8.clicked.connect(lambda:self.add_num('8'))
        self.ui.pushButton_9.clicked.connect(lambda:self.add_num('9'))
        self.ui.pushButton_plus.clicked.connect(lambda:self.gathering())
        self.ui.pushButton_substract.clicked.connect(lambda:self.subtracting())
        self.ui.pushButton_multiply.clicked.connect(lambda:self.Multiplying())
        self.ui.pushButton_divide.clicked.connect(lambda:self.dividing())
        self.ui.pushButton_equal.clicked.connect(lambda:self.equaling())
        self.ui.pushButton_clear.clicked.connect(lambda:self.clear())

        self.total = 0            # مجموع عدد 
        self.operator = ''
        self.text_line = ''

    def add_num(self,text:str = None):             
        text_line = self.ui.lineEdit_result.text()
        self.ui.lineEdit_result.setText(text_line + text)

    def gathering(self):                    #جمع کردن
        self.text_line  = self.ui.lineEdit_result.text()
        self.operator = '+'
        self.ui.lineEdit_result.setText(None)
        

    def subtracting(self):                      #تفریق کردن
        self.text_line  = self.ui.lineEdit_result.text()
        self.operator = '-'
        self.ui.lineEdit_result.setText(None)
                
        

    def Multiplying(self):                               #ضرب کردن
        self.text_line = self.ui.lineEdit_result.text()
        self.operator = '×'
        self.ui.lineEdit_result.setText(None)
                

    def dividing(self):                          #تقسیم کردن
        self.text_line = self.ui.lineEdit_result.text()
        self.operator = '÷'
        self.ui.lineEdit_result.setText(None)        

    def equaling(self):                           # نشان دادن مجموع
        if self.operator == '+':
            text = int(self.text_line) + int(self.ui.lineEdit_result.text())
            self.ui.lineEdit_result.setText(str(text))

        elif self.operator == '-':
            text = int(self.text_line) - int(self.ui.lineEdit_result.text())
            self.ui.lineEdit_result.setText(str(text))

        elif self.operator == '×':
            text = int(self.text_line) * int(self.ui.lineEdit_result.text())
            self.ui.lineEdit_result.setText(str(text))

        elif self.operator == '÷':
            text = int(self.text_line) / int(self.ui.lineEdit_result.text())
            self.ui.lineEdit_result.setText(str(text))

    def clear(self):                              #پاک کردن
        self.ui.lineEdit_result.setText(None)
        

app = QApplication(sys.argv)
main = Main()
main.show()
app.exec()