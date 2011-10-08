#Boa:Frame:EditorFrame

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

import aboutDialog, taskDialog
import crontab

FRAME_TITLE = u'crontab.txt Editor'

listColumns = {0: "Line No", 1: "Minute", 2: "Hour", 3: "Day of Month", 4: "Month",
               5: "Week Day", 6: "Task"}

NUMBER_OF_COLUMNS = len(listColumns)

def create(parent):
    return EditorFrame(parent)

[wxID_EDITORFRAME, wxID_EDITORFRAMECRONITEMLIST, wxID_EDITORFRAMESTATUSBAR,
] = map(lambda _init_ctrls: wx.NewId(), range(3))

[wxID_EDITORFRAMEFILEMENUITEMS0, wxID_EDITORFRAMEFILEMENUITEMS1,
 wxID_EDITORFRAMEFILEMENUITEMS2, wxID_EDITORFRAMEFILEMENUITEMS3,
 wxID_EDITORFRAMEFILEMENUITEMS4,
] = map(lambda _init_coll_fileMenu_Items: wx.NewId(), range(5))

[wxID_EDITORFRAMEITEMMENUITEMS0, wxID_EDITORFRAMEITEMMENUITEMS1,
 wxID_EDITORFRAMEITEMMENUITEMS2,
] = map(lambda _init_coll_itemMenu_Items: wx.NewId(), range(3))

[wxID_EDITORFRAMEHELPMENUITEMS0] = map(lambda _init_coll_helpMenu_Items: wx.NewId(), range(1))

