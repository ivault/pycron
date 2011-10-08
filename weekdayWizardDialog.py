#Boa:Dialog:WeekdayWizardDialog

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
    return WeekdayWizardDialog(parent)

[wxID_WEEKDAYWIZARDDIALOG, wxID_WEEKDAYWIZARDDIALOGCANCELBUTTON,
 wxID_WEEKDAYWIZARDDIALOGFRCHECKBOX, wxID_WEEKDAYWIZARDDIALOGMOCHECKBOX,
 wxID_WEEKDAYWIZARDDIALOGOKBUTTON, wxID_WEEKDAYWIZARDDIALOGSACHECKBOX,
 wxID_WEEKDAYWIZARDDIALOGSELECTALLBUTTON, wxID_WEEKDAYWIZARDDIALOGSUCHECKBOX,
 wxID_WEEKDAYWIZARDDIALOGTHCHECKBOX, wxID_WEEKDAYWIZARDDIALOGTUCHECKBOX,
 wxID_WEEKDAYWIZARDDIALOGUNSELECTALLBUTTON,
 wxID_WEEKDAYWIZARDDIALOGWECHECKBOX, wxID_WEEKDAYWIZARDDIALOGWEEKDAYSBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(13))

class WeekdayWizardDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_WEEKDAYWIZARDDIALOG,
              name=u'WeekdayWizardDialog', parent=prnt, pos=wx.Point(17, 176),
              size=wx.Size(413, 171), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Scheduler Wizard: Week Day')
        self.SetClientSize(wx.Size(405, 144))

        self.moCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGMOCHECKBOX,
              label=u'Mon', name=u'moCheckBox', parent=self, pos=wx.Point(16,
              24), size=wx.Size(40, 13), style=0)
        self.moCheckBox.SetValue(False)

        self.tuCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGTUCHECKBOX,
              label=u'Tue', name=u'tuCheckBox', parent=self, pos=wx.Point(72,
              24), size=wx.Size(40, 13), style=0)
        self.tuCheckBox.SetValue(False)

        self.weCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGWECHECKBOX,
              label=u'Wed', name=u'weCheckBox', parent=self, pos=wx.Point(128,
              24), size=wx.Size(48, 13), style=0)
        self.weCheckBox.SetValue(False)

        self.thCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGTHCHECKBOX,
              label=u'Thu', name=u'thCheckBox', parent=self, pos=wx.Point(184,
              24), size=wx.Size(40, 13), style=0)
        self.thCheckBox.SetValue(False)

        self.frCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGFRCHECKBOX,
              label=u'Fri', name=u'frCheckBox', parent=self, pos=wx.Point(240,
              24), size=wx.Size(40, 13), style=0)
        self.frCheckBox.SetValue(False)

        self.saCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGSACHECKBOX,
              label=u'Sat', name=u'saCheckBox', parent=self, pos=wx.Point(296,
              24), size=wx.Size(40, 13), style=0)
        self.saCheckBox.SetValue(False)

        self.suCheckBox = wx.CheckBox(id=wxID_WEEKDAYWIZARDDIALOGSUCHECKBOX,
              label=u'Sun', name=u'suCheckBox', parent=self, pos=wx.Point(352,
              24), size=wx.Size(40, 13), style=0)
        self.suCheckBox.SetValue(False)

        self.selectAllButton = wx.Button(id=wxID_WEEKDAYWIZARDDIALOGSELECTALLBUTTON,
              label=u'&Select All', name=u'selectAllButton', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.selectAllButton,
              wxID_WEEKDAYWIZARDDIALOGSELECTALLBUTTON,
              self.OnSelectallbuttonButton)

        self.unselectAllButton = wx.Button(id=wxID_WEEKDAYWIZARDDIALOGUNSELECTALLBUTTON,
              label=u'&Unselect All', name=u'unselectAllButton', parent=self,
              pos=wx.Point(104, 56), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.unselectAllButton,
              wxID_WEEKDAYWIZARDDIALOGUNSELECTALLBUTTON,
              self.OnUnselectallbuttonButton)

        self.weekdaysButton = wx.Button(id=wxID_WEEKDAYWIZARDDIALOGWEEKDAYSBUTTON,
              label=u'Weekdays', name=u'weekdaysButton', parent=self,
              pos=wx.Point(317, 56), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.weekdaysButton, wxID_WEEKDAYWIZARDDIALOGWEEKDAYSBUTTON,
              self.OnWeekdaysbuttonButton)

        self.OKButton = wx.Button(id=wxID_WEEKDAYWIZARDDIALOGOKBUTTON,
              label=u'&OK', name=u'OKButton', parent=self, pos=wx.Point(112,
              112), size=wx.Size(75, 23), style=0)
        self.OKButton.SetDefault()
        wx.EVT_BUTTON(self.OKButton, wxID_WEEKDAYWIZARDDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_WEEKDAYWIZARDDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(216, 112), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_WEEKDAYWIZARDDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent
        self.weekdayControls = (self.suCheckBox, self.moCheckBox, self.tuCheckBox, self.weCheckBox,
            self.thCheckBox, self.frCheckBox, self.saCheckBox)
        self.old_weekdayControls = (self.moCheckBox, self.tuCheckBox, self.weCheckBox,
            self.thCheckBox, self.frCheckBox, self.saCheckBox, self.suCheckBox)
        config = pycron.ConfigParser.ConfigParser()
        config.read(pycron.SETTINGS_FILENAME)
        self.old_dow_compatibility = False
        if config.has_section("pycron") and config.has_option("pycron", "old_dow_compatibility"):
            self.old_dow_compatibility = config.getboolean("pycron",
                                                           "old_dow_compatibility")
        for weekday in range(7):
            try:
                m = pycron.Matcher(parent.dowTextCtrl.GetValue(), lineno = -1)
                m.minval = 0
                m.maxval = 6
                if m.matches(weekday, -1):
                    self.setWeekday(weekday, True)
            except pycron.InvalidLineException:
                pass

    def setWeekday(self, weekday, value):
        if self.old_dow_compatibility:
            self.old_weekdayControls[weekday].SetValue(value)
        else:
            self.weekdayControls[weekday].SetValue(value)

    def getWeekday(self, weekday):
        if self.old_dow_compatibility:
            return self.old_weekdayControls[weekday].GetValue()
        else:
            return self.weekdayControls[weekday].GetValue()

    def setAllWeekdays(self, value):
        for weekday in range(7):
            self.setWeekday(weekday, value)

    def OnSelectallbuttonButton(self, event):
        self.setAllWeekdays(True)

    def getWeekdayStringFromValues(self, values):
        return tools.getValueStringFromValues(values, 0, 6)

    def OnOkbuttonButton(self, event):
        values = []
        for weekday in range(7):
            values += [self.getWeekday(weekday)]
        dow = self.getWeekdayStringFromValues(values)
        if not self.old_dow_compatibility:
            weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
            for day in weekdays:
                dow = dow.replace(str(weekdays.index(day)), day)
        self.parent.dow = dow
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnUnselectallbuttonButton(self, event):
        self.setAllWeekdays(False)

    def OnWeekdaysbuttonButton(self, event):
        for weekday in range(5):
            if self.old_dow_compatibility:
                self.setWeekday(weekday, True)
            else:
                self.setWeekday(weekday + 1, True)
        if self.old_dow_compatibility:
            self.setWeekday(5, False)
        else:
            self.setWeekday(0, False)
        self.setWeekday(6, False)
