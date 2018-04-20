#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

APP_EXIT = 1

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&QuittCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)
        self.SetSize((300, 200))
        self.SetTitle('Icons and shortcuts')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()