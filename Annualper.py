import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.dashboard as dash

class Annualper(QWidget):

    def __init__(self):
        super().__init__()
        self.Annualpermethod()

    def Annualpermethod(self):
        self.setWindowTitle("Annual Percentage yield")
        self.setGeometry(500, 200, 600, 600)
        self.img()
        self.Annualperform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("bg.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,500)

    def Annualperform(self):
        global  box_time, box_rate

        main.MyLabel(self,"Annual % Yield",150,50,600,100)

        main.MyLabel2(self, "Rate :", 150, 150, 200, 100)
        box_rate = main.Spinbox(self, 270, 180, 200, 30)

        main.MyLabel2(self, "Time :", 137, 200, 200, 100)
        box_time =  main.Lineedit(self, 270, 230, 200, 30)

        main.Mybutton(self, "Back", 200, 300, 100, 50, self.dash)
        main.Mybutton(self, "Annual %",320,300,210,50,self.annual)


        global  mylabel
        mylabel=main.MyLabel3(self, "" , 50, 400, 600, 100)


        self.show()

    def annual(self):
        time = int(box_time.text())
        print(time)
        rate = int(box_rate.value())
        print(rate)
        total = (1+(rate/time)**time)-1
        mylabel.setText("Annual % yield : "+str(total))

    def dash(self):
            self.gotoMain()

    @pyqtSlot()
    def gotoMain(self):
        self.next = dash.Dashboard()
        self.next.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = Annualper()
    w.show()
    exit(app.exec_())