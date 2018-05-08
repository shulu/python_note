#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.SetTitle('Event veto')
        self.Center()
        self.Show(True)


    def OnCloseWindow(self, e):

        dial = wx.MessageDialog(None, 'Are You sure to quit?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
            # self.Close() dead loop
        else:
            e.Veto()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()