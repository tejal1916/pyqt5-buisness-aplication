import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

import calculation.Main as main
import calculation.TaxCal as tax
import calculation.DiscountCal as dis
import calculation.SimpleInt as simple
import calculation.CompoundInt as compound
import calculation.LoanPayment as loan
import calculation.Annualper as annual

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()
        self.Dashboardmethod()

    def Dashboardmethod(self):
        self.setWindowTitle("Dashboard")
        self.setGeometry(500, 200, 600, 400)
        self.img()
        self.Dashboardform()

    def img(self):
        self.label2 = QLabel(self)
        img1 = QPixmap("bg.jpg")
        self.label2.setPixmap(img1)
        self.resize(600,400)

    def Dashboardform(self):
        main.MyLabel(self, "DASHBOARD", 200, 0, 1200, 100)

        main.Mybutton(self, "Tax Cal",100,100,170,50,self.Tax)
        main.Mybutton(self, "Discount Cal", 350,100,200,50,self.Discount)
        main.Mybutton(self, "Simple Interest", 100, 200, 170, 50, self.SimpleInterest)
        main.Mybutton(self, "Compound Interest", 350, 200, 210, 50, self.CompoundInterest)
        main.Mybutton(self, "Loan Payment", 100, 300, 170, 50, self.LoanPay)
        main.Mybutton(self, "Annual % yield ", 350, 300, 210, 50, self.AnnualPer)

    def Tax(self):
            self.gototaxcal()
    @pyqtSlot()
    def gototaxcal(self):
        self.next = tax.TaxCal()
        self.next.show()
        self.close()



    def Discount(self):
            self.gotodiscountcal()
    @pyqtSlot()
    def gotodiscountcal(self):
        self.next = dis.DiscountCal()
        self.next.show()
        self.close()


    def SimpleInterest(self):
            self.gotosimpleint()
    @pyqtSlot()
    def gotosimpleint(self):
        self.next = simple.SimpleInt()
        self.next.show()
        self.close()


    def CompoundInterest(self):
            self.gotocompoundint()
    @pyqtSlot()
    def gotocompoundint(self):
        self.next = compound.CompoundInt()
        self.next.show()
        self.close()


    def LoanPay(self):
            self.gotoLoan()
    @pyqtSlot()
    def gotoLoan(self):
        self.next = loan.LoanPayment()
        self.next.show()
        self.close()


    def AnnualPer(self):
            self.gotoannualper()
    @pyqtSlot()
    def gotoannualper(self):
        self.next = annual.Annualper()
        self.next.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w = Dashboard()
    w.show()
    exit(app.exec_())