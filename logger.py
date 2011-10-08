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

import logging

import loghandlers


LOGGING_LEVEL = logging.INFO
MAX_FILESIZE = 102400

class Logger(object):
    """ Logger class that locks the log file and closes the log file after each log """
    handlers = {} # one handler for each logger name

    def __init__(self, filename, name=None, level=LOGGING_LEVEL,
                 format="%(asctime)s %(levelname)-5s: %(message)s",
                 dateformat="%Y-%m-%d %H:%M",
                 max_filesize = MAX_FILESIZE):
        self.name = name
        self.filename = filename
        logging.basicConfig()
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(level)
        if not self.name in Logger.handlers:
            handler = loghandlers.RotatingFileHandler(self.filename,
                                "a", max_filesize, 2)
            Logger.handlers[self.name] = handler
            formatter = logging.Formatter(format, dateformat)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)


class NullLogger(object):

    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def critical(self, msg):
        pass

    def exception(self, msg):
        pass
