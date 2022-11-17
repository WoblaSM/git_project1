import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from random import randint
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.kv = False
        self.qp = QPainter()
        self.t = QPushButton("задать кол-во цветов", self)
        self.xm, self.ym = (0, 0)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Рисование")

    def mouseMoveEvent(self, event):
        self.xm, self.ym = (event.x(), event.y())

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw_flag()
        self.qp.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.qp.begin(self)
            self.kv = True
            self.qp.end()
        elif event.button() == Qt.RightButton:
            print(2)

    def draw_flag(self):
        if self.kv:
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(self.xm, self.ym, 120, 30)
            self.repaint()
            self.kv = False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
