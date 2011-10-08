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
    return MinuteWizardDialog(parent)

[wxID_MINUTEWIZARDDIALOG, wxID_MINUTEWIZARDDIALOGCANCELBUTTON,
 wxID_MINUTEWIZARDDIALOGEVERYFIFTEENBUTTON,
 wxID_MINUTEWIZARDDIALOGEVERYFIVEBUTTON,
 wxID_MINUTEWIZARDDIALOGEVERYTENBUTTON,
 wxID_MINUTEWIZARDDIALOGMINUTE0CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE10CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE11CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE12CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE13CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE14CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE15CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE16CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE17CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE18CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE19CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE1CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE20CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE21CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE22CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE23CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE24CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE25CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE26CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE27CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE28CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE29CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE2CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE30CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE31CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE32CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE33CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE34CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE35CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE36CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE37CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE38CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE39CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE3CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE40CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE41CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE42CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE43CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE44CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE45CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE46CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE47CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE48CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE49CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE4CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE50CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE51CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE52CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE53CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE54CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE55CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE56CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE57CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE58CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE59CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE5CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE6CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE7CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE8CHECKBOX,
 wxID_MINUTEWIZARDDIALOGMINUTE9CHECKBOX, wxID_MINUTEWIZARDDIALOGOKBUTTON,
 wxID_MINUTEWIZARDDIALOGSELECTALLBUTTON,
 wxID_MINUTEWIZARDDIALOGUNSELECTALLBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(68))

class MinuteWizardDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MINUTEWIZARDDIALOG,
              name=u'MinuteWizardDialog', parent=prnt, pos=wx.Point(27, 66),
              size=wx.Size(433, 339), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Scheduler Wizard: Minute')
        self.SetClientSize(wx.Size(425, 312))

        self.minute0CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE0CHECKBOX,
              label=u'0', name=u'minute0CheckBox', parent=self, pos=wx.Point(16,
              24), size=wx.Size(40, 13), style=0)
        self.minute0CheckBox.SetValue(False)

        self.minute1CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE1CHECKBOX,
              label=u'1', name=u'minute1CheckBox', parent=self, pos=wx.Point(56,
              24), size=wx.Size(40, 13), style=0)
        self.minute1CheckBox.SetValue(False)

        self.minute2CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE2CHECKBOX,
              label=u'2', name=u'minute2CheckBox', parent=self, pos=wx.Point(96,
              24), size=wx.Size(40, 13), style=0)
        self.minute2CheckBox.SetValue(False)

        self.minute3CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE3CHECKBOX,
              label=u'3', name=u'minute3CheckBox', parent=self, pos=wx.Point(136,
              24), size=wx.Size(40, 13), style=0)
        self.minute3CheckBox.SetValue(False)

        self.minute4CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE4CHECKBOX,
              label=u'4', name=u'minute4CheckBox', parent=self, pos=wx.Point(176,
              24), size=wx.Size(40, 13), style=0)
        self.minute4CheckBox.SetValue(False)

        self.minute5CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE5CHECKBOX,
              label=u'5', name=u'minute5CheckBox', parent=self, pos=wx.Point(216,
              24), size=wx.Size(40, 13), style=0)
        self.minute5CheckBox.SetValue(False)

        self.minute6CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE6CHECKBOX,
              label=u'6', name=u'minute6CheckBox', parent=self, pos=wx.Point(256,
              24), size=wx.Size(40, 13), style=0)
        self.minute6CheckBox.SetValue(False)

        self.minute7CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE7CHECKBOX,
              label=u'7', name=u'minute7CheckBox', parent=self, pos=wx.Point(296,
              24), size=wx.Size(40, 13), style=0)
        self.minute7CheckBox.SetValue(False)

        self.minute8CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE8CHECKBOX,
              label=u'8', name=u'minute8CheckBox', parent=self, pos=wx.Point(336,
              24), size=wx.Size(40, 13), style=0)
        self.minute8CheckBox.SetValue(False)

        self.minute9CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE9CHECKBOX,
              label=u'9', name=u'minute9CheckBox', parent=self, pos=wx.Point(376,
              24), size=wx.Size(40, 13), style=0)
        self.minute9CheckBox.SetValue(False)

        self.minute10CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE10CHECKBOX,
              label=u'10', name=u'minute10CheckBox', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(40, 13), style=0)
        self.minute10CheckBox.SetValue(False)

        self.minute11CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE11CHECKBOX,
              label=u'11', name=u'minute11CheckBox', parent=self,
              pos=wx.Point(56, 56), size=wx.Size(40, 13), style=0)
        self.minute11CheckBox.SetValue(False)

        self.minute12CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE12CHECKBOX,
              label=u'12', name=u'minute12CheckBox', parent=self,
              pos=wx.Point(96, 56), size=wx.Size(40, 13), style=0)
        self.minute12CheckBox.SetValue(False)

        self.minute13CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE13CHECKBOX,
              label=u'13', name=u'minute13CheckBox', parent=self,
              pos=wx.Point(136, 56), size=wx.Size(40, 13), style=0)
        self.minute13CheckBox.SetValue(False)

        self.minute14CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE14CHECKBOX,
              label=u'14', name=u'minute14CheckBox', parent=self,
              pos=wx.Point(176, 56), size=wx.Size(40, 13), style=0)
        self.minute14CheckBox.SetValue(False)

        self.minute15CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE15CHECKBOX,
              label=u'15', name=u'minute15CheckBox', parent=self,
              pos=wx.Point(216, 56), size=wx.Size(40, 13), style=0)
        self.minute15CheckBox.SetValue(False)

        self.minute16CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE16CHECKBOX,
              label=u'16', name=u'minute16CheckBox', parent=self,
              pos=wx.Point(256, 56), size=wx.Size(40, 13), style=0)
        self.minute16CheckBox.SetValue(False)

        self.minute17CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE17CHECKBOX,
              label=u'17', name=u'minute17CheckBox', parent=self,
              pos=wx.Point(296, 56), size=wx.Size(40, 13), style=0)
        self.minute17CheckBox.SetValue(False)

        self.minute18CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE18CHECKBOX,
              label=u'18', name=u'minute18CheckBox', parent=self,
              pos=wx.Point(336, 56), size=wx.Size(40, 13), style=0)
        self.minute18CheckBox.SetValue(False)

        self.minute19CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE19CHECKBOX,
              label=u'19', name=u'minute19CheckBox', parent=self,
              pos=wx.Point(376, 56), size=wx.Size(40, 13), style=0)
        self.minute19CheckBox.SetValue(False)

        self.minute20CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE20CHECKBOX,
              label=u'20', name=u'minute20CheckBox', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(40, 13), style=0)
        self.minute20CheckBox.SetValue(False)

        self.minute21CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE21CHECKBOX,
              label=u'21', name=u'minute21CheckBox', parent=self,
              pos=wx.Point(56, 88), size=wx.Size(40, 13), style=0)
        self.minute21CheckBox.SetValue(False)

        self.minute22CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE22CHECKBOX,
              label=u'22', name=u'minute22CheckBox', parent=self,
              pos=wx.Point(96, 88), size=wx.Size(40, 13), style=0)
        self.minute22CheckBox.SetValue(False)

        self.minute23CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE23CHECKBOX,
              label=u'23', name=u'minute23CheckBox', parent=self,
              pos=wx.Point(136, 88), size=wx.Size(40, 13), style=0)
        self.minute23CheckBox.SetValue(False)

        self.minute24CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE24CHECKBOX,
              label=u'24', name=u'minute24CheckBox', parent=self,
              pos=wx.Point(176, 88), size=wx.Size(40, 13), style=0)
        self.minute24CheckBox.SetValue(False)

        self.minute25CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE25CHECKBOX,
              label=u'25', name=u'minute25CheckBox', parent=self,
              pos=wx.Point(216, 88), size=wx.Size(40, 13), style=0)
        self.minute25CheckBox.SetValue(False)

        self.minute26CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE26CHECKBOX,
              label=u'26', name=u'minute26CheckBox', parent=self,
              pos=wx.Point(256, 88), size=wx.Size(40, 13), style=0)
        self.minute26CheckBox.SetValue(False)

        self.minute27CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE27CHECKBOX,
              label=u'27', name=u'minute27CheckBox', parent=self,
              pos=wx.Point(296, 88), size=wx.Size(40, 13), style=0)
        self.minute27CheckBox.SetValue(False)

        self.minute28CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE28CHECKBOX,
              label=u'28', name=u'minute28CheckBox', parent=self,
              pos=wx.Point(336, 88), size=wx.Size(40, 13), style=0)
        self.minute28CheckBox.SetValue(False)

        self.minute29CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE29CHECKBOX,
              label=u'29', name=u'minute29CheckBox', parent=self,
              pos=wx.Point(376, 88), size=wx.Size(40, 13), style=0)
        self.minute29CheckBox.SetValue(False)

        self.minute30CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE30CHECKBOX,
              label=u'30', name=u'minute30CheckBox', parent=self,
              pos=wx.Point(16, 120), size=wx.Size(40, 13), style=0)
        self.minute30CheckBox.SetValue(False)

        self.minute31CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE31CHECKBOX,
              label=u'31', name=u'minute31CheckBox', parent=self,
              pos=wx.Point(56, 120), size=wx.Size(40, 13), style=0)
        self.minute31CheckBox.SetValue(False)

        self.minute32CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE32CHECKBOX,
              label=u'32', name=u'minute32CheckBox', parent=self,
              pos=wx.Point(96, 120), size=wx.Size(40, 13), style=0)
        self.minute32CheckBox.SetValue(False)

        self.minute33CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE33CHECKBOX,
              label=u'33', name=u'minute33CheckBox', parent=self,
              pos=wx.Point(136, 120), size=wx.Size(40, 13), style=0)
        self.minute33CheckBox.SetValue(False)

        self.minute34CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE34CHECKBOX,
              label=u'34', name=u'minute34CheckBox', parent=self,
              pos=wx.Point(176, 120), size=wx.Size(40, 13), style=0)
        self.minute34CheckBox.SetValue(False)

        self.minute35CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE35CHECKBOX,
              label=u'35', name=u'minute35CheckBox', parent=self,
              pos=wx.Point(216, 120), size=wx.Size(40, 13), style=0)
        self.minute35CheckBox.SetValue(False)

        self.minute36CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE36CHECKBOX,
              label=u'36', name=u'minute36CheckBox', parent=self,
              pos=wx.Point(256, 120), size=wx.Size(40, 13), style=0)
        self.minute36CheckBox.SetValue(False)

        self.minute37CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE37CHECKBOX,
              label=u'37', name=u'minute37CheckBox', parent=self,
              pos=wx.Point(296, 120), size=wx.Size(40, 13), style=0)
        self.minute37CheckBox.SetValue(False)

        self.minute38CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE38CHECKBOX,
              label=u'38', name=u'minute38CheckBox', parent=self,
              pos=wx.Point(336, 120), size=wx.Size(40, 13), style=0)
        self.minute38CheckBox.SetValue(False)

        self.minute39CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE39CHECKBOX,
              label=u'39', name=u'minute39CheckBox', parent=self,
              pos=wx.Point(376, 120), size=wx.Size(40, 13), style=0)
        self.minute39CheckBox.SetValue(False)

        self.minute40CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE40CHECKBOX,
              label=u'40', name=u'minute40CheckBox', parent=self,
              pos=wx.Point(16, 152), size=wx.Size(40, 13), style=0)
        self.minute40CheckBox.SetValue(False)

        self.minute41CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE41CHECKBOX,
              label=u'41', name=u'minute41CheckBox', parent=self,
              pos=wx.Point(56, 152), size=wx.Size(40, 13), style=0)
        self.minute41CheckBox.SetValue(False)

        self.minute42CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE42CHECKBOX,
              label=u'42', name=u'minute42CheckBox', parent=self,
              pos=wx.Point(96, 152), size=wx.Size(40, 13), style=0)
        self.minute42CheckBox.SetValue(False)

        self.minute43CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE43CHECKBOX,
              label=u'43', name=u'minute43CheckBox', parent=self,
              pos=wx.Point(136, 152), size=wx.Size(40, 13), style=0)
        self.minute43CheckBox.SetValue(False)

        self.minute44CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE44CHECKBOX,
              label=u'44', name=u'minute44CheckBox', parent=self,
              pos=wx.Point(176, 152), size=wx.Size(40, 13), style=0)
        self.minute44CheckBox.SetValue(False)

        self.minute45CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE45CHECKBOX,
              label=u'45', name=u'minute45CheckBox', parent=self,
              pos=wx.Point(216, 152), size=wx.Size(40, 13), style=0)
        self.minute45CheckBox.SetValue(False)

        self.minute46CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE46CHECKBOX,
              label=u'46', name=u'minute46CheckBox', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(40, 13), style=0)
        self.minute46CheckBox.SetValue(False)

        self.minute47CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE47CHECKBOX,
              label=u'47', name=u'minute47CheckBox', parent=self,
              pos=wx.Point(296, 152), size=wx.Size(40, 13), style=0)
        self.minute47CheckBox.SetValue(False)

        self.minute48CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE48CHECKBOX,
              label=u'48', name=u'minute48CheckBox', parent=self,
              pos=wx.Point(336, 152), size=wx.Size(40, 13), style=0)
        self.minute48CheckBox.SetValue(False)

        self.minute49CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE49CHECKBOX,
              label=u'49', name=u'minute49CheckBox', parent=self,
              pos=wx.Point(376, 152), size=wx.Size(40, 13), style=0)
        self.minute49CheckBox.SetValue(False)

        self.minute50CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE50CHECKBOX,
              label=u'50', name=u'minute50CheckBox', parent=self,
              pos=wx.Point(16, 184), size=wx.Size(40, 13), style=0)
        self.minute50CheckBox.SetValue(False)

        self.minute51CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE51CHECKBOX,
              label=u'51', name=u'minute51CheckBox', parent=self,
              pos=wx.Point(56, 184), size=wx.Size(40, 13), style=0)
        self.minute51CheckBox.SetValue(False)

        self.minute52CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE52CHECKBOX,
              label=u'52', name=u'minute52CheckBox', parent=self,
              pos=wx.Point(96, 184), size=wx.Size(40, 13), style=0)
        self.minute52CheckBox.SetValue(False)

        self.minute53CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE53CHECKBOX,
              label=u'53', name=u'minute53CheckBox', parent=self,
              pos=wx.Point(136, 184), size=wx.Size(40, 13), style=0)
        self.minute53CheckBox.SetValue(False)

        self.minute54CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE54CHECKBOX,
              label=u'54', name=u'minute54CheckBox', parent=self,
              pos=wx.Point(176, 184), size=wx.Size(40, 13), style=0)
        self.minute54CheckBox.SetValue(False)

        self.minute55CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE55CHECKBOX,
              label=u'55', name=u'minute55CheckBox', parent=self,
              pos=wx.Point(216, 184), size=wx.Size(40, 13), style=0)
        self.minute55CheckBox.SetValue(False)

        self.minute56CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE56CHECKBOX,
              label=u'56', name=u'minute56CheckBox', parent=self,
              pos=wx.Point(256, 184), size=wx.Size(40, 13), style=0)
        self.minute56CheckBox.SetValue(False)

        self.minute57CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE57CHECKBOX,
              label=u'57', name=u'minute57CheckBox', parent=self,
              pos=wx.Point(296, 184), size=wx.Size(40, 13), style=0)
        self.minute57CheckBox.SetValue(False)

        self.minute58CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE58CHECKBOX,
              label=u'58', name=u'minute58CheckBox', parent=self,
              pos=wx.Point(336, 184), size=wx.Size(40, 13), style=0)
        self.minute58CheckBox.SetValue(False)

        self.minute59CheckBox = wx.CheckBox(id=wxID_MINUTEWIZARDDIALOGMINUTE59CHECKBOX,
              label=u'59', name=u'minute59CheckBox', parent=self,
              pos=wx.Point(376, 184), size=wx.Size(40, 13), style=0)
        self.minute59CheckBox.SetValue(False)

        self.selectAllButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGSELECTALLBUTTON,
              label=u'&Select All', name=u'selectAllButton', parent=self,
              pos=wx.Point(16, 224), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.selectAllButton, wxID_MINUTEWIZARDDIALOGSELECTALLBUTTON,
              self.OnSelectallbuttonButton)

        self.unselectAllButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGUNSELECTALLBUTTON,
              label=u'&Unselect All', name=u'unselectAllButton', parent=self,
              pos=wx.Point(96, 224), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.unselectAllButton,
              wxID_MINUTEWIZARDDIALOGUNSELECTALLBUTTON,
              self.OnUnselectallbuttonButton)

        self.everyFiveButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGEVERYFIVEBUTTON,
              label=u'Every Five', name=u'everyFiveButton', parent=self,
              pos=wx.Point(176, 224), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.everyFiveButton, wxID_MINUTEWIZARDDIALOGEVERYFIVEBUTTON,
              self.OnEveryfivebuttonButton)

        self.everyTenButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGEVERYTENBUTTON,
              label=u'Every Ten', name=u'everyTenButton', parent=self,
              pos=wx.Point(256, 224), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.everyTenButton, wxID_MINUTEWIZARDDIALOGEVERYTENBUTTON,
              self.OnEverytenbuttonButton)

        self.everyFifteenButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGEVERYFIFTEENBUTTON,
              label=u'Every Fifteen', name=u'everyFifteenButton', parent=self,
              pos=wx.Point(336, 224), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.everyFifteenButton,
              wxID_MINUTEWIZARDDIALOGEVERYFIFTEENBUTTON,
              self.OnEveryfifteenbuttonButton)

        self.OKButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGOKBUTTON,
              label=u'&OK', name=u'OKButton', parent=self, pos=wx.Point(120,
              280), size=wx.Size(75, 23), style=0)
        self.OKButton.SetDefault()
        wx.EVT_BUTTON(self.OKButton, wxID_MINUTEWIZARDDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.cancelButton = wx.Button(id=wxID_MINUTEWIZARDDIALOGCANCELBUTTON,
              label=u'&Cancel', name=u'cancelButton', parent=self,
              pos=wx.Point(232, 280), size=wx.Size(75, 23), style=0)
        wx.EVT_BUTTON(self.cancelButton, wxID_MINUTEWIZARDDIALOGCANCELBUTTON,
              self.OnCancelbuttonButton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent
        self.minuteControls = (self.minute0CheckBox, self.minute1CheckBox, self.minute2CheckBox,
            self.minute3CheckBox, self.minute4CheckBox, self.minute5CheckBox, self.minute6CheckBox,
            self.minute7CheckBox, self.minute8CheckBox, self.minute9CheckBox, self.minute10CheckBox,
            self.minute11CheckBox, self.minute12CheckBox, self.minute13CheckBox, self.minute14CheckBox,
            self.minute15CheckBox, self.minute16CheckBox, self.minute17CheckBox, self.minute18CheckBox,
            self.minute19CheckBox, self.minute20CheckBox, self.minute21CheckBox, self.minute22CheckBox,
            self.minute23CheckBox, self.minute24CheckBox, self.minute25CheckBox, self.minute26CheckBox,
            self.minute27CheckBox, self.minute28CheckBox, self.minute29CheckBox, self.minute30CheckBox,
            self.minute31CheckBox, self.minute32CheckBox, self.minute33CheckBox, self.minute34CheckBox,
            self.minute35CheckBox, self.minute36CheckBox, self.minute37CheckBox, self.minute38CheckBox,
            self.minute39CheckBox, self.minute40CheckBox, self.minute41CheckBox, self.minute42CheckBox,
            self.minute43CheckBox, self.minute44CheckBox, self.minute45CheckBox, self.minute46CheckBox,
            self.minute47CheckBox, self.minute48CheckBox, self.minute49CheckBox, self.minute50CheckBox,
            self.minute51CheckBox, self.minute52CheckBox, self.minute53CheckBox, self.minute54CheckBox,
            self.minute55CheckBox, self.minute56CheckBox, self.minute57CheckBox, self.minute58CheckBox,
            self.minute59CheckBox)
        for minute in range(60):
            try:
                m = pycron.Matcher(parent.minuteTextCtrl.GetValue(), lineno = -1)
                m.minval = 0
                m.maxval = 59
                if m.matches(minute, -1):
                    self.setMinute(minute, True)
            except pycron.InvalidLineException:
                pass

    def setMinute(self, minute, value):
        self.minuteControls[minute].SetValue(value)

    def getMinute(self, minute):
        return self.minuteControls[minute].GetValue()

    def setAllMinutes(self, value):
        for minute in range(60):
            self.setMinute(minute, value)

    def OnSelectallbuttonButton(self, event):
        self.setAllMinutes(True)

    def getMinuteStringFromValues(self, values):
        return tools.getValueStringFromValues(values, 0, 59)

    def OnOkbuttonButton(self, event):
        values = []
        for minute in range(60):
            values += [self.getMinute(minute)]
        self.parent.minute = self.getMinuteStringFromValues(values)
        self.Close()
        self.SetReturnCode(wx.ID_OK)

    def OnCancelbuttonButton(self, event):
        self.Close()

    def OnUnselectallbuttonButton(self, event):
        self.setAllMinutes(False)

    def OnEveryfivebuttonButton(self, event):
        self.setAllMinutes(False)
        for minute in xrange(0, 60, 5):
            self.setMinute(minute, True)

    def OnEverytenbuttonButton(self, event):
        self.setAllMinutes(False)
        for minute in xrange(0, 60, 10):
            self.setMinute(minute, True)

    def OnEveryfifteenbuttonButton(self, event):
        self.setAllMinutes(False)
        for minute in xrange(0, 60, 15):
            self.setMinute(minute, True)
