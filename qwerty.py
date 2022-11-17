import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton


SCREEN_SIZE = [1000, 500]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('PIL 2.0')

        ## Изображение
        self.qwerty = 0

        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.im = Image.open(self.fname)
        self.pixels = self.im.load()  # список с пикселями
        self.x, self.y = self.im.size  # ширина (x) и высота (y) изображения
        self.u = self.pixels

        self.im.save("qwer.jpg")
        self.pixmap = QPixmap("qwer.jpg")
        # Если картинки нет, то QPixmap будет пустым, 
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1000, 500)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)
        self.t = QPushButton('R', self)
        self.t.clicked.connect(self.r)
        self.t.move(610, 5)
        self.p = QPushButton('g', self)
        self.p.move(610, 65)
        self.p.clicked.connect(self.g)
        self.q = QPushButton('b', self)
        self.q.move(610, 125)
        self.q.clicked.connect(self.b)
        self.ll = QPushButton('all', self)
        self.ll.move(610, 185)
        self.ll.clicked.connect(self.all)
        self.rl = QPushButton('повернуть против часовой', self)
        self.rl.move(610, 245)
        self.rl.clicked.connect(self.rotl)
        self.rr = QPushButton('повернуть по часовой', self)
        self.rr.move(610, 305)
        self.rr.clicked.connect(self.rotr)


    def r(self):
        self.im = Image.open(self.fname)
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = r, 0, 0
        self.im = self.im.rotate(90 * self.qwerty)
        self.im.save("qwer.jpg")
        self.pixmap = QPixmap("qwer.jpg")
        self.image.setPixmap(self.pixmap)

    def g(self):
        self.im = Image.open(self.fname)
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, g, 0
        self.im = self.im.rotate(90 * self.qwerty)
        self.im.save("qwer.jpg")
        self.pixmap = QPixmap("qwer.jpg")
        self.image.setPixmap(self.pixmap)

    def b(self):
        self.im = Image.open(self.fname)
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, 0, b
        self.im = self.im.rotate(90 * self.qwerty)
        self.im.save("qwer.jpg")
        self.pixmap = QPixmap("qwer.jpg")
        self.image.setPixmap(self.pixmap)

    def all(self):
        self.im = Image.open(self.fname)
        self.im = self.im.rotate(90 * self.qwerty)
        self.image.setPixmap(QPixmap(self.fname))

    def rotl(self):
        self.qwerty = (self.qwerty + 1) % 4
        im_rotate = self.im.rotate(90 * self.qwerty)
        print(self.qwerty)
        im_rotate.save("qwer.jpg")

        self.pixmap = QPixmap("qwer.jpg")
        self.image.setPixmap(self.pixmap)

    def rotr(self):
        self.qwerty = (3 + self.qwerty) % 4
        im_rotate = self.im.rotate(90 * self.qwerty)
        print(self.qwerty)
        im_rotate.save("qwer.jpg")

        self.pixmap = QPixmap("qwer.jpg")
        self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())