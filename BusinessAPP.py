import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.dashboard as dash


class BusinessAPP(QWidget):

    def __init__(self):
        super().__init__()
        self.BusinessAPPmethod()

    def BusinessAPPmethod(self):
        self.setWindowTitle("PYQT5 Business Application")
        self.setGeometry(800, 200, 600, 600)
        self.img()
        self.BusinessAPPform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("image/BGI.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,500)

    def BusinessAPPform(self):
        global box_amount, box_rate

        main.MyLabel4(self, "PYQT5", 230, 50, 600, 100)
        main.MyLabel4(self,"Business Application ",100,100,600,100)

        main.MyLabel6(self, "Group Members", 200, 200, 450, 100)
        main.MyLabel5(self, "Tejal Panmand", 330, 250, 450, 100)
        main.MyLabel5(self, "Vaishnavi Ghodake", 330, 300, 450, 100)

        main.Mybutton(self, "-", 480, 300, 10, 10, self.dash)

        self.show()


    def dash(self):
            self.gotoMain()

    @pyqtSlot()
    def gotoMain(self):
        self.next = dash.Dashboard()
        self.next.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = BusinessAPP()
    w.show()
    exit(app.exec_())