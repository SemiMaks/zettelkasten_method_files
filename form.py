import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


# подкласс QMain Window для настройки главного окна приложения
class MainWIndow(QMainWindow):
    def __init__(self):
        super(MainWIndow, self).__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        self.setFixedSize(QSize(500, 600))

        # устанавливаем центральный виджет Window
        self.setCentralWidget(button)

    # def the_button_was_clicked(self):
    #     print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
        print(self.button_is_checked)


app = QApplication(sys.argv)
# window = QWidget()
# window = QPushButton("Нажми меня")
# window = QMainWindow()
window = MainWIndow()
window.show()

app.exec()
