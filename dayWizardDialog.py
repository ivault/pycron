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

import pycron
import tools

def create(parent):
    return DayWizardDialog(parent)

[wxID_DAYWIZARDDIALOG, wxID_DAYWIZARDDIALOGCANCELBUTTON,
 wxID_DAYWIZARDDIALOGDAY10CHECKBOX, wxID_DAYWIZARDDIALOGDAY11CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY12CHECKBOX, wxID_DAYWIZARDDIALOGDAY13CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY14CHECKBOX, wxID_DAYWIZARDDIALOGDAY15CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY16CHECKBOX, wxID_DAYWIZARDDIALOGDAY17CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY18CHECKBOX, wxID_DAYWIZARDDIALOGDAY19CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY1CHECKBOX, wxID_DAYWIZARDDIALOGDAY20CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY21CHECKBOX, wxID_DAYWIZARDDIALOGDAY22CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY23CHECKBOX, wxID_DAYWIZARDDIALOGDAY24CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY25CHECKBOX, wxID_DAYWIZARDDIALOGDAY26CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY27CHECKBOX, wxID_DAYWIZARDDIALOGDAY28CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY29CHECKBOX, wxID_DAYWIZARDDIALOGDAY2CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY30CHECKBOX, wxID_DAYWIZARDDIALOGDAY31CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY3CHECKBOX, wxID_DAYWIZARDDIALOGDAY4CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY5CHECKBOX, wxID_DAYWIZARDDIALOGDAY6CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY7CHECKBOX, wxID_DAYWIZARDDIALOGDAY8CHECKBOX,
 wxID_DAYWIZARDDIALOGDAY9CHECKBOX, wxID_DAYWIZARDDIALOGOKBUTTON,
 wxID_DAYWIZARDDIALOGSELECTALLBUTTON, wxID_DAYWIZARDDIALOGUNSELECTALLBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(36))

class DayWizardDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DAYWIZARDDIALOG,
              name=u'DayWizardDialog', parent=prnt, pos=wx.Point(20, 164),
              size=wx.Size(431, 262), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Scheduler Wizard: Day')
        self.SetClientSize(wx.Size(423, 235))

        self.day1CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY1CHECKBOX,
              label=u'1', name=u'day1CheckBox', parent=self, pos=wx.Point(16,
              24), size=wx.Size(40, 13), style=0)
        self.day1CheckBox.SetValue(False)

        self.day2CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY2CHECKBOX,
              label=u'2', name=u'day2CheckBox', parent=self, pos=wx.Point(56,
              24), size=wx.Size(40, 13), style=0)
        self.day2CheckBox.SetValue(False)

        self.day3CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY3CHECKBOX,
              label=u'3', name=u'day3CheckBox', parent=self, pos=wx.Point(96,
              24), size=wx.Size(40, 13), style=0)
        self.day3CheckBox.SetValue(False)

        self.day4CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY4CHECKBOX,
              label=u'4', name=u'day4CheckBox', parent=self, pos=wx.Point(136,
              24), size=wx.Size(40, 13), style=0)
        self.day4CheckBox.SetValue(False)

        self.day5CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY5CHECKBOX,
              label=u'5', name=u'day5CheckBox', parent=self, pos=wx.Point(176,
              24), size=wx.Size(40, 13), style=0)
        self.day5CheckBox.SetValue(False)

        self.day6CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY6CHECKBOX,
              label=u'6', name=u'day6CheckBox', parent=self, pos=wx.Point(216,
              24), size=wx.Size(40, 13), style=0)
        self.day6CheckBox.SetValue(False)

        self.day7CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY7CHECKBOX,
              label=u'7', name=u'day7CheckBox', parent=self, pos=wx.Point(256,
              24), size=wx.Size(40, 13), style=0)
        self.day7CheckBox.SetValue(False)

        self.day8CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY8CHECKBOX,
              label=u'8', name=u'day8CheckBox', parent=self, pos=wx.Point(296,
              24), size=wx.Size(40, 13), style=0)
        self.day8CheckBox.SetValue(False)

        self.day9CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY9CHECKBOX,
              label=u'9', name=u'day9CheckBox', parent=self, pos=wx.Point(336,
              24), size=wx.Size(40, 13), style=0)
        self.day9CheckBox.SetValue(False)

        self.day10CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY10CHECKBOX,
              label=u'10', name=u'day10CheckBox', parent=self, pos=wx.Point(376,
              24), size=wx.Size(40, 13), style=0)
        self.day10CheckBox.SetValue(False)

        self.day11CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY11CHECKBOX,
              label=u'11', name=u'day11CheckBox', parent=self, pos=wx.Point(16,
              56), size=wx.Size(40, 13), style=0)
        self.day11CheckBox.SetValue(False)

        self.day12CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY12CHECKBOX,
              label=u'12', name=u'day12CheckBox', parent=self, pos=wx.Point(56,
              56), size=wx.Size(40, 13), style=0)
        self.day12CheckBox.SetValue(False)

        self.day13CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY13CHECKBOX,
              label=u'13', name=u'day13CheckBox', parent=self, pos=wx.Point(96,
              56), size=wx.Size(40, 13), style=0)
        self.day13CheckBox.SetValue(False)

        self.day14CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY14CHECKBOX,
              label=u'14', name=u'day14CheckBox', parent=self, pos=wx.Point(136,
              56), size=wx.Size(40, 13), style=0)
        self.day14CheckBox.SetValue(False)

        self.day15CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY15CHECKBOX,
              label=u'15', name=u'day15CheckBox', parent=self, pos=wx.Point(176,
              56), size=wx.Size(40, 13), style=0)
        self.day15CheckBox.SetValue(False)

        self.day16CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY16CHECKBOX,
              label=u'16', name=u'day16CheckBox', parent=self, pos=wx.Point(216,
              56), size=wx.Size(40, 13), style=0)
        self.day16CheckBox.SetValue(False)

        self.day17CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY17CHECKBOX,
              label=u'17', name=u'day17CheckBox', parent=self, pos=wx.Point(256,
              56), size=wx.Size(40, 13), style=0)
        self.day17CheckBox.SetValue(False)

        self.day18CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY18CHECKBOX,
              label=u'18', name=u'day18CheckBox', parent=self, pos=wx.Point(296,
              56), size=wx.Size(40, 13), style=0)
        self.day18CheckBox.SetValue(False)

        self.day19CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY19CHECKBOX,
              label=u'19', name=u'day19CheckBox', parent=self, pos=wx.Point(336,
              56), size=wx.Size(40, 13), style=0)
        self.day19CheckBox.SetValue(False)

        self.day20CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY20CHECKBOX,
              label=u'20', name=u'day20CheckBox', parent=self, pos=wx.Point(376,
              56), size=wx.Size(40, 13), style=0)
        self.day20CheckBox.SetValue(False)

        self.day21CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY21CHECKBOX,
              label=u'21', name=u'day21CheckBox', parent=self, pos=wx.Point(16,
              88), size=wx.Size(40, 13), style=0)
        self.day21CheckBox.SetValue(False)

        self.day22CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY22CHECKBOX,
              label=u'22', name=u'day22CheckBox', parent=self, pos=wx.Point(56,
              88), size=wx.Size(40, 13), style=0)
        self.day22CheckBox.SetValue(False)

        self.day23CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY23CHECKBOX,
              label=u'23', name=u'day23CheckBox', parent=self, pos=wx.Point(96,
              88), size=wx.Size(40, 13), style=0)
        self.day23CheckBox.SetValue(False)

        self.day24CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY24CHECKBOX,
              label=u'24', name=u'day24CheckBox', parent=self, pos=wx.Point(136,
              88), size=wx.Size(40, 13), style=0)
        self.day24CheckBox.SetValue(False)

        self.day25CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY25CHECKBOX,
              label=u'25', name=u'day25CheckBox', parent=self, pos=wx.Point(176,
              88), size=wx.Size(40, 13), style=0)
        self.day25CheckBox.SetValue(False)

        self.day26CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY26CHECKBOX,
              label=u'26', name=u'day26CheckBox', parent=self, pos=wx.Point(216,
              88), size=wx.Size(40, 13), style=0)
        self.day26CheckBox.SetValue(False)

        self.day27CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY27CHECKBOX,
              label=u'27', name=u'day27CheckBox', parent=self, pos=wx.Point(256,
              88), size=wx.Size(40, 13), style=0)
        self.day27CheckBox.SetValue(False)

        self.day28CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY28CHECKBOX,
              label=u'28', name=u'day28CheckBox', parent=self, pos=wx.Point(296,
              88), size=wx.Size(40, 13), style=0)
        self.day28CheckBox.SetValue(False)

        self.day29CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY29CHECKBOX,
              label=u'29', name=u'day29CheckBox', parent=self, pos=wx.Point(336,
              88), size=wx.Size(40, 13), style=0)
        self.day29CheckBox.SetValue(False)

        self.day30CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY30CHECKBOX,
              label=u'30', name=u'day30CheckBox', parent=self, pos=wx.Point(376,
              88), size=wx.Size(40, 13), style=0)
        self.day30CheckBox.SetValue(False)

        self.day31CheckBox = wx.CheckBox(id=wxID_DAYWIZARDDIALOGDAY31CHECKBOX,
              label=u'31', name=u'day31CheckBox', parent=self, pos=wx.Point(16,
              120), size=wx.Size(40, 13), style=0)
        self.day31CheckBox.SetValue(False)

        self.selectAllButton = wx.Button(id=wxID_DAYWIZARDDIALOGSELECTALLBUTTON,
              label=u'&Select All', name=u'selectAllButton', parent=self,
              pos=wx.Point(16, 152), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.selectAllButton, wxID_DAYWIZARDDIALOGSELECTALLBUTTON,
              self.OnSelectallbuttonButton)

        self.unselectAllButton = wx.Button(id=wxID_DAYWIZARDDIALOGUNSELECTALLBUTTON,
              label=u'&Unselect All', name=u'unselectAllButton', parent=self,
              pos=wx.Point(104, 152), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.unselectAllButton,
              wxID_DAYWIZARDDIALOGUNSELECTALLBUTTON,
              self.OnUnselectallbuttonButton)

        self.OKButton = wx.Button(id=wxID_DAYWIZARDDIALOGOKBUTTON, label=u'&OK',
              name=u'OKButton', parent=self, pos=wx.Point(112, 200),
              size=wx.Size(75, 23), style=0)
        self.OKButton.SetDefault()
        wx.EVT_BUTTON(self.OKButton, wxID_DAYWIZARDDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_DAYWIZARDDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(240, 200), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_DAYWIZARDDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent
        self.dayControls = (self.day1CheckBox, self.day2CheckBox,
            self.day3CheckBox, self.day4CheckBox, self.day5CheckBox, self.day6CheckBox,
            self.day7CheckBox, self.day8CheckBox, self.day9CheckBox, self.day10CheckBox,
            self.day11CheckBox, self.day12CheckBox, self.day13CheckBox, self.day14CheckBox,
            self.day15CheckBox, self.day16CheckBox, self.day17CheckBox, self.day18CheckBox,
            self.day19CheckBox, self.day20CheckBox, self.day21CheckBox, self.day22CheckBox,
            self.day23CheckBox, self.day24CheckBox, self.day25CheckBox, self.day26CheckBox,
            self.day27CheckBox, self.day28CheckBox, self.day29CheckBox, self.day30CheckBox,
            self.day31CheckBox)
        for day in xrange(1, 32):
            try:
                m = pycron.Matcher(parent.dayTextCtrl.GetValue(), lineno = -1)
                m.minval = 1
                m.maxval = 31
                if m.matches(day, -1):
                    self.setDay(day, True)
            except pycron.InvalidLineException:
                pass

    def setDay(self, day, value):
        self.dayControls[day - 1].SetValue(value)

    def getDay(self, day):
        return self.dayControls[day - 1].GetValue()

    def setAllDays(self, value):
        for day in xrange(1, 32):
            self.setDay(day, value)

    def OnSelectallbuttonButton(self, event):
        self.setAllDays(True)

    def getDayStringFromValues(self, values):
        return tools.getValueStringFromValues(values, 1, 31)

    def OnOkbuttonButton(self, event):
        values = []
        for day in xrange(1, 32):
            values += [self.getDay(day)]
        self.parent.day = self.getDayStringFromValues(values)
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnUnselectallbuttonButton(self, event):
        self.setAllDays(False)
