import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox
from PyQt5.QtWidgets import QListWidget, QVBoxLayout, QListWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QInputDialog
import time
from random import randint
import threading as th


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.initUI()
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def initUI(self):
        self.rot = 'r'
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
        self.pleft = QPushButton(' ↑', self)
        self.pleft.resize(50, 50)
        self.pleft.move(50, 240)
        self.pleft.clicked.connect(self.pl)
        self.pright = QPushButton('↓', self)
        self.pright.resize(50, 50)
        self.pright.move(110, 240)
        self.pright.clicked.connect(self.pr)
        print(self.gg.pos().x())
        print(self.gg.pos().y())
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        self.w = 0
        self.ch2 = QPixmap('chort.png')
        self.ch = QLabel(self)
        self.ch.move(300, 160)
        self.ch.setPixmap(self.ch2)
        self.at = QPushButton('🗡', self)
        self.at.resize(50, 50)
        self.at.move(170, 300)
        self.at.clicked.connect(self.paw)
        self.t = QLabel("HP", self)
        self.t.move(10, 10)
        self.HP = QLabel('100', self)
        self.HP.move(80, 15)
        self.qw = True
        self.hp = QLabel('100', self)
        self.hp.move(400, 15)
        self.shop = QPushButton('shop', self)
        self.shop.clicked.connect(self.magaz)
        self.shop.resize(150, 40)
        self.shop.move(10, 40)
        self.shans = 0
        self.yr = 0
        self.sty = QLabel('урон - ' + str(self.yr), self)
        self.sty.move(400, 280)
        self.stp = QLabel('щанс - ' + str(self.shans) + '                  ', self)
        self.stp.move(400, 300)
        self.e = QPushButton('📦', self)
        self.e.resize(50, 50)
        self.e.move(170, 240)
        self.e.clicked.connect(self.qqwett)
        self.sas = False




        def sctn():
            if int(self.HP.text()) <= 0:
                self.gg.close()
                self.close()
            if self.qw:
                self.xp = self.ch.pos().x()
                self.yp = self.ch.pos().y()
                self.y0 = self.gg.pos().y()
                self.x0 = self.gg.pos().x()
                if ((self.x0 - self.xp) ** 2 + (self.y0 - self.yp) ** 2) ** 0.5 < 60:
                    if randint(0, 10) == 4:
                        self.HP.setText(str(int(self.HP.text()) - 10))
            if self.w == 0:
                self.ch2 = QPixmap('chort.png')
                self.ch.setPixmap(self.ch2)
                if self.rot == 'r':
                    self.gg2 = QPixmap('pum1.png')
                    self.gg.setPixmap(self.gg2)
                    self.w = 1
                else:
                    self.gg2 = QPixmap('pum12.png')
                    self.gg.setPixmap(self.gg2)
                    self.w = 1
            else:
                self.ch2 = QPixmap('chort2.png')
                self.ch.setPixmap(self.ch2)
                if self.rot == 'l':
                    self.gg2 = QPixmap('pum22.png')
                    self.gg.setPixmap(self.gg2)
                    self.w = 0
                else:
                    self.gg2 = QPixmap('pum2.png')
                    self.gg.setPixmap(self.gg2)
                    self.w = 0
            S = th.Timer(0.1, sctn)
            S.start()


        S = th.Timer(0.1, sctn)
        S.start()



    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw_flag(self.qp)
        self.qp.end()

    def qqwett(self):
        self.sas = True
        self.draw_flag(self.qp)
        self.sas = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(40, 5, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(370, 5, 120, 30)
        if self.sas:
            qp.setBrush(QColor(0, 255, 0))
            qp.drawRect(self.y0, self.x0, self.x0, self.y0)







    #def mouseMoveEvent(self, event):
    #    self.xm, self.ym = (event.x(), event.y())
    #    self.pr.move(self.xm - 10, self.ym - 10)
    #    self.repaint()



    def r(self):
        self.rot = 'r'
        self.gg.move(self.gg.pos().x() + 10, self.gg.pos().y())

    def l(self):
        self.rot = 'l'
        self.gg.move(self.gg.pos().x() - 10, self.gg.pos().y())

    def pr(self):
        self.gg.move(self.gg.pos().x(), self.gg.pos().y() + 10)
        """self.gg2 = QPixmap('pum1.png')
        self.gg.setPixmap(self.gg2)
        y0 = self.gg.pos().y()
        x0 = self.gg.pos().x()
        a = 0.5
        for i in range(0, 41, 1):
            time.sleep(0.002)
            self.gg.move(int(x0 + i * 3), int(y0 + a * (i - 20) ** 2 - a * (-20) ** 2))
            self.repaint()"""



    def pl(self):
        self.gg.move(self.gg.pos().x(), self.gg.pos().y() - 10)
        """self.gg2 = QPixmap('pum1.png')
        self.gg.setPixmap(self.gg2)
        y0 = self.gg.pos().y()
        x0 = self.gg.pos().x()
        a = 0.5
        for i in range(0, 41, 1):
            time.sleep(0.002)
            self.gg.move(int(x0 - i * 3), int(y0 + a * (i-20) ** 2 - a * (-20) ** 2))
            self.repaint()"""


    def paw(self):
        self.xp = self.ch.pos().x()
        self.yp = self.ch.pos().y()
        self.y0 = self.gg.pos().y()
        self.x0 = self.gg.pos().x()
        if ((self.x0 - self.xp) ** 2 + (self.y0 - self.yp) ** 2) ** 0.5 > 60:
            pass
        else:
            if self.qw:
                if randint(0, 10 - self.shans) == 0:
                    self.hp.setText(str(int(self.hp.text()) - self.yr))
                    if int(self.hp.text()) <= 0:
                        self.ch.close()
                        self.qw = False

    def magaz(self):
        self.run2()

    def run(self):
        self.ar, ok_pressed = QInputDialog.getItem(
            self, "", "что купить?",
            ("мечь(15🗡, 5%)", "кортик(5🗡, 9%)", "кинжал(10🗡, 7%)"), 1, False)
        if ok_pressed:
            if self.ar == "мечь(15🗡)":
                self.yr = 15
                self.shans = 5
                self.sty.setText('урон - ' + str(self.yr) + '                  ')
                self.stp.setText('щанс - ' + str(self.shans) + '                  ')

            elif self.ar == "кортик(5🗡)":
                self.yr = 5
                self.shans = 10
                self.sty.setText('урон - ' + str(self.yr) + '                  ')
                self.stp.setText('щанс - ' + str(self.shans) + '                  ')
            else:
                self.yr = 10
                self.shans = 7
                self.sty.setText('урон - ' + str(self.yr) + '                  ')
                self.stp.setText('щанс - ' + str(self.shans) + '                  ')

    def run2(self):
        self.ar, ok_pressed = QInputDialog.getItem(
            self, "", "что купить?",
            ("оружие", "броня", "HP"), 1, False)
        if ok_pressed:
            if self.ar == "оружие":
                self.run()
            elif self.ar == "броня":
                self.run3()
            else:
                self.HP.setText(str(int(self.HP.text()) + 10))

    def run3(self):
        self.ar, ok_pressed = QInputDialog.getItem(
            self, "", "что купить?",
            ("кальчуга(10🛡)", "латы(20🛡)"), 1, False)
        if ok_pressed:
            if self.ar == "кальчуга(10🛡)":
                self.HP.setText(str(int(self.HP.text()) + 10))

            elif self.ar == "латы(20🛡)":
                self.HP.setText(str(int(self.HP.text()) + 20))
                self.shans -= 3
                self.stp.setText('щанс - ' + str(self.shans) + '                  ')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
