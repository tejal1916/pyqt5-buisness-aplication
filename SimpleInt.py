import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.dashboard as dash

class SimpleInt(QWidget):

    def __init__(self):
        super().__init__()
        self.SimpleIntmethod()

    def SimpleIntmethod(self):
        self.setWindowTitle("Discount Calculation")
        self.setGeometry(500, 200, 600, 600)
        self.img()
        self.SimpleIntform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("bg.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,500)

    def SimpleIntform(self):
        global box_principal, box_time, box_rate

        main.MyLabel(self,"Simple Interest Calculation",30,50,600,100)

        main.MyLabel2(self,"Principal :",100,150,200,100)
        box_principal = main.Lineedit(self,270,180,200,30)

        main.MyLabel2(self, "Time :", 150, 200, 200, 100)
        box_time = main.Lineedit(self, 270, 230, 200, 30)

        main.MyLabel2(self, "Rate% :", 129, 250, 200, 100)
        box_rate = main.Spinbox(self, 270, 280, 200, 30)

        main.Mybutton(self, "Back", 200, 350, 100, 50, self.dash)
        main.Mybutton(self, "Simple Interest",350,350,170,50,self.Simple)


        global  mylabel
        mylabel=main.MyLabel3(self, "" , 35, 400, 600, 100)


        self.show()

    def Simple(self):
        principal = int(box_principal.text())
        print(principal)
        time = int(box_time.text())
        print(time)
        rate = int(box_rate.value())
        print(rate)
        total = (principal*rate*time/100)
        mylabel.setText("Simple Interest : "+str(total))

    def dash(self):
            self.gotoMain()

    @pyqtSlot()
    def gotoMain(self):
        self.next = dash.Dashboard()
        self.next.show()
        self.close()
if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = SimpleInt()
    w.show()
    exit(app.exec_())