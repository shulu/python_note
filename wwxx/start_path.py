#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class startPath(wx.Frame):

    def __init__(self, parent, title):
        super(startPath, self).__init__(parent, title=title, size=(450, 250))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5,5)

        st0 = wx.StaticText(panel, label='请配置文件路径')
        sizer.Add(st0, pos=(0,2), span=(0,4), flag=wx.EXPAND|wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM, border=15)

        stl1 = wx.StaticLine(panel)
        sizer.Add(stl1, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.BOTTOM)

        st1 = wx.StaticText(panel, label='请选择文件路径：')
        sizer.Add(st1, pos=(2,0), flag=wx.TOP|wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2,1), span=(1,3), flag=wx.TOP|wx.EXPAND, border=5)

        btn1 = wx.Button(panel, label='Browser...')
        sizer.Add(btn1, pos=(2,4), flag=wx.TOP|wx.RIGHT, border=5)

        st2 = wx.StaticText(panel, label='请选择水印路径：')
        sizer.Add(st2, pos=(3,0), flag=wx.TOP|wx.LEFT, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3,1), span=(1,3), flag=wx.TOP|wx.EXPAND, border=5)

        btn2 = wx.Button(panel, label='Browser...')
        sizer.Add(btn2, pos=(3,4), flag=wx.TOP|wx.RIGHT, border=5)

        st3 = wx.StaticText(panel, label='请选择保存路径：')
        sizer.Add(st3, pos=(4,0), flag=wx.TOP|wx.LEFT, border=10)

        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(4,1), span=(1,3), flag=wx.TOP|wx.EXPAND, border=5)

        btn3 = wx.Button(panel, label='Browser...')
        sizer.Add(btn3, pos=(4,4), flag=wx.TOP|wx.RIGHT, border=5)

        btn4 = wx.Button(panel, label='Ok')
        sizer.Add(btn4, pos=(5,1))

        btn5 = wx.Button(panel, label='later')
        sizer.Add(btn5, pos=(5,3), flag=wx.BOTTOM, border=15)

        sizer.AddGrowableCol(2)
        panel.SetSizerAndFit(sizer)

if __name__ == '__main__':
    app = wx.App()
    startPath(None, title='')
    app.MainLoop()
