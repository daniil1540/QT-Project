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
white = 0
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
        elif r >= 0 and r <= 50 and g >= 0 and g <= 199 and b >= 63 and b <= 255:
            blue += 1
        elif r >= 239 and r <= 255 and g >= 208 and g <= 255 and b >= 0 and b <= 51:
            yellow += 1
        elif  r >= 228 and r <= 255 and g >= 155 and g <= 207 and b >= 0 and b <= 70:
            orange += 1
        elif r >= 0 and r <= 153 and g >= 128 and g <= 255 and b >= 0 and b <= 159:
            green += 1
        elif r >= 193 and r <= 255 and g >= 202 and g <= 255 and b >= 202 and b <= 255:
            white += 1
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
vse += white
vse += orange
vse += yellow
vse += blue
vse += red

reds = 'red - '

blues = 'blue - '

greens = 'green - '

oranges = 'orange - '

whites = 'white - '

yellows = 'yellow - '

yelloworanges = 'yelloworange - '

ottenokoranges = 'ottenokorange - '

browns = 'brown - '

purples = 'purple - '

ottenokpurples = 'ottenokpurple - '

grays = 'gray - '

ottenokgrays = 'ottenokgray - '

reds += str((red / vse) * 100)

blues += str((blue / vse) * 100)

greens += str((green / vse) * 100)

oranges += str((orange / vse) * 100)

yellows += str((yellow / vse) * 100)

yelloworanges += str((yelloworange / vse) * 100)

ottenokoranges += str((ottenokorange / vse) * 100)

browns += str((brown / vse) * 100)

purples += str((purple / vse) * 100)

ottenokpurples += str((ottenokpurple / vse) * 100)

grays += str((gray / vse) * 100)

ottenokgrays += str((ottenokgray / vse) * 100)

whites += str((white / vse) * 100)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Шестая программа')

        self.labelred = QLabel(self)
        self.labelred.setText(reds)
        self.labelred.move(40, 30)

        self.labelblue = QLabel(self)
        self.labelblue.setText(blues)
        self.labelblue.move(40, 60)

        self.labelgreen = QLabel(self)
        self.labelgreen.setText(greens)
        self.labelgreen.move(40, 90)

        self.labelorange = QLabel(self)
        self.labelorange.setText(oranges)
        self.labelorange.move(40, 120)

        self.labelyellow = QLabel(self)
        self.labelyellow.setText(yellows)
        self.labelyellow.move(40, 150)

        self.labelyelloworange = QLabel(self)
        self.labelyelloworange.setText(yelloworanges)
        self.labelyelloworange.move(40, 180)

        self.labelottenokorange = QLabel(self)
        self.labelottenokorange.setText(ottenokoranges)
        self.labelottenokorange.move(40, 210)

        self.labelbrown = QLabel(self)
        self.labelbrown.setText(browns)
        self.labelbrown.move(40, 240)

        self.labelpurple = QLabel(self)
        self.labelpurple.setText(purples)
        self.labelpurple.move(40, 270)

        self.labelottenokpurple = QLabel(self)
        self.labelottenokpurple.setText(ottenokpurples)
        self.labelottenokpurple.move(40, 300)

        self.labelgray = QLabel(self)
        self.labelgray.setText(grays)
        self.labelgray.move(40, 330)

        self.labelottenokgray = QLabel(self)
        self.labelottenokgray.setText(ottenokgrays)
        self.labelottenokgray.move(40, 360)

        self.labelcvetligreens = QLabel(self)
        self.labelcvetligreens.setText(whites)
        self.labelcvetligreens.move(40, 390)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())