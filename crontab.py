# coding: iso-8859-1

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

# Crontab class for loading, saving, changing, deleting crontab entries

import sys, os

import pycron

class Crontab:
    def __init__(self):
        self._clearMembers()
        prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.filename = prgpath + os.sep + "crontab.txt"
        #self.open()

    def __len__(self):
        return len(self.itemDict)

    def _clearMembers(self):
        self.itemDict = {}
        self.cronFileLines = ()
        self.deletedItems = {}
        self.lastNewItemKey = 0
        self.changed = False

    def _readCronFile(self):
        self.cronFileLines = open(self.filename, "rb").readlines()
        cronFile = pycron.Cronfile(self.filename)
        self.lastNewItemKey = len(self.cronFileLines) # no new items yet
        for line in cronFile.lines:
            self._insertItemIntoDict(line.lineno, line.minute, line.hour,
                                    line.day, line.month, line.dow, line.command, line.parameters)

    def _insertItemIntoDict(self, lineNumber, minute, hour, day, month, dow, command, parameters):
        paramString = ""
        if parameters is not None:
            paramString = " ".join(parameters)
        self.itemDict[lineNumber] = (minute, hour, day, month, dow, command, paramString.strip())

    def getItem(self, itemKey):
        return self.itemDict[itemKey]

    def open(self):
        self._clearMembers()
        self._readCronFile()

    def getLineNumbers(self):
        return self.itemDict.keys()

    def _writeItem(self, f, lineno):
        minute, hour, day, month, dow, command, parameters  = self.itemDict[lineno]
        f.write('%s %s %s %s %s "%s" %s\n' %(minute, hour, day, month, dow, command, parameters))

    def saveFile(self):
        lines = self.cronFileLines
        f = open(self.filename, "wb")

        line_continues = False
        lineno = 1
        # check for line continuation characters r" \"
        for i in range(len(lines)):
            if lineno in self.itemDict:
                self._writeItem(f, lineno)
                if lines[i].strip().endswith(" \\"):
                    if not line_continues:
                        line_continues = True
            elif lineno in self.deletedItems:
                del self.deletedItems[lineno]
            else:
                if line_continues:
                    if not lines[i].strip().endswith(" \\"):
                        line_continues = False
                else:
                    f.write(lines[i])
            lineno += 1
        for lineno in range(len(self.cronFileLines) + 1, self.lastNewItemKey + 1):
            if lineno in self.itemDict:
                self._writeItem(f, lineno)
        f.close()
        self._clearMembers()
        self._readCronFile() #reload file because file numbers could have changed

    def close(self):
        self._clearMembers()
        self.filename = None

    def newItem(self):
        self.lastNewItemKey += 1
        self._insertItemIntoDict(self.lastNewItemKey, "*", "*", "*", "*", "*", "", "")
        self.changed = True
        return self.lastNewItemKey

    def deleteItem(self, itemKey):
        if len(self.itemDict) > 0:
            self.deletedItems[itemKey] = self.itemDict[itemKey]
            del self.itemDict[itemKey]
            self.changed = True

    def changeItem(self, itemKey, minute, hour, day, month, dow, command, parameters):
        newValues = (minute, hour, day, month, dow, command, parameters)
        if itemKey in self.itemDict:
            if self.itemDict[itemKey] == newValues:
                return
        self.itemDict[itemKey] = newValues
        self.changed = True
