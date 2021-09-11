
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def MyLabel(self,text,x,y,width,height):
    mylabel = QLabel(self)
    mylabel.setText(text)
    mylabel.setFont(QFont("times new roman",30))
    mylabel.setStyleSheet('color:cyan')
    mylabel.setGeometry(x,y,width,height)


def MyLabel2(self,text,x,y,width,height):
    mylabel2 = QLabel(self)
    mylabel2.setText(text)
    mylabel2.setFont(QFont("times new Roman",20))
    mylabel2.setStyleSheet('color:white')
    mylabel2.setGeometry(x,y,width,height)

def MyLabel3(self,text,x,y,width,height):
    mylabel3 = QLabel(self)
    mylabel3.setText(text)
    mylabel3.setFont(QFont("times new Roman",20))
    mylabel3.setStyleSheet('color:green')
    mylabel3.setGeometry(x,y,width,height)
    return mylabel3

def MyLabel4(self,text,x,y,width,height):
    mylabel4 = QLabel(self)
    mylabel4.setText(text)
    mylabel4.setFont(QFont("times new Roman",30))
    mylabel4.setStyleSheet('color:Black')
    mylabel4.setGeometry(x,y,width,height)

def MyLabel5(self,text,x,y,width,height):
    mylabel5 = QLabel(self)
    mylabel5.setText(text)
    mylabel5.setFont(QFont("times new Roman",15))
    mylabel5.setStyleSheet('color:Black')
    mylabel5.setGeometry(x,y,width,height)

def MyLabel6(self,text,x,y,width,height):
    mylabel6 = QLabel(self)
    mylabel6.setText(text)
    mylabel6.setFont(QFont("times new Roman",20))
    mylabel6.setStyleSheet('color:red')
    mylabel6.setGeometry(x,y,width,height)

def Myimage(self,image,x,y,width,height):
    myimage = QPixmap(image)
    label = QLabel(self)
    label.setScaledContents(True)
    label.setGeometry(x,y,width,height)
    label.setPixmap(myimage)

def Mybutton(self,text,x,y,width,height,myevent):
    button = QPushButton(self)
    button.setText(text)
    button.setGeometry(x,y,width,height)
    button.setStyleSheet('QPushButton {color:blue;}')
    button.setFont(QFont('Times', 15))
    button.clicked.connect(myevent)

def Lineedit(self,x,y,width,height):
    lineedit = QLineEdit(self)
    lineedit.setGeometry(x,y,width,height)
    lineedit.setFont(QFont('Time',12))
    return lineedit

def Spinbox(self,x,y,width,height):
    sb = QSpinBox(self)
    sb.setGeometry(x,y,width,height)
    sb.setFont(QFont('Time', 12))
    return sb