class EditorFrame(wx.Frame):
    def _init_coll_helpMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Display general information about crontab.txt Editor',
              id=wxID_EDITORFRAMEHELPMENUITEMS0, text=u'About...',
              kind=wx.ITEM_NORMAL)
        wx.EVT_MENU(self, wxID_EDITORFRAMEHELPMENUITEMS0,
              self.OnHelpmenuitems0Menu)

    def _init_coll_mainMenuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.fileMenu, title=u'File')
        parent.Append(menu=self.itemMenu, title=u'Item')
        parent.Append(menu=self.helpMenu, title=u'Help')

    def _init_coll_itemMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Create a new crontab entry',
              id=wxID_EDITORFRAMEITEMMENUITEMS0, text=u'New',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Change the selected entry',
              id=wxID_EDITORFRAMEITEMMENUITEMS1, text=u'Change',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Delete the selected entry',
              id=wxID_EDITORFRAMEITEMMENUITEMS2, text=u'Delete',
              kind=wx.ITEM_NORMAL)
        wx.EVT_MENU(self, wxID_EDITORFRAMEITEMMENUITEMS0,
              self.OnItemMenuItems0Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEITEMMENUITEMS1,
              self.OnItemMenuItems1Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEITEMMENUITEMS2,
              self.OnItemMenuItems2Menu)

    def _init_coll_fileMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Open a crontab.txt file',
              id=wxID_EDITORFRAMEFILEMENUITEMS0, text=u'Open',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Save the crontab.txt file',
              id=wxID_EDITORFRAMEFILEMENUITEMS1, text=u'Save',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Save the current file with a different name',
              id=wxID_EDITORFRAMEFILEMENUITEMS2, text=u'Save As...',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Close the current file',
              id=wxID_EDITORFRAMEFILEMENUITEMS3, text=u'Close',
              kind=wx.ITEM_NORMAL)
        parent.Append(help=u'Exit application',
              id=wxID_EDITORFRAMEFILEMENUITEMS4, text=u'Exit',
              kind=wx.ITEM_NORMAL)
        wx.EVT_MENU(self, wxID_EDITORFRAMEFILEMENUITEMS0,
              self.OnFilemenuitems0Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEFILEMENUITEMS1,
              self.OnFilemenuitems1Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEFILEMENUITEMS2,
              self.OnFilemenuitems2Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEFILEMENUITEMS3,
              self.OnFilemenuitems3Menu)
        wx.EVT_MENU(self, wxID_EDITORFRAMEFILEMENUITEMS4,
              self.OnFilemenuitems4Menu)

    def _init_coll_statusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.fileMenu = wx.Menu(title='')

        self.helpMenu = wx.Menu(title='')

        self.mainMenuBar = wx.MenuBar()

        self.itemMenu = wx.Menu(title='')

        self._init_coll_fileMenu_Items(self.fileMenu)
        self._init_coll_helpMenu_Items(self.helpMenu)
        self._init_coll_mainMenuBar_Menus(self.mainMenuBar)
        self._init_coll_itemMenu_Items(self.itemMenu)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDITORFRAME, name=u'EditorFrame',
              parent=prnt, pos=wx.Point(117, 109), size=wx.Size(437, 296),
              style=wx.DEFAULT_FRAME_STYLE, title=u'crontab.txt Editor')
        self._init_utils()
        self.SetClientSize(wx.Size(429, 269))
        self.SetMenuBar(self.mainMenuBar)
        wx.EVT_CLOSE(self, self.OnEditorFrameClose)

        self.cronItemList = wx.ListCtrl(id=wxID_EDITORFRAMECRONITEMLIST,
              name=u'cronItemList', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(429, 230), style=wx.LC_REPORT,
              validator=wx.DefaultValidator)
        self.cronItemList.SetToolTipString(u'double-click on an entry to edit')
        wx.EVT_LEFT_DCLICK(self.cronItemList, self.OnCronitemlistLeftDclick)
        wx.EVT_LIST_ITEM_SELECTED(self.cronItemList, wxID_EDITORFRAMECRONITEMLIST,
              self.OnCronitemlistListItemSelected)

        self.statusBar = wx.StatusBar(id=wxID_EDITORFRAMESTATUSBAR,
              name=u'statusBar', parent=self, style=0)
        self.statusBar.SetPosition(wx.Point(0, 230))
        self.statusBar.SetSize(wx.Size(429, 20))
        self._init_coll_statusBar_Fields(self.statusBar)
        self.SetStatusBar(self.statusBar)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.crontab = crontab.Crontab()
        try:
            self.crontab.open()
        except IOError:
            pass
        self.setTitleFromFilename()
        self.currentItem = 0
        self.populateList()

    def setListItemBackgroundColour(self, itemNumber):
        item = self.cronItemList.GetItem(itemNumber)
        if itemNumber % 2:
            item.SetBackgroundColour("light blue")
        else:
            item.SetBackgroundColour("white")
        self.cronItemList.SetItem(item)

    def insertItemIntoList(self, currentItem, lineNumber, minute, hour, day, month, dow, command, parameters):
        self.cronItemList.InsertStringItem(currentItem, str(lineNumber))
        paramString = ""
        if len(parameters) > 0:
            paramString = " " + parameters
        self.changeListItem(currentItem, minute, hour, day, month, dow, command + paramString)
        self.setListItemBackgroundColour(currentItem)
        return currentItem + 1

    def populateList(self):
        self.clearCronItemList()
        lineNumbers = self.crontab.getLineNumbers()
        lineNumbers.sort()
        currentItem = 0
        for lineNumber in lineNumbers:
            minute, hour, day, month, dow, command, parameters  = self.crontab.getItem(lineNumber)
            currentItem = self.insertItemIntoList(currentItem, lineNumber, minute, hour, day, month,
                                                  dow, command, parameters)

        self.changeListColumnWidth(NUMBER_OF_COLUMNS)

    def clearCronItemList(self):
        self.cronItemList.ClearAll()
        self.addColumnsToList()

    def addColumnsToList(self):
        columnItems = listColumns.items()
        for x in range(len(columnItems)):
            key, label = columnItems[x]
            self.cronItemList.InsertColumn(key, label)

    def changeListColumnWidth(self, length):
        for columnNo in range(length):
            self.cronItemList.SetColumnWidth(columnNo, wx.LIST_AUTOSIZE_USEHEADER)

    def changeListItem(self, index, minute, hour, day, month, dow, taskString):
        self.cronItemList.SetStringItem(index, 1, minute)
        self.cronItemList.SetStringItem(index, 2, hour)
        self.cronItemList.SetStringItem(index, 3, day)
        self.cronItemList.SetStringItem(index, 4, month)
        self.cronItemList.SetStringItem(index, 5, dow)
        self.cronItemList.SetStringItem(index, 6, taskString.strip())

    def setTitleFromFilename(self):
        if self.crontab.filename is not None:
            title = u"%s - %s" % (FRAME_TITLE, self.crontab.filename)
            if self.crontab.changed:
                title += " *"
        else:
            title = FRAME_TITLE
        self.SetTitle(title)

    def changeItem(self, itemKey):
        dlg = taskDialog.TaskDialog(self)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                minute, hour, day, month, dow, command, parameters  = self.crontab.getItem(itemKey)
                taskString = command + " " + parameters
                self.changeListItem(self.currentItem, minute, hour, day, month, dow, taskString)
                self.changeListColumnWidth(NUMBER_OF_COLUMNS)
                self.setTitleFromFilename()
        finally:
            dlg.Destroy()

    def OnCronitemlistLeftDclick(self, event):
        if len(self.crontab) > 0:
            itemKey = int(self.cronItemList.GetItemText(self.currentItem))
            self.changeItem(itemKey)

    def showError(self, msg, title):
        dlg = wx.MessageDialog(self, msg, title, wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def showNotSavedDialog(self, event, title):
        result = True
        if self.crontab.changed:
            dlg = wx.MessageDialog(self, "Save changes to the current file?", title, wx.YES | wx.NO | wx.CANCEL)
            dlgResult = dlg.ShowModal()
            if dlgResult == wx.ID_YES:
                self.OnFilemenuitems1Menu(event) #call Save
            elif dlgResult == wx.ID_CANCEL:
                result = False
            dlg.Destroy()
        return result

    def openCrontabFile(self):
        self.setTitleFromFilename()
        try:
            self.crontab.open()
        except crontab.pycron.InvalidLineException, e:
            msg = "Error in file %s - line number: %s" % (self.crontab.filename, e.value)
            title = "Unable to load file"
            self.showError(msg, title)
            return
        except IOError, e:
            msg = str(e)
            title = "Unable to load file"
            self.showError(msg, title)
            return
        self.populateList()

    def OnFilemenuitems0Menu(self, event): #Open
        #dlg = wxFileDialog(self, "Choose a log file", ".", "", "Log files (*.log)|*.log;*.log.*|All files (*)|*", wxOPEN)
        dlg = wx.FileDialog(self, "Choose a crontab file", ".", "", "Crontab (crontab.txt)|crontab.txt|All files (*)|*", wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                self.currentItem = 0
                self.crontab.filename = filename
                self.openCrontabFile()
        finally:
            dlg.Destroy()

    def OnFilemenuitems1Menu(self, event): #Save
        if self.crontab.filename == None:
            return self.OnFilemenuitems2Menu(event)
        else:
            self.crontab.saveFile()
            self.currentItem = 0
            self.openCrontabFile() #reload file because file numbers could have changed
        return None

    def OnFilemenuitems2Menu(self, event): #Save As
        dlg = wx.FileDialog(self, "Save file as", ".", "", "*.*", wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                self.crontab.filename = filename
                self.crontab.saveFile()
                self.setTitleFromFilename()
        finally:
            dlg.Destroy()

    def OnFilemenuitems3Menu(self, event): #Close
        if not self.showNotSavedDialog(event, "Close file"):
            return
        self.currentItem = 0
        self.clearCronItemList()
        self.crontab.close()
        self.SetTitle(FRAME_TITLE)

    def OnFilemenuitems4Menu(self, event): #Exit
        if not self.showNotSavedDialog(event, "Save changes"):
            return
        self.Close()

    def OnHelpmenuitems0Menu(self, event): #About
        dlg = aboutDialog.AboutDialog(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnCronitemlistListItemSelected(self, event):
        self.currentItem = event.m_itemIndex

    def OnItemMenuItems0Menu(self, event): #New
        newKey = self.crontab.newItem()
        self.cronItemList.Select(self.currentItem, 0)
        self.currentItem = self.insertItemIntoList(self.cronItemList.GetItemCount(), newKey, "*", "*",
                                               "*", "*", "*", "", "") - 1
        self.cronItemList.Select(self.currentItem)
        self.changeItem(newKey)

    def OnItemMenuItems1Menu(self, event): #Change
        return self.OnCronitemlistLeftDclick(event)

    def OnItemMenuItems2Menu(self, event): #Delete
        if len(self.crontab) > 0:
            itemKey = int(self.cronItemList.GetItemText(self.currentItem))
            self.crontab.deleteItem(itemKey)
            self.cronItemList.DeleteItem(self.currentItem)
            self.setTitleFromFilename()
            if self.currentItem >= self.cronItemList.GetItemCount():
                self.currentItem = self.cronItemList.GetItemCount()-1
            self.cronItemList.Select(self.currentItem)
            self.recolorList()

    def recolorList(self):
        for i in xrange(self.cronItemList.GetItemCount()):
            self.setListItemBackgroundColour(i)

    def OnEditorFrameClose(self, event):
        if not self.showNotSavedDialog(event, "Save changes"):
            return
        event.Skip()
