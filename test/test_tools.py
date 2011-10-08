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
import sys

sys.path.append("..")

import tools

class ToolsTestCase(unittest.TestCase):
    def check_getValueStringFromValues(self):
        """ getValueStringFromValues """
        values = [False,True,True,False,True,True,True]
        self.assertEqual(tools.getValueStringFromValues(values, 0, 6), "1-2,4-6")

def makeTestSuite():
    return unittest.makeSuite(ToolsTestCase, "check")

def suite():
    return makeTestSuite()

if __name__ == "__main__":
    unittest.main(defaultTest = "suite")
