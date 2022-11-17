import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 400, 400, 350)
        self.setWindowTitle("UFo")
        self.setFixedSize(400, 350)
        self.gg2 = QPixmap('UFO.png')
        self.gg = QLabel(self)
        self.gg.move(10, 100)
        self.gg.setPixmap(self.gg2)
        self.gg.resize(150, 70)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.gg.move(self.gg.x() - 5, self.gg.y())
            if self.gg.x() == -200:
                self.gg.move(350, self.gg.y())
        elif event.key() == Qt.Key_Right:
            self.gg.move(self.gg.x() + 5, self.gg.y())
            if self.gg.x() == 400:
                self.gg.move(-200, self.gg.y())
        elif event.key() == Qt.Key_Up:
            self.gg.move(self.gg.x(), self.gg.y() - 5)
            if self.gg.y() == -70:
                self.gg.move(self.gg.x(), 400)
        elif event.key() == Qt.Key_Down:
            self.gg.move(self.gg.x(), self.gg.y() + 5)
            if self.gg.y() == 405:
                self.gg.move(self.gg.x(), -70)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())