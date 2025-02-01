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
        self.label.setText("В имени можно использовать только\nсимволы латинского алфавита,\nцифры и символ '_'")
        self.label.move(20, 50)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите имя: ")
        self.name_label.move(20, 10)

        self.name_input = QLineEdit(self)
        self.name_input.move(120, 10)

    def get_name(self):
        name = self.name_input.text()
        for el in name:
            if el.lower() not in 'qwertyuiopasdfghjklzxcvbnm1234567890_':
                return
        new_row = [name, str(self.c), str(self.t)]
        with open('save.csv', 'a', newline='', encoding='utf8') as f:
            csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, quotechar='"').writerow(new_row)
        self.close()


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
        self.setGeometry(300, 300, 300, 325)
        self.setFixedSize(300, 325)
        self.setWindowTitle('Table')

        self.i = None
        self.table_name = 'save.csv'

        self.btn = QPushButton('Удалить запись', self)
        self.btn.resize(140, 20)
        self.btn.move(5, 305)
        self.btn.clicked.connect(self.delete_record)
        self.btn.setEnabled(False)

        self.btn1 = QPushButton('Удалить все записи', self)
        self.btn1.resize(140, 20)
        self.btn1.move(150, 305)
        self.btn1.clicked.connect(self.delete_all)

        self.tableWidget = QTableWidget(self)
        self.loadTable()
        self.tableWidget.cellClicked.connect(self.click)

    def loadTable(self):
        with open(self.table_name, encoding="utf8") as csvfile:
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

    def click(self, i):
        self.i = self.tableWidget.currentIndex().row()
        self.btn.setEnabled(True)
        print(self.i)

    def delete_record(self):
        if self.i != None:
            with open(self.table_name, encoding="utf8", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                rows = [row for idx, row in enumerate(reader) if idx != self.i]
                print(rows)
            with open(self.table_name, 'w') as f:
                writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, quotechar='"', lineterminator='\r')
                writer.writerows(rows)
            self.loadTable()

    def delete_all(self):
        with open(self.table_name, encoding="utf8", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            row = list(reader)[0]
        with open(self.table_name, 'w') as f:
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, quotechar='"', lineterminator='\r')
            writer.writerow(row)
        self.loadTable()


def table():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    app.exec()
table()