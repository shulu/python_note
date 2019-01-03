#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from calculated import *

class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def btone_click( self ):
        self.lineEdit.insert('1')

    def bttwo_click ( self ):
        self.lineEdit.insert('2')

    def btthree_click ( self ):
        self.lineEdit.insert('3')

    def btfour_click ( self ):
        self.lineEdit.insert('4')

    def btfive_click ( self ):
        self.lineEdit.insert('5')

    def btsix_click ( self ):
        self.lineEdit.insert('6')

    def btseven_click ( self ):
        self.lineEdit.insert('7')

    def bteight_click ( self ):
        self.lineEdit.insert('8')

    def btnine_click ( self ):
        self.lineEdit.insert('9')

    def btzero_click ( self ):
        self.lineEdit.insert('0')

    def plus_click ( self ):
        self.lineEdit.insert('+')

    def sub_click ( self ):
        self.lineEdit.insert('-')

    def mul_click ( self ):
        self.lineEdit.insert('*')

    def div_click ( self ):
        self.lineEdit.insert('/')

    def equal_click ( self ):
        s = self.lineEdit.text()
        if len(s) > 0:
            try:
                ans = eval(s)
                self.lineEdit.clear()
                self.lineEdit.setText(str(ans))
            except:
                self.lineEdit.clear()
                self.slotCritical()
                return False

    def clear_click ( self ):
        self.lineEdit.clear()

    def slotCritical(self):
        QMessageBox.critical(self, "Critical",
                             self.tr("请输入正确的表达式!"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.num_0.clicked.connect(myWin.btzero_click)
    myWin.num_1.clicked.connect(myWin.btone_click)
    myWin.num_2.clicked.connect(myWin.bttwo_click)
    myWin.num_3.clicked.connect(myWin.btthree_click)
    myWin.num_4.clicked.connect(myWin.btfour_click)
    myWin.num_5.clicked.connect(myWin.btfive_click)
    myWin.num_6.clicked.connect(myWin.btsix_click)
    myWin.num_7.clicked.connect(myWin.btseven_click)
    myWin.num_8.clicked.connect(myWin.bteight_click)
    myWin.num_9.clicked.connect(myWin.btnine_click)
    myWin.op_plus.clicked.connect(myWin.plus_click)
    myWin.op_sub.clicked.connect(myWin.sub_click)
    myWin.op_mul.clicked.connect(myWin.mul_click)
    myWin.op_div.clicked.connect(myWin.div_click)
    myWin.op_equal.clicked.connect(myWin.equal_click)
    myWin.CE.clicked.connect(myWin.clear_click)
    myWin.show()
    sys.exit(app.exec_())