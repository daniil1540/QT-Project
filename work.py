from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit

im = Image.open("images.jpg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения
red = 0
blue = 0
green = 0
yelloworange = 0
yellow = 0
greenyellow = 0
cvetligreen = 0
orange = 0
ottenokorange = 0
brown = 0
purple = 0
ottenokpurple = 0
ottenokgray = 0
gray = 0
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        if r >= 248 and r <= 255 and g >= 3 and g <= 43 and b >= 43 and b <= 71:
            red += 1
        elif r >= 0 and r <= 50 and g >= 0 and g <= 50 and b >= 63 and b <= 255:
            blue += 1
        elif r >= 239 and r <= 255 and g >= 208 and g <= 255 and b >= 0 and b <= 51:
            yellow += 1
        elif  r >= 228 and r <= 255 and g >= 155 and g <= 207 and b >= 0 and b <= 70:
            orange += 1
        elif r >= 0 and r <= 34 and g >= 128 and g <= 200 and b >= 0 and b <= 120:
            green += 1
        elif r >= 84 and r <= 153 and g >= 201 and g <= 255 and b >= 23 and b <= 159:
            cvetligreen += 1
        elif r >= 147 and r <= 255 and g >= 170 and g <= 255 and  b >= 0 and b <= 116:
            greenyellow += 1
        elif r >= 230 and r <= 255 and g >= 202 and g <= 255 and b >= 88 and b <= 183:
            ottenokorange += 1
        elif r >= 184 and r <= 210 and g >= 168 and g <= 184 and b >= 133 and b <= 153:
            ottenokgray += 1
        elif r >= 94 and r <= 128 and g >= 66 and g >= 129 and b >= 15 and b <= 72:
            brown += 1
        elif r >= 50 and r <= 79 and g >= 0 and g <= 42 and b >= 39 and b <= 64:
            purple += 1
        elif r >= 106 and r <= 153 and g >= 0 and g <= 104 and b >= 169 and b <= 255:
            ottenokpurple += 1
        elif r >= 125 and r <= 138 and g >= 112 and g <= 130 and b >= 102 and b <= 142:
            gray += 1


vse = gray + ottenokpurple + brown + ottenokgray + ottenokorange + greenyellow + green
vse += cvetligreen
vse += orange
vse += yellow
vse += blue
vse += red
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Шестая программа')

        self.labelred = QLabel(self)
        self.labelred.setText("red -", (red // vse) * 100)
        self.labelred.move(40, 30)

        self.labelblue = QLabel(self)
        self.labelblue.setText("blue -", (blue // vse) * 100)
        self.labelblue.move(40, 40)

        self.labelgreen = QLabel(self)
        self.labelgreen.setText("green -", (green // vse) * 100)
        self.labelgreen.move(40, 50)

        self.labelorange = QLabel(self)
        self.labelorange.setText("orange -", (orange // vse) * 100)
        self.labelorange.move(40, 60)

        self.labelyellow = QLabel(self)
        self.labelyellow.setText("yellow -", (yellow // vse) * 100)
        self.labelyellow.move(40, 70)

        self.labelyelloworange = QLabel(self)
        self.labelyelloworange.setText("yelloworange -", (yelloworange // vse) * 100)
        self.labelyelloworange.move(40, 80)

        self.labelottenokorange = QLabel(self)
        self.labelottenokorange.setText("ottenokorange -", (ottenokorange // vse) * 100)
        self.labelottenokorange.move(40, 90)

        self.labelbrown = QLabel(self)
        self.labelbrown.setText("brown -", (brown // vse) * 100)
        self.labelbrown.move(40, 100)

        self.labelpurple = QLabel(self)
        self.labelpurple.setText("purple -", (purple // vse) * 100)
        self.labelpurple.move(40, 110)

        self.labelottenokpurple = QLabel(self)
        self.labelottenokpurple.setText("ottenokpurple -", (ottenokpurple // vse) * 100)
        self.labelottenokpurple.move(40, 120)

        self.labelgray = QLabel(self)
        self.labelgray.setText("gray -", (gray // vse) * 100)
        self.labelgray.move(40, 130)

        self.labelottenokgray = QLabel(self)
        self.labelottenokgray.setText("ottenokgray -", (ottenokgray // vse) * 100)
        self.labelottenokgray.move(40, 140)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())