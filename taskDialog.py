#Boa:Dialog:TaskDialog

# This file is part of PyCron.
#
# PyCron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import wx
import hourWizardDialog
import weekdayWizardDialog
import monthWizardDialog
import minuteWizardDialog
import dayWizardDialog

import pycron

def create(parent):
    return TaskDialog(parent)

[wxID_TASKDIALOG, wxID_TASKDIALOGBROWSEBUTTON, wxID_TASKDIALOGCANCELBUTTON,
 wxID_TASKDIALOGCOMMANDTEXTCTRL, wxID_TASKDIALOGDAYTEXTCTRL,
 wxID_TASKDIALOGDAYWIZARDBUTTON, wxID_TASKDIALOGDOWTEXTCTRL,
 wxID_TASKDIALOGDOWWIZARDBUTTON, wxID_TASKDIALOGHOURTEXTCTRL,
 wxID_TASKDIALOGHOURWIZARDBUTTON, wxID_TASKDIALOGMINUTETEXTCTRL,
 wxID_TASKDIALOGMINUTEWIZARDBUTTON, wxID_TASKDIALOGMONTHTEXTCTRL,
 wxID_TASKDIALOGMONTHWIZARDBUTTON, wxID_TASKDIALOGOKBUTTON,
 wxID_TASKDIALOGPARAMETERSTEXTCTRL, wxID_TASKDIALOGSTATICBOX1,
 wxID_TASKDIALOGSTATICBOX2, wxID_TASKDIALOGSTATICTEXT1,
 wxID_TASKDIALOGSTATICTEXT2, wxID_TASKDIALOGSTATICTEXT3,
 wxID_TASKDIALOGSTATICTEXT4, wxID_TASKDIALOGSTATICTEXT5,
 wxID_TASKDIALOGSTATICTEXT6, wxID_TASKDIALOGSTATICTEXT7,
 wxID_TASKDIALOGTESTEXECBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(26))

class TaskDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_TASKDIALOG, name=u'TaskDialog',
              parent=prnt, pos=wx.Point(45, 78), size=wx.Size(431, 398),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Task Properties')
        self.SetClientSize(wx.Size(423, 371))

        self.staticBox1 = wx.StaticBox(id=wxID_TASKDIALOGSTATICBOX1,
              label=u'Task', name='staticBox1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(408, 120), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_TASKDIALOGSTATICBOX2,
              label=u'Schedule', name='staticBox2', parent=self, pos=wx.Point(8,
              136), size=wx.Size(408, 184), style=0)

        self.staticText1 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT1,
              label=u'Command', name='staticText1', parent=self, pos=wx.Point(24,
              32), size=wx.Size(47, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT2,
              label=u'Parameters', name='staticText2', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(53, 13), style=0)

        self.CommandTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGCOMMANDTEXTCTRL,
              name=u'CommandTextCtrl', parent=self, pos=wx.Point(104, 29),
              size=wx.Size(232, 21), style=0, value=u'')

        self.browseButton = wx.Button(id=wxID_TASKDIALOGBROWSEBUTTON,
              label=u'Browse...', name=u'browseButton', parent=self,
              pos=wx.Point(344, 28), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.browseButton, wxID_TASKDIALOGBROWSEBUTTON,
              self.OnBrowsebuttonButton)

        self.ParametersTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGPARAMETERSTEXTCTRL,
              name=u'ParametersTextCtrl', parent=self, pos=wx.Point(104, 61),
              size=wx.Size(232, 21), style=0, value=u'')

        self.testExecButton = wx.Button(id=wxID_TASKDIALOGTESTEXECBUTTON,
              label=u'Test execution', name=u'testExecButton', parent=self,
              pos=wx.Point(169, 94), size=wx.Size(88, 23), style=0)
        wx.EVT_BUTTON(self.testExecButton, wxID_TASKDIALOGTESTEXECBUTTON,
              self.OnTestexecbuttonButton)

        self.staticText3 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT3,
              label=u'Minute', name='staticText3', parent=self, pos=wx.Point(32,
              160), size=wx.Size(32, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT4,
              label=u'Hour', name='staticText4', parent=self, pos=wx.Point(32,
              192), size=wx.Size(23, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT5,
              label=u'Day of Month', name='staticText5', parent=self,
              pos=wx.Point(32, 224), size=wx.Size(64, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT6,
              label=u'Month', name='staticText6', parent=self, pos=wx.Point(32,
              256), size=wx.Size(30, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_TASKDIALOGSTATICTEXT7,
              label=u'Week Day', name='staticText7', parent=self,
              pos=wx.Point(32, 288), size=wx.Size(51, 13), style=0)

        self.minuteTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGMINUTETEXTCTRL,
              name=u'minuteTextCtrl', parent=self, pos=wx.Point(104, 157),
              size=wx.Size(232, 21), style=0, value=u'')

        self.minuteWizardButton = wx.Button(id=wxID_TASKDIALOGMINUTEWIZARDBUTTON,
              label=u'Wizard...', name=u'minuteWizardButton', parent=self,
              pos=wx.Point(344, 156), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.minuteWizardButton, wxID_TASKDIALOGMINUTEWIZARDBUTTON,
              self.OnMinutewizardbuttonButton)

        self.hourTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGHOURTEXTCTRL,
              name=u'hourTextCtrl', parent=self, pos=wx.Point(104, 189),
              size=wx.Size(232, 21), style=0, value=u'')

        self.hourWizardButton = wx.Button(id=wxID_TASKDIALOGHOURWIZARDBUTTON,
              label=u'Wizard...', name=u'hourWizardButton', parent=self,
              pos=wx.Point(344, 188), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.hourWizardButton, wxID_TASKDIALOGHOURWIZARDBUTTON,
              self.OnHourwizardbuttonButton)

        self.dayTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGDAYTEXTCTRL,
              name=u'dayTextCtrl', parent=self, pos=wx.Point(104, 221),
              size=wx.Size(232, 21), style=0, value=u'')

        self.dayWizardButton = wx.Button(id=wxID_TASKDIALOGDAYWIZARDBUTTON,
              label=u'Wizard...', name=u'dayWizardButton', parent=self,
              pos=wx.Point(344, 220), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.dayWizardButton, wxID_TASKDIALOGDAYWIZARDBUTTON,
              self.OnDaywizardbuttonButton)

        self.monthTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGMONTHTEXTCTRL,
              name=u'monthTextCtrl', parent=self, pos=wx.Point(104, 253),
              size=wx.Size(232, 21), style=0, value=u'')

        self.monthWizardButton = wx.Button(id=wxID_TASKDIALOGMONTHWIZARDBUTTON,
              label=u'Wizard...', name=u'monthWizardButton', parent=self,
              pos=wx.Point(344, 252), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.monthWizardButton, wxID_TASKDIALOGMONTHWIZARDBUTTON,
              self.OnMonthwizardbuttonButton)

        self.dowTextCtrl = wx.TextCtrl(id=wxID_TASKDIALOGDOWTEXTCTRL,
              name=u'dowTextCtrl', parent=self, pos=wx.Point(104, 285),
              size=wx.Size(232, 21), style=0, value=u'')

        self.dowWizardButton = wx.Button(id=wxID_TASKDIALOGDOWWIZARDBUTTON,
              label=u'Wizard...', name=u'dowWizardButton', parent=self,
              pos=wx.Point(344, 284), size=wx.Size(56, 23), style=0)
        wx.EVT_BUTTON(self.dowWizardButton, wxID_TASKDIALOGDOWWIZARDBUTTON,
              self.OnDowwizardbuttonButton)

        self.OKButton = wx.Button(id=wxID_TASKDIALOGOKBUTTON, label=u'&OK',
              name=u'OKButton', parent=self, pos=wx.Point(120, 336),
              size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.OKButton, wxID_TASKDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_TASKDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(232, 336), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_TASKDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.crontab = parent.crontab
        self.itemKey = int(parent.cronItemList.GetItemText(parent.currentItem))
        self.minute, self.hour, self.day, self.month, self.dow, self.command, self.parameters  = self.crontab.getItem(self.itemKey)
        self.minuteTextCtrl.SetValue(self.minute)
        self.hourTextCtrl.SetValue(self.hour)
        self.dayTextCtrl.SetValue(self.day)
        self.monthTextCtrl.SetValue(self.month)
        self.dowTextCtrl.SetValue(self.dow)
        self.CommandTextCtrl.SetValue(self.command)
        self.ParametersTextCtrl.SetValue(self.parameters)

    def OnBrowsebuttonButton(self, event):
        dlg = wx.FileDialog(self, "Choose an executable or a python script",
            ".", "",
            "Executable files (*.exe,*.com,*.cmd,*.bat)|*.exe;*.com;*.cmd;*.bat|Python modules (*.py)|*.py|All files (*.*)|*.*",
            wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                self.CommandTextCtrl.SetValue(filename)
        finally:
            dlg.Destroy()

    def OnHourwizardbuttonButton(self, event):
        dlg = hourWizardDialog.HourWizardDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.hourTextCtrl.SetValue(self.hour)
        finally:
            dlg.Destroy()

    def OnDaywizardbuttonButton(self, event):
        dlg = dayWizardDialog.DayWizardDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.dayTextCtrl.SetValue(self.day)
        finally:
            dlg.Destroy()

    def OnMonthwizardbuttonButton(self, event):
        dlg = monthWizardDialog.MonthWizardDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.monthTextCtrl.SetValue(self.month)
        finally:
            dlg.Destroy()

    def OnDowwizardbuttonButton(self, event):
        dlg = weekdayWizardDialog.WeekdayWizardDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.dowTextCtrl.SetValue(self.dow)
        finally:
            dlg.Destroy()

    def OnMinutewizardbuttonButton(self, event):
        dlg = minuteWizardDialog.MinuteWizardDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.minuteTextCtrl.SetValue(self.minute)
        finally:
            dlg.Destroy()

    def OnOkbuttonButton(self, event):
        self.minute = self.minuteTextCtrl.GetValue()
        self.hour = self.hourTextCtrl.GetValue()
        self.day = self.dayTextCtrl.GetValue()
        self.month = self.monthTextCtrl.GetValue()
        self.dow = self.dowTextCtrl.GetValue()
        self.command = self.CommandTextCtrl.GetValue()
        self.parameters = self.ParametersTextCtrl.GetValue()
        self.crontab.changeItem(self.itemKey, self.minute, self.hour, self.day,
                                self.month, self.dow, self.command, self.parameters)
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnTestexecbuttonButton(self, event):
        job = pycron.Job(self.CommandTextCtrl.GetValue(), [self.ParametersTextCtrl.GetValue()], missed=False)
        job.start()
        job.join(30.0) #wait for max. 30 seconds
        msg = ""
        if job.result == 0:
            msg = "Execution was successful."
        else:
            msg = "Execution return code = %s" % job.result
        dlg = wx.MessageDialog(self, msg, "Execution", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

