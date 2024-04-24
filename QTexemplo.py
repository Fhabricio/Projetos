import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Exemplo PyQt')
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel('Prometheus teste', self)
        self.label.setGeometry(10, 10, 380, 20)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(10, 40, 380, 200)

        self.ts_tab = QWidget()
        self.tab_widget.addTab(self.ts_tab, 'TS')
        self.ts_button = QPushButton('Clique para TS', self.ts_tab)
        self.ts_button.move(50, 50)
        self.ts_button.clicked.connect(self.tsButtonClick)

        self.bts_tab = QWidget()
        self.tab_widget.addTab(self.bts_tab, 'BTS')
        self.bts_button = QPushButton('Clique para BTS', self.bts_tab)
        self.bts_button.move(50, 50)
        self.bts_button.clicked.connect(self.btsButtonClick)

    def tsButtonClick(self):
        QMessageBox.information(self, 'Mensagem', 'Botão TS clicado!')

    def btsButtonClick(self):
        QMessageBox.information(self, 'Mensagem', 'Botão BTS clicado!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec_())
