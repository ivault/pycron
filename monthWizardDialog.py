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
    return MonthWizardDialog(parent)

[wxID_MONTHWIZARDDIALOG, wxID_MONTHWIZARDDIALOGAPRCHECKBOX,
 wxID_MONTHWIZARDDIALOGAUGCHECKBOX, wxID_MONTHWIZARDDIALOGCANCELBUTTON,
 wxID_MONTHWIZARDDIALOGDECCHECKBOX, wxID_MONTHWIZARDDIALOGFEBCHECKBOX,
 wxID_MONTHWIZARDDIALOGJANCHECKBOX, wxID_MONTHWIZARDDIALOGJULCHECKBOX,
 wxID_MONTHWIZARDDIALOGJUNCHECKBOX, wxID_MONTHWIZARDDIALOGMARCHECKBOX,
 wxID_MONTHWIZARDDIALOGMAYCHECKBOX, wxID_MONTHWIZARDDIALOGNOVCHECKBOX,
 wxID_MONTHWIZARDDIALOGOCTCHECKBOX, wxID_MONTHWIZARDDIALOGOKBUTTON,
 wxID_MONTHWIZARDDIALOGSELECTALLBUTTON, wxID_MONTHWIZARDDIALOGSEPCHECKBOX,
 wxID_MONTHWIZARDDIALOGUNSELECTALLBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(17))

class MonthWizardDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MONTHWIZARDDIALOG,
              name=u'MonthWizardDialog', parent=prnt, pos=wx.Point(34, 159),
              size=wx.Size(358, 199), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Scheduler Wizard: Month')
        self.SetClientSize(wx.Size(350, 172))

        self.janCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGJANCHECKBOX,
              label=u'Jan', name=u'janCheckBox', parent=self, pos=wx.Point(16,
              24), size=wx.Size(40, 13), style=0)
        self.janCheckBox.SetValue(False)

        self.febCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGFEBCHECKBOX,
              label=u'Feb', name=u'febCheckBox', parent=self, pos=wx.Point(72,
              24), size=wx.Size(40, 13), style=0)
        self.febCheckBox.SetValue(False)

        self.marCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGMARCHECKBOX,
              label=u'Mar', name=u'marCheckBox', parent=self, pos=wx.Point(128,
              24), size=wx.Size(40, 13), style=0)
        self.marCheckBox.SetValue(False)

        self.aprCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGAPRCHECKBOX,
              label=u'Apr', name=u'aprCheckBox', parent=self, pos=wx.Point(184,
              24), size=wx.Size(40, 13), style=0)
        self.aprCheckBox.SetValue(False)

        self.mayCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGMAYCHECKBOX,
              label=u'May', name=u'mayCheckBox', parent=self, pos=wx.Point(240,
              24), size=wx.Size(40, 13), style=0)
        self.mayCheckBox.SetValue(False)

        self.junCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGJUNCHECKBOX,
              label=u'Jun', name=u'junCheckBox', parent=self, pos=wx.Point(296,
              24), size=wx.Size(40, 13), style=0)
        self.junCheckBox.SetValue(False)

        self.julCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGJULCHECKBOX,
              label=u'Jul', name=u'julCheckBox', parent=self, pos=wx.Point(16,
              56), size=wx.Size(40, 13), style=0)
        self.julCheckBox.SetValue(False)

        self.augCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGAUGCHECKBOX,
              label=u'Aug', name=u'augCheckBox', parent=self, pos=wx.Point(72,
              56), size=wx.Size(40, 13), style=0)
        self.augCheckBox.SetValue(False)

        self.sepCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGSEPCHECKBOX,
              label=u'Sep', name=u'sepCheckBox', parent=self, pos=wx.Point(128,
              56), size=wx.Size(40, 13), style=0)
        self.sepCheckBox.SetValue(False)

        self.octCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGOCTCHECKBOX,
              label=u'Oct', name=u'octCheckBox', parent=self, pos=wx.Point(184,
              56), size=wx.Size(40, 13), style=0)
        self.octCheckBox.SetValue(False)

        self.novCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGNOVCHECKBOX,
              label=u'Nov', name=u'novCheckBox', parent=self, pos=wx.Point(240,
              56), size=wx.Size(40, 13), style=0)
        self.novCheckBox.SetValue(False)

        self.decCheckBox = wx.CheckBox(id=wxID_MONTHWIZARDDIALOGDECCHECKBOX,
              label=u'Dec', name=u'decCheckBox', parent=self, pos=wx.Point(296,
              56), size=wx.Size(40, 13), style=0)
        self.decCheckBox.SetValue(False)

        self.selectAllButton = wx.Button(id=wxID_MONTHWIZARDDIALOGSELECTALLBUTTON,
              label=u'&Select All', name=u'selectAllButton', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.selectAllButton, wxID_MONTHWIZARDDIALOGSELECTALLBUTTON,
              self.OnSelectallbuttonButton)

        self.unselectAllButton = wx.Button(id=wxID_MONTHWIZARDDIALOGUNSELECTALLBUTTON,
              label=u'&Unselect All', name=u'unselectAllButton', parent=self,
              pos=wx.Point(104, 88), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.unselectAllButton,
              wxID_MONTHWIZARDDIALOGUNSELECTALLBUTTON,
              self.OnUnselectallbuttonButton)

        self.OKButton = wx.Button(id=wxID_MONTHWIZARDDIALOGOKBUTTON,
              label=u'&OK', name=u'OKButton', parent=self, pos=wx.Point(72, 136),
              size=wx.Size(75, 23), style=0)
        self.OKButton.SetDefault()
        wx.EVT_BUTTON(self.OKButton, wxID_MONTHWIZARDDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_MONTHWIZARDDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(200, 136), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_MONTHWIZARDDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent
        self.monthControls = (self.janCheckBox, self.febCheckBox, self.marCheckBox,
            self.aprCheckBox, self.mayCheckBox, self.junCheckBox, self.julCheckBox,
            self.augCheckBox, self.sepCheckBox, self.octCheckBox, self.novCheckBox,
            self.decCheckBox)
        for month in xrange(1, 13):
            try:
                m = pycron.Matcher(parent.monthTextCtrl.GetValue(), lineno = -1)
                m.minval = 1
                m.maxval = 12
                if m.matches(month, -1):
                    self.setMonth(month, True)
            except pycron.InvalidLineException:
                pass

    def setMonth(self, month, value):
        self.monthControls[month - 1].SetValue(value)

    def getMonth(self, month):
        return self.monthControls[month - 1].GetValue()

    def setAllMonths(self, value):
        for month in xrange(1, 13):
            self.setMonth(month, value)

    def OnSelectallbuttonButton(self, event):
        self.setAllMonths(True)

    def getMonthStringFromValues(self, values):
        return tools.getValueStringFromValues(values, 1, 12)

    def OnOkbuttonButton(self, event):
        values = []
        for month in xrange(1, 13):
            values += [self.getMonth(month)]
        self.parent.month = self.getMonthStringFromValues(values)
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnUnselectallbuttonButton(self, event):
        self.setAllMonths(False)
