import sys
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QMainWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QTableWidgetItem
from PyQt6 import QtCore, QtWidgets

class Name(QWidget):
    def __init__(self, c, t):
        super().__init__()
        self.initUI()
        self.c = c
        self.t = t

    def initUI(self):
        self.setGeometry(300, 300, 280, 150)
        self.setWindowTitle('Name')

        self.btn = QPushButton('Сохранить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.get_name)

        self.label = QLabel(self)
        self.label.setText("В имени можно использовать только\nсимволы латинского алфавита и символ '_'")
        self.label.move(20, 50)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите имя: ")
        self.name_label.move(20, 10)

        self.name_input = QLineEdit(self)
        self.name_input.move(120, 10)

    def get_name(self):
        name = self.name_input.text()
        new_row = [name, str(self.c), str(self.t)]
        with open('save.csv', 'a', newline='', encoding='utf8') as f:
            csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, quotechar='"').writerow(new_row)


def save(c, t):
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = Name(c, t)
    ex.show()
    app.exec()
#save(15, 20)

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Table')
        self.tableWidget = QTableWidget(self)
        self.loadTable('save.csv')

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setSortingEnabled(True)
            self.tableWidget.setFixedSize(300, 300)
            self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


def table():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    app.exec()
#table()