import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from StarWarsLabels import Ui_Dialog

class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Star Wars Characters")
        self.n = 0
        
        self.previous_button.clicked.connect(lambda: self.wyswietlanie(0))
        self.next_button.clicked.connect(lambda: self.wyswietlanie(1))

    def wyswietlanie(self, which):
        #instrukcja warunkowa do zmiany stron
        if which == 0:
            self.n -= 1
        elif which == 1:
            self.n += 1
        
        #pobieramy api z swapi
        response = requests.get(f"https://swapi.dev/api/people/{self.n}/")
        data = response.json()

        #tworzymy odpowiedni label
        self.label.setText(f"My name is <span style='color:#03fc90'>{data['name']}</span> and I have <span style='color:#03fc90'>{data['height']}</span> cm height !!")
        self.label 
        self.pages.setText(f"Page {self.n}")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())