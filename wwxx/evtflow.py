#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class MyPanel(wx.Panel):

    def __init__(self, *args, **kw):

        super(MyPanel, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        print('event reached panel class')
        e.Skip()

class MyButton(wx.Button):

    def __init__(self, *args, **kw):

        super(MyButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, e):

        print('event reached button class')
        e.Skip()


class Example(wx.Frame):

    def __init__(self, *args, **kw):

        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        mpnl = MyPanel(self)

        MyButton(mpnl, label='Ok', pos=(15,15))

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.SetTitle('Propagate event')
        self.Center()
        self.Show(True)

    def OnButtonClicked(self, e):

        print('event reachec frame class')
        e.Skip()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()

