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
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
        # 子菜单
        fileMenu.Append(wx.ID_ANY, 'Import', imp)
        # 手动菜单
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&QuittCtrl+w')
        fileMenu.Append(qmi)
        # 给菜单绑定事件
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        # 绑定菜单到菜单栏
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)

        self.SetSize((350, 350))
        self.SetTitle('Submenu')
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