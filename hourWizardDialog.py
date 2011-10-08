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
    return HourWizardDialog(parent)

[wxID_HOURWIZARDDIALOG, wxID_HOURWIZARDDIALOGCANCELBUTTON,
 wxID_HOURWIZARDDIALOGHOUR0CHECKBOX, wxID_HOURWIZARDDIALOGHOUR10CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR11CHECKBOX, wxID_HOURWIZARDDIALOGHOUR12CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR13CHECKBOX, wxID_HOURWIZARDDIALOGHOUR14CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR15CHECKBOX, wxID_HOURWIZARDDIALOGHOUR16CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR17CHECKBOX, wxID_HOURWIZARDDIALOGHOUR18CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR19CHECKBOX, wxID_HOURWIZARDDIALOGHOUR1CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR20CHECKBOX, wxID_HOURWIZARDDIALOGHOUR21CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR22CHECKBOX, wxID_HOURWIZARDDIALOGHOUR23CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR2CHECKBOX, wxID_HOURWIZARDDIALOGHOUR3CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR4CHECKBOX, wxID_HOURWIZARDDIALOGHOUR5CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR6CHECKBOX, wxID_HOURWIZARDDIALOGHOUR7CHECKBOX,
 wxID_HOURWIZARDDIALOGHOUR8CHECKBOX, wxID_HOURWIZARDDIALOGHOUR9CHECKBOX,
 wxID_HOURWIZARDDIALOGOKBUTTON, wxID_HOURWIZARDDIALOGSELECTALLBUTTON,
 wxID_HOURWIZARDDIALOGUNSELECTALLBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(29))

class HourWizardDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_HOURWIZARDDIALOG,
              name=u'HourWizardDialog', parent=prnt, pos=wx.Point(15, 161),
              size=wx.Size(507, 193), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Scheduler Wizard: Hour')
        self.SetClientSize(wx.Size(499, 166))

        self.hour0CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR0CHECKBOX,
              label=u'0', name=u'hour0CheckBox', parent=self, pos=wx.Point(16,
              24), size=wx.Size(40, 13), style=0)
        self.hour0CheckBox.SetValue(False)

        self.hour1CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR1CHECKBOX,
              label=u'1', name=u'hour1CheckBox', parent=self, pos=wx.Point(56,
              24), size=wx.Size(40, 13), style=0)
        self.hour1CheckBox.SetValue(False)

        self.hour2CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR2CHECKBOX,
              label=u'2', name=u'hour2CheckBox', parent=self, pos=wx.Point(96,
              24), size=wx.Size(40, 13), style=0)
        self.hour2CheckBox.SetValue(False)

        self.hour3CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR3CHECKBOX,
              label=u'3', name=u'hour3CheckBox', parent=self, pos=wx.Point(136,
              24), size=wx.Size(40, 13), style=0)
        self.hour3CheckBox.SetValue(False)

        self.hour4CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR4CHECKBOX,
              label=u'4', name=u'hour4CheckBox', parent=self, pos=wx.Point(176,
              24), size=wx.Size(40, 13), style=0)
        self.hour4CheckBox.SetValue(False)

        self.hour5CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR5CHECKBOX,
              label=u'5', name=u'hour5CheckBox', parent=self, pos=wx.Point(216,
              24), size=wx.Size(40, 13), style=0)
        self.hour5CheckBox.SetValue(False)

        self.hour6CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR6CHECKBOX,
              label=u'6', name=u'hour6CheckBox', parent=self, pos=wx.Point(256,
              24), size=wx.Size(40, 13), style=0)
        self.hour6CheckBox.SetValue(False)

        self.hour7CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR7CHECKBOX,
              label=u'7', name=u'hour7CheckBox', parent=self, pos=wx.Point(296,
              24), size=wx.Size(40, 13), style=0)
        self.hour7CheckBox.SetValue(False)

        self.hour8CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR8CHECKBOX,
              label=u'8', name=u'hour8CheckBox', parent=self, pos=wx.Point(336,
              24), size=wx.Size(40, 13), style=0)
        self.hour8CheckBox.SetValue(False)

        self.hour9CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR9CHECKBOX,
              label=u'9', name=u'hour9CheckBox', parent=self, pos=wx.Point(376,
              24), size=wx.Size(40, 13), style=0)
        self.hour9CheckBox.SetValue(False)

        self.hour10CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR10CHECKBOX,
              label=u'10', name=u'hour10CheckBox', parent=self, pos=wx.Point(416,
              24), size=wx.Size(40, 13), style=0)
        self.hour10CheckBox.SetValue(False)

        self.hour11CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR11CHECKBOX,
              label=u'11', name=u'hour11CheckBox', parent=self, pos=wx.Point(456,
              24), size=wx.Size(40, 13), style=0)
        self.hour11CheckBox.SetValue(False)

        self.hour12CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR12CHECKBOX,
              label=u'12', name=u'hour12CheckBox', parent=self, pos=wx.Point(16,
              56), size=wx.Size(40, 13), style=0)
        self.hour12CheckBox.SetValue(False)

        self.hour13CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR13CHECKBOX,
              label=u'13', name=u'hour13CheckBox', parent=self, pos=wx.Point(56,
              56), size=wx.Size(40, 13), style=0)
        self.hour13CheckBox.SetValue(False)

        self.hour14CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR14CHECKBOX,
              label=u'14', name=u'hour14CheckBox', parent=self, pos=wx.Point(96,
              56), size=wx.Size(40, 13), style=0)
        self.hour14CheckBox.SetValue(False)

        self.hour15CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR15CHECKBOX,
              label=u'15', name=u'hour15CheckBox', parent=self, pos=wx.Point(136,
              56), size=wx.Size(40, 13), style=0)
        self.hour15CheckBox.SetValue(False)

        self.hour16CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR16CHECKBOX,
              label=u'16', name=u'hour16CheckBox', parent=self, pos=wx.Point(176,
              56), size=wx.Size(40, 13), style=0)
        self.hour16CheckBox.SetValue(False)

        self.hour17CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR17CHECKBOX,
              label=u'17', name=u'hour17CheckBox', parent=self, pos=wx.Point(216,
              56), size=wx.Size(40, 13), style=0)
        self.hour17CheckBox.SetValue(False)

        self.hour18CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR18CHECKBOX,
              label=u'18', name=u'hour18CheckBox', parent=self, pos=wx.Point(256,
              56), size=wx.Size(40, 13), style=0)
        self.hour18CheckBox.SetValue(False)

        self.hour19CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR19CHECKBOX,
              label=u'19', name=u'hour19CheckBox', parent=self, pos=wx.Point(296,
              56), size=wx.Size(40, 13), style=0)
        self.hour19CheckBox.SetValue(False)

        self.hour20CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR20CHECKBOX,
              label=u'20', name=u'hour20CheckBox', parent=self, pos=wx.Point(336,
              56), size=wx.Size(40, 13), style=0)
        self.hour20CheckBox.SetValue(False)

        self.hour21CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR21CHECKBOX,
              label=u'21', name=u'hour21CheckBox', parent=self, pos=wx.Point(376,
              56), size=wx.Size(40, 13), style=0)
        self.hour21CheckBox.SetValue(False)

        self.hour22CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR22CHECKBOX,
              label=u'22', name=u'hour22CheckBox', parent=self, pos=wx.Point(416,
              56), size=wx.Size(40, 13), style=0)
        self.hour22CheckBox.SetValue(False)

        self.hour23CheckBox = wx.CheckBox(id=wxID_HOURWIZARDDIALOGHOUR23CHECKBOX,
              label=u'23', name=u'hour23CheckBox', parent=self, pos=wx.Point(456,
              56), size=wx.Size(40, 13), style=0)
        self.hour23CheckBox.SetValue(False)

        self.selectAllButton = wx.Button(id=wxID_HOURWIZARDDIALOGSELECTALLBUTTON,
              label=u'&Select All', name=u'selectAllButton', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.selectAllButton, wxID_HOURWIZARDDIALOGSELECTALLBUTTON,
              self.OnSelectallbuttonButton)

        self.unselectAllButton = wx.Button(id=wxID_HOURWIZARDDIALOGUNSELECTALLBUTTON,
              label=u'&Unselect All', name=u'unselectAllButton', parent=self,
              pos=wx.Point(104, 88), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.unselectAllButton,
              wxID_HOURWIZARDDIALOGUNSELECTALLBUTTON,
              self.OnUnselectallbuttonButton)

        self.OKButton = wx.Button(id=wxID_HOURWIZARDDIALOGOKBUTTON, label=u'&OK',
              name=u'OKButton', parent=self, pos=wx.Point(152, 136),
              size=wx.Size(75, 23), style=0)
        self.OKButton.SetDefault()
        wx.EVT_BUTTON(self.OKButton, wxID_HOURWIZARDDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_HOURWIZARDDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(272, 136), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_HOURWIZARDDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent
        self.hourControls = (self.hour0CheckBox, self.hour1CheckBox, self.hour2CheckBox,
            self.hour3CheckBox, self.hour4CheckBox, self.hour5CheckBox, self.hour6CheckBox,
            self.hour7CheckBox, self.hour8CheckBox, self.hour9CheckBox, self.hour10CheckBox,
            self.hour11CheckBox, self.hour12CheckBox, self.hour13CheckBox, self.hour14CheckBox,
            self.hour15CheckBox, self.hour16CheckBox, self.hour17CheckBox, self.hour18CheckBox,
            self.hour19CheckBox, self.hour20CheckBox, self.hour21CheckBox, self.hour22CheckBox,
            self.hour23CheckBox)
        for hour in range(24):
            try:
                m = pycron.Matcher(parent.hourTextCtrl.GetValue(), lineno = -1)
                m.minval = 0
                m.maxval = 23
                if m.matches(hour, -1):
                    self.setHour(hour, True)
            except pycron.InvalidLineException:
                pass

    def setHour(self, hour, value):
        self.hourControls[hour].SetValue(value)

    def getHour(self, hour):
        return self.hourControls[hour].GetValue()

    def setAllHours(self, value):
        for hour in range(24):
            self.setHour(hour, value)

    def OnSelectallbuttonButton(self, event):
        self.setAllHours(True)

    def getHourStringFromValues(self, values):
        return tools.getValueStringFromValues(values, 0, 23)

    def OnOkbuttonButton(self, event):
        values = []
        for hour in range(24):
            values += [self.getHour(hour)]
        self.parent.hour = self.getHourStringFromValues(values)
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnUnselectallbuttonButton(self, event):
        self.setAllHours(False)
