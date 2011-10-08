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

from distutils.core import setup
import py2exe
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

cronService = dict(
    modules = ["pycron"],
    icon_resources = [(0, "pycron.ico"),]
    )

includes = ["encodings.*",
           ]

excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "perfmon", "ctypes",
            "email", "EasyDialogs", ]

setup(
    options = {"py2exe": {#"compressed": 1, --> setup is smaller if files are not compressed!
                          "optimize": 2
                          ,"includes": includes
                          ,"excludes": excludes
                         }},
    zipfile = "shared.zip",
    service = [cronService],
    version='0.5.9.1',
    description="A cron service written in Python",
    windows = [{"script": "pyCronEditor.py",
                "icon_resources": [(1, "pycron.ico")]
               }],
    console = [{"script": "pycron.py",
                "icon_resources": [(1, "pycron.ico")],
                "dest_base": "pycron_console"
               }],
    )
