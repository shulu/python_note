#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class Example(wx.Frame):

    def __init__(self, paren, title):

        super(Example, self).__init__(paren, title=title, size=(300, 250))

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        hbox = wx.BoxSizer()

        fgs = wx.FlexGridSizer(3,2,9,25)

        title = wx.StaticText(panel, label='Title')
        author = wx.StaticText(panel, label='Author')
        review = wx.StaticText(panel, label='Review')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel)

        fgs.AddMany([
            (title),
            (tc1, 1, wx.EXPAND),
            (author),
            (tc2, 1, wx.EXPAND),
            (review, 1, wx.EXPAND),
            (tc3, 1, wx.EXPAND)
        ])
        # param1 从0开始 标记那些行 param2 proportion 是否可增长
        fgs.AddGrowableRow(2, 1)

        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Review')
    app.MainLoop()