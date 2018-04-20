#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 200))
        # self.Move((0,0))
        # self.Maximize()
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    # frame = wx.Frame(None, -1, 'simple.py', style=wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)
    # frame.Show()
    Example(None, title='move')
    app.MainLoop()