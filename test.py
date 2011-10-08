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

import os, sys, time

prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
f = open(prgpath + "\\testcron.txt", "ab")
f.write("-"*80 + "\n")
f.write("time: %s\n" % time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time())))
f.write("parameters: %s\n" % sys.argv)
f.write("-"*80 + "\n")
