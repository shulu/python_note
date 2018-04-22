#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show StatusBar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show Toolbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, 'Quit')
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.OnClose, qmi)

        menuBar.Append(fileMenu, '&File')
        menuBar.Append(viewMenu, '&view')
        self.SetMenuBar(menuBar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, '', wx.Bitmap('./icon/exit.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((350, 250))
        self.SetTitle('Check menu item')
        self.Center()
        self.Show()

    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def OnClose(self, e):
        self.Close()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()