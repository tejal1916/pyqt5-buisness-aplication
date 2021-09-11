import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.dashboard as dash

class CompoundInt(QWidget):

    def __init__(self):
        super().__init__()
        self.CompoundIntmethod()

    def CompoundIntmethod(self):
        self.setWindowTitle("Compound Interest Calculation")
        self.setGeometry(500, 200, 600, 600)
        self.img()
        self.CompoundIntform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("bg.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,500)

    def CompoundIntform(self):
        global box_principal, box_year, box_rate

        main.MyLabel(self,"Compound Interest Cal",70,50,600,100)

        main.MyLabel2(self, "Principal :", 100, 150, 200, 100)
        box_principal = main.Lineedit(self, 270, 180, 200, 30)

        main.MyLabel2(self, "Year :", 150, 200, 200, 100)
        box_year = main.Lineedit(self, 270, 230, 200, 30)

        main.MyLabel2(self, "Rate% :", 129, 250, 200, 100)
        box_rate = main.Spinbox(self, 270, 280, 200, 30)

        main.Mybutton(self, "Back", 200, 350, 100, 50, self.dash)
        main.Mybutton(self, "Compound Interest",320,350,210,50,self.Compound)


        global  mylabel
        mylabel=main.MyLabel3(self, "" , 20, 400, 600, 100)


        self.show()

    def Compound(self):
        principal = int(box_principal.text())
        print(principal)
        year = int(box_year.text())
        print(year)
        rate = int(box_rate.value())
        print(rate)

        total = (principal*(1+(rate/100))**year)
        mylabel.setText("Compound Interest: "+str(total))

    def dash(self):
            self.gotoMain()

    @pyqtSlot()
    def gotoMain(self):
        self.next = dash.Dashboard()
        self.next.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = CompoundInt()
    w.show()
    exit(app.exec_())