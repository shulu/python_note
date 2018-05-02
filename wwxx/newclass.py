#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,size=(450, 350))

        self.InitUI()
        self.Centre()
        self.Show()


    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5,5)

        st1 = wx.StaticText(panel, label='Java Class')
        sizer.Add(st1, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)
        # 8bit
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('./icon/exec.png'))
        sizer.Add(icon, pos=(0,4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT, border=5)
        # line
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.BOTTOM, border=10)
        # textctrl
        st2 = wx.StaticText(panel, label='Name')
        sizer.Add(st2, pos=(2,0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2,1), span=(1,3), flag=wx.EXPAND|wx.TOP)

        st3 = wx.StaticText(panel, label='Package')
        sizer.Add(st3, pos=(3,0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3,1), span=(1, 3), flag=wx.EXPAND|wx.TOP, border=5)

        btn_browser1 = wx.Button(panel, label='Browser...')
        sizer.Add(btn_browser1, pos=(3,4), flag=wx.TOP|wx.RIGHT, border=5)

        st4 = wx.StaticText(panel, label='Extends')
        sizer.Add(st4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4,1), span=(1,3), flag=wx.TOP|wx.EXPAND, border=5)

        btn_browser2 = wx.Button(panel, label='Browser...')
        sizer.Add(btn_browser2, pos=(4, 4), flag=wx.EXPAND | wx.RIGHT, border=5)

        sb = wx.StaticBox(panel, label='Optional Attributes')

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        boxsizer.Add(wx.CheckBox(panel, label='Public'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Default Constructor'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Main Method'), flag=wx.LEFT, border=5)
        sizer.Add(boxsizer, pos=(5,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        btn3 = wx.Button(panel, label='Help')
        sizer.Add(btn3, pos=(7,0), flag=wx.LEFT, border=10)

        btn4 = wx.Button(panel, label='Ok')
        sizer.Add(btn4, pos=(7,3))

        btn5 = wx.Button(panel, label='Cancel')
        sizer.Add(btn5, pos=(7,4), span=(1,1), flag=wx.BOTTOM|wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)
        #sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Create java Class')
    app.MainLoop()