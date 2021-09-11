import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.dashboard as dash

class DiscountCal(QWidget):

    def __init__(self):
        super().__init__()
        self.DiscountCalmethod()

    def DiscountCalmethod(self):
        self.setWindowTitle("Discount Calculation")
        self.setGeometry(500, 200, 600, 600)
        self.img()
        self.DiscountCalform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("bg.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,500)

    def DiscountCalform(self):
        global box_amount, box_rate

        main.MyLabel(self,"Discount Calculation",100,50,450,100)

        main.MyLabel2(self,"Amount :",110,150,200,100)
        box_amount = main.Lineedit(self,270,180,200,30)

        main.MyLabel2(self, "Rate% :", 130, 190, 200, 100)
        box_rate = main.Spinbox(self, 270, 230, 200, 30)

        main.Mybutton(self, "Back", 200, 300, 100, 50, self.dash)
        main.Mybutton(self, "Discount Cal",350,300,150,50,self.DiscountCal)


        global  mylabel
        mylabel=main.MyLabel3(self, "" , 35, 400, 600, 100)


        self.show()

    def DiscountCal(self):
        amount = int(box_amount.text())
        print(amount)
        rate = int(box_rate.value())
        print(rate)
        total = amount - ((rate / 100) * amount)
        mylabel.setText("Discount Calculated value: "+str(total))

    def dash(self):
            self.gotoMain()

    @pyqtSlot()
    def gotoMain(self):
        self.next = dash.Dashboard()
        self.next.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = DiscountCal()
    w.show()
    exit(app.exec_())