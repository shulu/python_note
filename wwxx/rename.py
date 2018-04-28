#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,size=(320, 130))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4,4)

        text = wx.StaticText(panel, label='Rename To')
        sizer.Add(text, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        btnOk = wx.Button(panel, label='Ok', size=(90,28))
        btnClose = wx.Button(panel, label='Close', size=(90,28))
        sizer.Add(btnOk, pos=(3,3))
        sizer.Add(btnClose, pos=(3,4), flag=wx.RIGHT|wx.BOTTOM, border=5)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Rename')
    app.MainLoop()