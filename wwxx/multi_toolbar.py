#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('./icon/new.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('./icon/open.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('./icon/save.png'))
        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self)
        qtool = toolbar2.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('./icon/exit.png'))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSizer(vbox)

        self.SetSize((250, 200))
        self.SetTitle('toolbars')
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