from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 335)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.lineEdit_result = QLineEdit(self.centralwidget)
        self.lineEdit_result.setObjectName(u"lineEdit_result")
        self.lineEdit_result.setAlignment(Qt.AlignRight)
        self.lineEdit_result.setReadOnly(True)
        self.verticalLayout.addWidget(self.lineEdit_result)
        
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        
        # دکمه‌ها
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setText("1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText("3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        
        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setSizePolicy(sizePolicy)
        self.pushButton_plus.setText("+")
        self.gridLayout.addWidget(self.pushButton_plus, 0, 3, 1, 1)
        
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setText("4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setText("5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setText("6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        
        self.pushButton_multiply = QPushButton(self.centralwidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setSizePolicy(sizePolicy)
        self.pushButton_multiply.setText("*")
        self.gridLayout.addWidget(self.pushButton_multiply, 1, 3, 1, 1)
        
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setText("7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setText("8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setText("9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        
        self.pushButton_substract = QPushButton(self.centralwidget)
        self.pushButton_substract.setObjectName(u"pushButton_substract")
        self.pushButton_substract.setSizePolicy(sizePolicy)
        self.pushButton_substract.setText("-")
        self.gridLayout.addWidget(self.pushButton_substract, 2, 3, 1, 1)
        
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setText("C")
        self.gridLayout.addWidget(self.pushButton_clear, 3, 0, 1, 1)
        
        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setText("0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)
        
        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setSizePolicy(sizePolicy)
        self.pushButton_equal.setText("=")
        self.gridLayout.addWidget(self.pushButton_equal, 3, 2, 1, 1)
        
        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setSizePolicy(sizePolicy)
        self.pushButton_divide.setText("/")
        self.gridLayout.addWidget(self.pushButton_divide, 3, 3, 1, 1)
        
        self.verticalLayout.addLayout(self.gridLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 22))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))