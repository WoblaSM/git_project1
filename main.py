import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox
from PyQt5.QtWidgets import QListWidget, QVBoxLayout, QListWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
import time
from random import randint



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.initUI()
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def initUI(self):
        self.setGeometry(340, 250, 505, 400)
        self.setWindowTitle("жаба симулятор")
        self.ground = QLabel('_____________________________________________________________________________________________________________________________', self)
        self.ground.move(15, 150)
        self.ground2 = QLabel('_____________________________________________________________________________________________________________________________', self)
        self.ground2.move(15, 200)
        self.gg2 = QPixmap('22.png')
        self.gg = QLabel(self)
        self.gg.move(10, 100)
        self.gg.setPixmap(self.gg2)
        self.left = QPushButton('<-', self)
        self.left.resize(50, 50)
        self.left.move(50, 300)
        self.left.clicked.connect(self.l)
        self.right = QPushButton('->', self)
        self.right.resize(50, 50)
        self.right.move(110, 300)
        self.right.clicked.connect(self.r)
        self.pleft = QPushButton('↖', self)
        self.pleft.resize(50, 50)
        self.pleft.move(50, 240)
        self.pleft.clicked.connect(self.pl)
        self.pright = QPushButton('↗', self)
        self.pright.resize(50, 50)
        self.pright.move(110, 240)
        self.pright.clicked.connect(self.pr)
        print(self.gg.pos().x())
        print(self.gg.pos().y())
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        #self.pr = QPushButton('()', self)
        self.p = QPushButton('(⊙ω⊙)', self)
        self.p.clicked.connect(self.paw)
        self.p.move(randint(80, 700), randint(30, 150))
        self.p2 = QPushButton('(⊙ω⊙)', self)
        self.p2.move(randint(80, 700), randint(30, 150))
        self.p2.clicked.connect(self.paw)
        self.p3 = QPushButton('(⊙ω⊙)', self)
        self.p3.move(randint(80, 700), randint(30, 150))
        self.p3.clicked.connect(self.paw)
        self.sch = QLCDNumber(self)
        self.sch.resize(80, 30)



    #def mouseMoveEvent(self, event):
    #    self.xm, self.ym = (event.x(), event.y())
    #    self.pr.move(self.xm - 10, self.ym - 10)
    #    self.repaint()



    def r(self):
        self.gg2 = QPixmap('22.png')
        self.gg.setPixmap(self.gg2)
        self.gg.move(self.gg.pos().x() + 10, self.gg.pos().y())
        if self.gg.pos().x() > 300:
            self.setGeometry(340, 250, 805, 400)

    def l(self):
        self.gg2 = QPixmap('3.png')
        self.gg.setPixmap(self.gg2)
        self.gg.move(self.gg.pos().x() - 10, self.gg.pos().y())

    def pr(self):
        self.gg2 = QPixmap('22.png')
        self.gg.setPixmap(self.gg2)
        y0 = self.gg.pos().y()
        x0 = self.gg.pos().x()
        a = 0.5
        for i in range(0, 41, 1):
            time.sleep(0.002)
            self.gg.move(int(x0 + i * 3), int(y0 + a * (i - 20) ** 2 - a * (-20) ** 2))
            self.repaint()
        if x0 > 300:
            self.setGeometry(340, 250, 805, 400)
        xp1 = self.p.pos().x()
        yp1 = self.p.pos().y()
        xp2 = self.p2.pos().x()
        yp2 = self.p2.pos().y()
        xp3 = self.p3.pos().x()
        yp3 = self.p3.pos().y()
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        if ((self.x0 - xp1) ** 2 + (self.y0 - yp1) ** 2) ** 0.5 < 200:
            self.p.move(randint(80, 700), randint(30, 150))
        if ((self.x0 - xp2) ** 2 + (self.y0 - yp2) ** 2) ** 0.5 < 200:
            self.p2.move(randint(80, 700), randint(30, 150))
        if ((self.x0 - xp3) ** 2 + (self.y0 - yp3) ** 2) ** 0.5 < 200:
            self.p3.move(randint(80, 700), randint(30, 150))


    def pl(self):
        self.gg2 = QPixmap('3.png')
        self.gg.setPixmap(self.gg2)
        y0 = self.gg.pos().y()
        x0 = self.gg.pos().x()
        a = 0.5
        for i in range(0, 41, 1):
            time.sleep(0.002)
            self.gg.move(int(x0 - i * 3), int(y0 + a * (i-20) ** 2 - a * (-20) ** 2))
            self.repaint()
        xp1 = self.p.pos().x()
        yp1 = self.p.pos().y()
        xp2 = self.p2.pos().x()
        yp2 = self.p2.pos().y()
        xp3 = self.p3.pos().x()
        yp3 = self.p3.pos().y()
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        if ((self.x0 - xp1) ** 2 + (self.y0 - yp1) ** 2) ** 0.5 < 200:
            self.p.move(randint(80, 700), randint(30, 150))
        if ((self.x0 - xp2) ** 2 + (self.y0 - yp2) ** 2) ** 0.5 < 200:
            self.p2.move(randint(80, 700), randint(30, 150))
        if ((self.x0 - xp3) ** 2 + (self.y0 - yp3) ** 2) ** 0.5 < 200:
            self.p3.move(randint(80, 700), randint(30, 150))
    def paw(self):
        self.xp = self.sender().pos().x()
        self.yp = self.sender().pos().y()
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        if ((self.x0 - self.xp) ** 2 + (self.y0 - self.yp) ** 2) ** 0.5 > 200:
            print('слишком далеко не могу сесть')
        else:
            print('НЯМ)')
            self.sender().move(randint(80, 700), randint(30, 150))
            self.sch.display(self.sch.value() + 1)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
