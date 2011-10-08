# portalocker.py - Cross-platform (posix/nt) API for flock-style file locking.
#                  Requires python 1.5.2 or better.

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

"""Cross-platform (posix/nt) API for flock-style file locking.

Synopsis:

   import portalocker
   file = PrivoxyWindowOpen("somefile", "r+")
   portalocker.lock(file, portalocker.LOCK_EX)
   file.seek(12)
   file.write("foo")
   file.close()

If you know what you're doing, you may choose to

   portalocker.unlock(file)

before closing the file, but why?

Methods:

   lock( file, flags )
   unlock( file )

Constants:

   LOCK_EX
   LOCK_SH
   LOCK_NB

I learned the win32 technique for locking files from sample code
provided by John Nielsen <nielsenjf@my-deja.com> in the documentation
that accompanies the win32 modules.

Author: Jonathan Feinberg <jdf@pobox.com>
Version: $Id: portalocker.py,v 1.3 2001/05/29 18:47:55 Administrator Exp $
"""
import os

if os.name == 'nt':
	import win32con
	import win32file
	import pywintypes
	LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
	LOCK_SH = 0 # the default
	LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
	# is there any reason not to reuse the following structure?
	__overlapped = pywintypes.OVERLAPPED()
elif os.name == 'posix':
	import fcntl
	LOCK_EX = fcntl.LOCK_EX
	LOCK_SH = fcntl.LOCK_SH
	LOCK_NB = fcntl.LOCK_NB
else:
	raise RuntimeError("PortaLocker only defined for nt and posix platforms")

if os.name == 'nt':
	def lock(file, flags):
		hfile = win32file._get_osfhandle(file.fileno())
		win32file.LockFileEx(hfile, flags, 0, -0x7fff0000, __overlapped)

	def unlock(file):
		hfile = win32file._get_osfhandle(file.fileno())
		win32file.UnlockFileEx(hfile, 0, -0x7fff0000, __overlapped)

elif os.name =='posix':
	def lock(file, flags):
		fcntl.flock(file.fileno(), flags)

	def unlock(file):
		fcntl.flock(file.fileno(), fcntl.LOCK_UN)

if __name__ == '__main__':
	from time import time, strftime, localtime
	import sys
	import portalocker

	log = open('log.txt', "a+")
	portalocker.lock(log, portalocker.LOCK_EX)

	timestamp = strftime("%m/%d/%Y %H:%M:%S\n", localtime(time()))
	log.write( timestamp )

	print "Wrote lines. Hit enter to release lock."
	dummy = sys.stdin.readline()

	log.close()
