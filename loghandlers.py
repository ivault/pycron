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

import os
import sys
import logging

import portalocker


class LockingFileHandler(logging.StreamHandler):
    """
    A handler class which writes formatted logging records to disk files.
    """
    import servicemanager
    def __init__(self, filename, mode="a"):
        """
        Open the specified file and use it as the stream for logging.
        """
        logging.StreamHandler.__init__(self, open(filename, mode))
        #keep the absolute path, otherwise derived classes which use this
        #may come a cropper when the current directory changes
        self.baseFilename = os.path.abspath(filename)
        self.mode = mode

    def close(self):
        """
        Closes the stream.
        """
        self.flush()
        self.stream.close()
        logging.StreamHandler.close(self)

    def emit(self, record):
        self.stream = open(self.baseFilename, self.mode)
        portalocker.lock(self.stream, portalocker.LOCK_EX)
        logging.StreamHandler.emit(self, record)
        self.stream.close()

    def handleError(self, record):
        """
        Handle errors which occur during an emit() call.

        sys.stderr does nowwhere, so redirect this into the event log.
        """
        if logging.raiseExceptions:
            import StringIO
            import traceback
            ei = sys.exc_info()
            msg = StringIO.StringIO()
            traceback.print_exception(ei[0], ei[1], ei[2], None, msg)
            msg.seek(0)
            self.servicemanager.LogErrorMsg(msg.getvalue())
            del ei

class BaseRotatingHandler(LockingFileHandler):
    """
    Base class for handlers that rotate log files at a certain point.
    Not meant to be instantiated directly.  Instead, use RotatingFileHandler
    or TimedRotatingFileHandler.
    """
    def __init__(self, filename, mode):
        """
        Use the specified filename for streamed logging
        """
        LockingFileHandler.__init__(self, filename, mode)

    def emit(self, record):
        """
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            LockingFileHandler.emit(self, record)
        except:
            self.handleError(record)


class RotatingFileHandler(BaseRotatingHandler):
    """
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size.
    """
    def __init__(self, filename, mode="a", maxBytes=0, backupCount=0):
        """
        Open the specified file and use it as the stream for logging.

        By default, the file grows indefinitely. You can specify particular
        values of maxBytes and backupCount to allow the file to rollover at
        a predetermined size.

        Rollover occurs whenever the current log file is nearly maxBytes in
        length. If backupCount is >= 1, the system will successively create
        new files with the same pathname as the base file, but with extensions
        ".1", ".2" etc. appended to it. For example, with a backupCount of 5
        and a base file name of "app.log", you would get "app.log",
        "app.log.1", "app.log.2", ... through to "app.log.5". The file being
        written to is always "app.log" - when it gets filled up, it is closed
        and renamed to "app.log.1", and if files "app.log.1", "app.log.2" etc.
        exist, then they are renamed to "app.log.2", "app.log.3" etc.
        respectively.

        If maxBytes is zero, rollover never occurs.
        """
        self.mode = mode
        if maxBytes > 0:
            self.mode = "a" # doesn't make sense otherwise!
        BaseRotatingHandler.__init__(self, filename, self.mode)
        self.maxBytes = maxBytes
        self.backupCount = backupCount

    def doRollover(self):
        """
        Do a rollover, as described in __init__().
        """

        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d" % (self.baseFilename, i)
                dfn = "%s.%d" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.chmod(dfn, 07777)
                        os.remove(dfn)
                    os.rename(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.chmod(dfn, 07777)
                os.remove(dfn)
            os.rename(self.baseFilename, dfn)

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        """
        result = False
        if self.maxBytes > 0:                   # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream = open(self.baseFilename, "rb")
            self.stream.seek(0, 2)  #due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                result = True
            self.stream.close()
        return result
