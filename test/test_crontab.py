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

import unittest
import os
import sys

sys.path.append("..")

import crontab

class CrontabTestCase(unittest.TestCase):
    def check_open(self):
        """ open """
        f = open("abc.txt", "wb")
        f.write("this is a bad line\n")
        f.close()
        c = crontab.Crontab()
        c.filename = "abc.txt"
        self.assertRaises(crontab.pycron.InvalidLineException, c.open)
        os.remove("abc.txt")
        self.assertRaises(IOError, c.open)
    def check_getItem(self):
        """ getItem """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        for lineNumber in c.getLineNumbers():
            item = c.getItem(lineNumber)
            self.assertEqual(len(item), 7)
    def check_getLineNumbers(self):
        """ getLineNumbers """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        assert c.getLineNumbers() > 0
    def check_newItem(self):
        """ newItem """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        lineNumber = c.newItem()
        assert lineNumber > 0
        self.assertEqual(len(c.getItem(lineNumber)), 7)
    def check_deleteItem(self):
        """ deleteItem """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        lineNumber = c.newItem()
        c.deleteItem(lineNumber)
        self.assertRaises(KeyError, c.getItem, lineNumber)
    def check_changeItem(self):
        """ changeItem """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        lineNumber = c.newItem()
        c.changeItem(lineNumber, "1", "2", "3", "4", "5", "cmd", "parameters")
        self.assertEqual(c.getItem(lineNumber), ("1", "2", "3", "4", "5", "cmd", "parameters"))
    def check_changed(self):
        """ changed """
        c = crontab.Crontab()
        c.filename = os.path.join("..", os.path.basename(c.filename) + ".sample")
        c.open()
        self.assertEqual(c.changed, False)
        lineNumber = c.getLineNumbers()[0]
        item = c.getItem(lineNumber)
        c.changeItem(lineNumber, *item) #same values --> no change
        self.assertEqual(c.changed, False)
        c.changeItem(lineNumber, *c.getItem(c.newItem()))
        self.assertEqual(c.changed, True)

def makeTestSuite():
    return unittest.makeSuite(CrontabTestCase, "check")

def suite():
    return makeTestSuite()

if __name__ == "__main__":
    unittest.main(defaultTest = "suite")
