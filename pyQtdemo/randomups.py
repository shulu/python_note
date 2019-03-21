#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys,random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from randomup import *


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def randup_click(self):
        try:
            self.username.clear()
            self.pwd.clear()
            uname = self.randuser()
            upwd = self.randpwd()
            self.username.setText(str(uname))
            self.pwd.setText(str(upwd))
        except:
            self.username.clear()
            self.pwd.clear()
            self.slotCritical()
            return False

    @staticmethod
    def randuser():
        special_str = '!@#$%^&*()_+=-><:}{?/'
        normal_str = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        userName = ''.join(random.sample(normal_str, 8))
        return userName

    @staticmethod
    def randpwd():
        normal_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        userPassword = ''.join(random.sample(normal_str, 6))
        return userPassword

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.randomup.clicked.connect(myWin.randup_click)
    myWin.show()
    sys.exit(app.exec_())