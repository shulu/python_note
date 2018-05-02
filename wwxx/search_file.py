#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import wx

class searchFile(wx.Frame):
    
    def __init__(self, parent, title):
        
        super(searchFile, self).__init__(parent, title='', size=(600, 300))

        self.InitUI()
        self.Center()
        self.Show()


    def InitUI(self):

        panel = wx.Panel(self)

        main_sizer = wx.GridBagSizer(2,1)

        left_sizer = wx.GridBagSizer(3, 5)
        right_sizer = wx.GridBagSizer(3, 5)

        st1 = wx.StaticText(panel, label='请选择文件')
        left_sizer.Add(st1, pos=(0,0), span=(0,3), flag=wx.ALIGN_LEFT|wx.BOTTOM|wx.EXPAND, border=15)

        st2 = wx.StaticText(panel, label='请选择水印')
        right_sizer.Add(st2, pos=(0,2), span=(0,3), flag=wx.ALIGN_RIGHT|wx.BOTTOM|wx.EXPAND, border=15)

        stl1 = wx.StaticLine(panel)
        left_sizer.Add(stl1, pos=(1,0), span=(0,3), flag=wx.EXPAND, border=15)

        stl2 = wx.StaticLine(panel)
        right_sizer.Add(stl2, pos=(1,0), span=(0,3), flag=wx.EXPAND, border=15)

        st3 = wx.StaticText(panel, label='搜索')
        left_sizer.Add(st3, pos=(2,0), flag=wx.LEFT|wx.ALIGN_CENTER, border=10)

        tc1 = wx.TextCtrl(panel)
        left_sizer.Add(tc1, pos=(2,1), flag=wx.LEFT|wx.RIGHT|wx.EXPAND)

        btn1 = wx.Button(panel, label='Browser...')
        left_sizer.Add(btn1, pos=(2,2), flag=wx.RIGHT, border=10)

        st4 = wx.StaticText(panel, label='搜索')
        right_sizer.Add(st4, pos=(2,0), flag=wx.LEFT|wx.ALIGN_CENTER, border=10)

        tc2 = wx.TextCtrl(panel)
        right_sizer.Add(tc2, pos=(2,1), flag=wx.LEFT|wx.RIGHT|wx.EXPAND)

        btn2 = wx.Button(panel, label='Browser...')
        right_sizer.Add(btn2, pos=(2,2), flag=wx.RIGHT, border=10)

        stl3 = wx.StaticLine(panel)
        left_sizer.Add(stl3, pos=(3, 0), span=(0, 3), flag=wx.EXPAND, border=15)

        stl4 = wx.StaticLine(panel)
        right_sizer.Add(stl4, pos=(3, 0), span=(0, 3), flag=wx.EXPAND, border=15)

        sb1 = wx.StaticBox(panel, label='Optional Attributes')

        boxsizer = wx.StaticBoxSizer(sb1, wx.VERTICAL)

        boxsizer.Add(wx.CheckBox(panel, label='Public'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Default Constructor'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Main Method'), flag=wx.LEFT, border=5)
        left_sizer.Add(boxsizer, pos=(4, 0), span=(1, 4), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        sb2 = wx.StaticBox(panel, label='Optional Attributes')

        boxsizer = wx.StaticBoxSizer(sb2, wx.VERTICAL)

        boxsizer.Add(wx.CheckBox(panel, label='Public'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Default Constructor'), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label='Generate Main Method'), flag=wx.LEFT, border=5)
        right_sizer.Add(boxsizer, pos=(4, 0), span=(1, 4), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        main_sizer.Add(left_sizer, pos=(0, 0), flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=20)
        main_sizer.Add(right_sizer, pos=(0, 2), flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=20)

        panel.SetSizerAndFit(main_sizer)


if __name__ == '__main__':
    app = wx.App()
    searchFile(None, title='')
    app.MainLoop()