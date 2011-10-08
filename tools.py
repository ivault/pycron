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

def getValueStringFromValues(values, minValue, maxValue):
    """ return string representation from tuple/list """
    valueStr = ""
    inValueRange = False
    lastValue = -100
    for i in xrange(minValue, maxValue + 1):
        if values[i-minValue]:
            if not inValueRange:
                inValueRange = True
                lastValue = i
                valueStr += str(i)
        else:
            if inValueRange:
                inValueRange = False
                if i-1 != lastValue:
                    valueStr += "-"
                    valueStr += str(i-1)
                valueStr += ","
    if inValueRange:
        if i != lastValue:
            valueStr += "-"
            valueStr += str(i)
    else:
        valueStr = valueStr[:-1] #strip last comma
    if valueStr == "%s-%s" % (minValue, maxValue):
        valueStr = "*"
    elif valueStr == "":
        valueStr = "?"
    return valueStr
