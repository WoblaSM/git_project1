import math
import sys
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from random import randint
from PyQt5.QtCore import Qt, QPoint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.name ="5"
        self.fig = ['rect', 10, 10, 20, 20]
        self.initUI()
        self.xm, self.ym = (0,0)


    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Супрематизм")
        # self.t = QPushButton("задать кол-во цветов", self)
        # self.t.clicked.connect(self.run)
        # self.run()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw_flag(self.qp)
        self.qp.end()

    def mouseMoveEvent(self, event):
        self.xm, self.ym = (event.x(), event.y())


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            w = randint(1, 100)
            self.fig = ['triangl', self.xm, self.ym, self.xm, self.ym, w, w]
        self.repaint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            w = randint(1, 100)
            self.fig = ['elips', self.xm, self.ym, w, w]
        elif event.button() == Qt.RightButton:
            w = randint(1, 100)
            self.fig = ['rect', self.xm, self.ym, w, w]
        self.repaint()

    def draw_flag(self, qp):
        if self.fig[0] == 'triangl':
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            l = randint(1, 109)
            h = int(math.sqrt(l**2 - (l/2)**2))

            self.qp.drawPolygon(
                QPolygon([
                    QPoint(self.fig[1], self.fig[2]),
                    QPoint(self.fig[1] + l, self.fig[2]),
                    QPoint(self.fig[1] + l//2, self.fig[2] - h)
                ]))

        elif self.fig[0] == 'rect':
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(self.fig[1], self.fig[2], self.fig[3], self.fig[4])
        elif self.fig[0] == 'elips':
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(self.fig[1], self.fig[2], self.fig[3], self.fig[4])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
