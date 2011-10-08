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

"""
PyCron

Copyright 2003-2007 Gerhard Kalab

"""
__author__ = "Gerhard Kalab"
__email__ = "kalab@gmx.net"
__version__ = "0.5.9"
__revision__ = "$Rev: 698 $"

# system modules
import os
import sys
import time
import csv
import threading
import re
import win32api, pywintypes
import win32serviceutil, win32service
import cStringIO
import traceback
import ConfigParser
import subprocess
import datetime

if sys.version_info[:2] == (2, 3):
    from sets import Set as set # for python 2.3

import logger

# enable the following line for debugging information
#logger.LOGGING_LEVEL = logger.logging.DEBUG

prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
SETTINGS_FILENAME = os.path.join(prgpath, "pycron.cfg")
DATA_FILENAME = os.path.join(prgpath, "pycron.dat")


def adjust_dow(dow, old_dow_compatibility):
    """ adjust weekday from python to unix weekday format """
    if old_dow_compatibility:
        return dow
    new_dow = dow + 1
    if new_dow >= 7:
        new_dow = 0
    return new_dow

def replace_alphanumerics(value):
    """ replace a month or weekday name with the corresponding int value """
    result = value
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November",
                   "December"]
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]
    for month in month_names:
        if month.upper().startswith(value.upper()):
            return month_names.index(month) + 1
    for day in weekdays:
        if day.upper().startswith(value.upper()):
            return weekdays.index(day)
    return int(result)


class PyCronLogger(logger.Logger):
    filename = None

    def __init__(self):
        if PyCronLogger.filename is None:
            config = ConfigParser.ConfigParser()
            try:
                config.read(SETTINGS_FILENAME)
                PyCronLogger.filename = config.get("pycron", "log_filename")
            except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
                pass # ignore any config file errors
            if PyCronLogger.filename is None:
                PyCronLogger.filename = os.path.join(prgpath, "pycron.log")
        logger.Logger.__init__(self, name="pycron",
            filename=os.path.abspath(os.path.join(prgpath,
                                     PyCronLogger.filename)))


class SpaceDialect(csv.excel):
    """ a csv dialect with a space delimiter """
    delimiter = " "


class InvalidLineException(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value


class Job(threading.Thread):
    """ run system commands or python scripts """

    def __init__(self, command, parameters, missed):
        threading.Thread.__init__(self)
        self.command = os.path.abspath(command)
        self.parameters = parameters
        self.runnable = False
        self.missed = missed
        self.result = -1
        self.log = PyCronLogger()
        try:
            # os.system doesn't work well with long file names
            # and parameter file names with spaces
            self.shortCommand = win32api.GetShortPathName(self.command)
        except pywintypes.error, e:
            self.log.error("'%s' - %s" % (command, e[2]))
            return
        self.runnable = True

    def run(self):
        if self.runnable:
            if self.missed:
                logstr = "executing missed task '%s'" % self.command
            else:
                logstr = "executing '%s" % self.command
            if self.parameters is None:
                paramstr = ""
            else:
                paramstr = " " + " ".join(self.parameters)
            logstr += paramstr + "'"
            try:
                pid = None
                if self.shortCommand.upper().endswith(".PY"):
                    self.log.info("start " + logstr)
                    self.result = self.execute_python()
                else:
                    process = subprocess.Popen(self.shortCommand + paramstr)
                    self.log.info("start (pid=%s) %s" % (process.pid, logstr))
                    pid = process.pid
                    process.wait()
                    self.result = process.returncode
                if pid is not None:
                    self.log.info("stop (pid=%s) %s, rc=%s" % (pid, logstr, self.result))
                else:
                    self.log.info("stop %s, rc=%s" % (logstr, self.result))
            except OSError, e:
                self.log.error("'%s' - %s" % (self.command, e))

    def execute_python(self):
        result = 0
        saved_args = sys.argv # save arguments
        sys.argv = [self.command]
        if len(self.parameters) > 0:
            sys.argv += self.parameters
        global_dict = {"sys":dir(sys)}
        try:
            if os.path.exists(self.command):
                execfile(self.command, global_dict)
            else:
                self.log.error("'%s' - %s" % (self.command, "does not exist"))
                result = -1
        except SystemExit:
            result = sys.exc_info()[1]
        except:
            self.log.exception("'%s' - exception" % self.command)
            result = -1
        sys.argv = saved_args # restore arguments
        return result


class Matcher(object):

    def __init__(self, timestr, lineno):
        self.timestr = timestr
        self.lineno = lineno
        self.minval = 0
        self.maxval = 0

    def matches(self, timeval, startup_timeval):
        result = False
        if self.timestr == "*":
            return True
        elif self.timestr == "?":
            if timeval == startup_timeval:
                return True
            else:
                return False
        values = self.timestr.split(",")
        try:
            for value in values:
                if value.find("-") >= 0:
                    result = self._process_match_range(value, timeval)
                elif value.find("/") >= 0:
                    result = self._process_match_devider(value, timeval)
                else:
                    value = replace_alphanumerics(value)
                    if value < self.minval or value > self.maxval:
                        raise InvalidLineException, self.lineno
                    elif timeval == value:
                        result = True
                if result:
                    return result
        except ValueError:
            raise InvalidLineException, self.lineno
        return result

    def _process_match_range(self, value, timeval):
        result = False
        valrange = []
        from_value, to_value = value.split("-")
        from_value = replace_alphanumerics(from_value)
        if to_value.find("/") >= 0:
            to_value, step = to_value.split("/")
            valrange = range(from_value,
                             replace_alphanumerics(to_value)+1,
                             int(step))
        to_value = replace_alphanumerics(to_value)
        if from_value < self.minval or from_value > self.maxval or to_value < self.minval or \
           to_value > self.maxval or to_value <= from_value:
            raise InvalidLineException, self.lineno
        if timeval in valrange:
            result = True
        elif len(valrange)==0 and from_value <= timeval and timeval <= to_value:
            result = True
        return result

    def _process_match_devider(self, value, timeval):
        result = False
        valrange = []
        value, step = value.split("/")
        if value != "*":
            raise InvalidLineException, self.lineno
        valrange = range(self.minval, self.maxval+1, int(step))
        if timeval in valrange:
            result = True
        return result


class MinuteMatcher(Matcher):

    def __init__(self, timestr, lineno):
        Matcher.__init__(self, timestr, lineno)
        self.minval = 0
        self.maxval = 59

    def matches(self, date, startup_date):
        return Matcher.matches(self, date.minute, startup_date.minute)


class HourMatcher(Matcher):

    def __init__(self, timestr, lineno):
        Matcher.__init__(self, timestr, lineno)
        self.minval = 0
        self.maxval = 23

    def matches(self, date, startup_date):
        return Matcher.matches(self, date.hour, startup_date.hour)


class DayMatcher(Matcher):

    def __init__(self, timestr, lineno):
        Matcher.__init__(self, timestr, lineno)
        self.minval = 1
        self.maxval = 31

    def matches(self, date, startup_date):
        return Matcher.matches(self, date.day, startup_date.day)


class MonthMatcher(Matcher):

    def __init__(self, timestr, lineno):
        Matcher.__init__(self, timestr, lineno)
        self.minval = 1
        self.maxval = 12

    def matches(self, date, startup_date):
        return Matcher.matches(self, date.month, startup_date.month)


class DayOfWeekMatcher(Matcher):

    def __init__(self, timestr, lineno, old_dow_compatibility):
        Matcher.__init__(self, timestr, lineno)
        self.old_dow_compatibility = old_dow_compatibility
        self.minval = 0
        self.maxval = 6

    def matches(self, date, startup_date):
        dow = adjust_dow(date.weekday(), self.old_dow_compatibility)
        start_dow = adjust_dow(startup_date.weekday(), self.old_dow_compatibility)
        return Matcher.matches(self, dow, start_dow)


class CompositeMatcher(object):

    def __init__(self):
        self.matchers = []

    def add(self, matcher):
        self.matchers.append(matcher)

    def matches(self, date, startup_date):
        result = True
        for matcher in self.matchers:
            if not matcher.matches(date, startup_date):
                result = False
                break
        return result


class Parser(object):

    def __init__(self, lineno):
        self.lineno = lineno

    def compare(self, currenttime, cronstartup,
                (str_minute, str_hour, str_day, str_month, str_dow),
                old_dow_compatibility):
        result = False
        cmatcher = CompositeMatcher()
        cmatcher.add(MinuteMatcher(str_minute, self.lineno))
        cmatcher.add(HourMatcher(str_hour, self.lineno))
        cmatcher.add(DayMatcher(str_day, self.lineno))
        cmatcher.add(MonthMatcher(str_month, self.lineno))
        cmatcher.add(DayOfWeekMatcher(str_dow, self.lineno, old_dow_compatibility))
        if cmatcher.matches(currenttime, cronstartup):
            return True
        return result


class MissedTaskParser(object):

    def __init__(self, lineno):
        self.lineno = lineno

    def _get_all_values_in_range(self, down_timeval, startup_timeval, minval, maxval):
        result = {}
        if startup_timeval < down_timeval:
            result[0] = range(down_timeval, maxval + 1)
            result[1] = range(minval, startup_timeval + 1)
        else:
            result[0] = range(down_timeval, startup_timeval + 1)
        return result

    def _values_from_range(self, start, end, step, ismonth, down_timeval, startup_timeval, minval, maxval):
        valrange = range(start, end, step)
        if ismonth:
            all_values = self._get_all_values_in_range(down_timeval, startup_timeval, minval, maxval)
            result = {}
            for year_adjust in all_values.keys():
                result_per_year = []
                for value in all_values[year_adjust]:
                    if value in valrange:
                        result_per_year.append(value)
                result[year_adjust] = result_per_year
            valrange = [result]
        return valrange

    def _process_devider(self, value, minval, maxval, down_timeval, startup_timeval, ismonth):
        value, step = value.split("/")
        if value != "*":
            raise InvalidLineException, self.lineno
        return self._values_from_range(minval, maxval+1, int(step), ismonth, down_timeval, startup_timeval, minval, maxval)

    def _process_range(self, value, minval, maxval, down_timeval, startup_timeval, ismonth):
        from_value, to_value = value.split("-")
        from_value = replace_alphanumerics(from_value)
        step = 1
        if to_value.find("/") >= 0:
            to_value, step = to_value.split("/")
        to_value = replace_alphanumerics(to_value)
        if from_value < minval or from_value > maxval or to_value < minval or \
           to_value > maxval or to_value <= from_value:
            raise InvalidLineException, self.lineno
        return self._values_from_range(from_value, to_value+1, int(step), ismonth, down_timeval, startup_timeval, minval, maxval)

    def valrange(self, down_timeval, startup_timeval, timestr, minval, maxval, ismonth=False):
        result = []
        if timestr == "*":
            if ismonth:
                result.append((self._get_all_values_in_range(down_timeval, startup_timeval, minval, maxval)))
            else:
                result = range(minval, maxval + 1)
            return result
        elif timestr == "?":
            return result
        values = timestr.split(",")
        try:
            for value in values:
                if value.find("-") >= 0:
                    result += self._process_range(value, minval,
                                              maxval, down_timeval, startup_timeval, ismonth)
                elif value.find("/") >= 0:
                    result += self._process_devider(value, minval,
                                              maxval, down_timeval, startup_timeval, ismonth)
                else:
                    value = replace_alphanumerics(value)
                    if value < minval or value > maxval:
                        raise InvalidLineException, self.lineno
                    else:
                        result += self._values_from_range(value, value+1, 1, ismonth,
                                        down_timeval, startup_timeval, minval, maxval)
        except ValueError:
            raise InvalidLineException, self.lineno
        return result

    def make_dates(self, down_time, startup_time,
                   (str_minute, str_hour, str_day, str_month, str_dow),
                   old_dow_compatibility):
        month_values = self.valrange(down_time.month, startup_time.month, str_month, 1, 12, ismonth=True)
        days = self.valrange(down_time.day, startup_time.day, str_day, 1, 31)
        hours = self.valrange(down_time.hour, startup_time.hour, str_hour, 0, 23)
        minutes = self.valrange(down_time.minute, startup_time.minute, str_minute, 0, 59)
        down_weekday = adjust_dow(down_time.weekday(), old_dow_compatibility)
        startup_weekday = adjust_dow(startup_time.weekday(), old_dow_compatibility)
        daysofweek = self.valrange(down_weekday, startup_weekday, str_dow, 0, 6)
        dates = set() # a set to filter multiple dates
        if len(month_values) == 0 or len(days) == 0 or len(hours) == 0 or len(minutes) == 0 or len(daysofweek) == 0:
            return dates
        for months in month_values:
            for year_adjust in months.keys():
                for month in months[year_adjust]:
                    for day in days:
                        for hour in hours:
                            for minute in minutes:
                                for dow in daysofweek:
                                    try:
                                        new_date = datetime.datetime(down_time.year + year_adjust,
                                                                     month, day, hour, minute)
                                        if dow == adjust_dow(new_date.weekday(), old_dow_compatibility):
                                            dates.add(new_date)
                                    except ValueError:
                                        pass # don't create invalid dates
        for date in dates.copy():
            if date <= down_time or date >= startup_time:
                dates.remove(date)
        return dates


class Cronline:

    def __init__(self, line, lineno):
        self.line = line
        self.lineno = lineno
        self.missedTask = None
        parseline = line.replace('!"', '! "') # csv parser chokes on ! or * in front of " (e.g. !" or *")
        parseline = parseline.replace('*"', '* "')
        csv.register_dialect("SpaceDialect", SpaceDialect)
        parser = csv.reader([parseline], "SpaceDialect")
        words = parser.next()
        for item in words[:]:
            if item == "":
                words.remove(item)
        if len(words)<6:
            raise InvalidLineException, self.lineno
        if words[5] == "!" or words[5] == "*":
            self.missedTask = words[5]
            del words[5]
        self.minute, self.hour, self.day, self.month, self.dow = words[:5]
        self.command = self._parse_env_vars(words[5])
        if self.command.startswith("!") or self.command.startswith("*"):
            self.missedTask = self.command[0]
            self.command = self.command[1:]
        self.parameters = None
        if len(words)>6:
            self.parameters = []
            for parameter in words[6:]:
                if len(parameter.split())>1:
                    self.parameters += ['"%s"' % self._parse_env_vars(parameter)]
                else:
                    self.parameters += [self._parse_env_vars(parameter)]

    def _parse_env_vars(self, cmdline):
        compile_obj = re.compile("%.*?%")
        found_variables = compile_obj.findall(cmdline)
        split_matchstr = compile_obj.split(cmdline)
        return self._replace_env_variables(split_matchstr, found_variables)

    def _replace_env_variables(self, split_matchstr, found_variables):
        result = ""
        index = 0
        while index < len(split_matchstr):
            if index < len(found_variables):
                env_name = found_variables[index][1:-1]
                if env_name in os.environ:
                    env_value = os.environ[env_name]
                    result += split_matchstr[index] + env_value
                else:
                    result += split_matchstr[index] + found_variables[index]
            else:
                result += split_matchstr[index]
            index += 1
        return result

    def __repr__(self):
        return "'" + self.line + "'"

    def checktime(self, currenttime, cronstartup, old_dow_compatibility=False):
        parser = Parser(self.lineno)
        return parser.compare(currenttime, cronstartup,
                    (self.minute, self.hour, self.day, self.month, self.dow),
                    old_dow_compatibility)

    def execute(self, missed):
        j = Job(self.command, self.parameters, missed)
        j.start()

    def missed_tasks(self, last_shutdown, cronstartup, old_dow_compatibility):
        result = 0
        if self.missedTask is not None:
            parser = MissedTaskParser(self.lineno)
            dates = parser.make_dates(last_shutdown, cronstartup,
                                      (self.minute, self.hour, self.day, self.month, self.dow),
                                      old_dow_compatibility)
            result = len(dates)
            if result > 1 and self.missedTask == "!":
                result = 1
        return result


class Cronfile:

    def __init__(self, filename):
        self.lines = []
        self.log = PyCronLogger()
        try:
            cfile = open(filename)
        except IOError:
            self.log.critical("'%s' - %s" % (filename, "does not exist"))
            return
        lines = cfile.readlines()
        cfile.close()
        line_continues = False
        newlines = []
        lineno = 1
        # check for line continuation characters r" \"
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            if lines[i].endswith(" \\"):
                if i == len(lines)-1:
                    # line ends with separator, but it's the last line
                    raise InvalidLineException, i+1
                if line_continues:
                    newlines[len(newlines)-1][0] += lines[i][:-1]
                else:
                    line_continues = True
                    newlines.append(list((lines[i][:-1], lineno)))
            else:
                if line_continues:
                    newlines[len(newlines)-1][0] += lines[i]
                    line_continues = False
                else:
                    newlines.append(list((lines[i], lineno)))
            lineno += 1
        for line, lineno in newlines:
            pos = line.find(r"#")
            if pos >= 0:
                line = line[:pos].strip()
            if len(line)>0:
                self.lines.append(Cronline(line, lineno))


class CfgParser:

    def __init__(self, filename):
        self.config = ConfigParser.ConfigParser()
        self.filename = filename

    def _ensure_config_section(self):
        self.config.read(self.filename)
        if not self.config.has_section("pycron"):
            self.config.add_section("pycron")

    def save_startup(self, startuptime):
        self._ensure_config_section()
        self.config.set("pycron", "startup", startuptime)
        self._save_config_data()

    def _save_config_data(self):
        self.config.write(open(self.filename, "w"))

    def save_shutdown(self):
        self._ensure_config_section()
        self.config.set("pycron", "shutdown", time.time())
        self._save_config_data()

    def read_config_value(self, name):
        result = None
        config = ConfigParser.ConfigParser()
        config.read(self.filename)
        if config.has_section("pycron") and config.has_option("pycron", name):
            result = config.getfloat("pycron", name)
        return result


class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "PyCron"
    _svc_display_name_ = "Python Cron Service"

    def __init__(self, args):
        if args is not None:
            win32serviceutil.ServiceFramework.__init__(self, args)
            self.event_stopped = threading.Event()
            self.event_stopping = threading.Event()
            self.thread = None
        else:
            self.log = PyCronLogger()
            self.old_dow_compatibility = False
            self.crontab_filename = "crontab.txt"
            self.cfg_parser = CfgParser(DATA_FILENAME)

    def SvcStop(self):
        self.log.debug("SvcStop")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.event_stopping.set()
        self.cfg_parser.save_shutdown()
        self.running = False

    def SvcDoRun(self):
        # initialize some values
        self.old_dow_compatibility = False
        self.crontab_filename = "crontab.txt"
        self.cfg_parser = CfgParser(DATA_FILENAME)
        self.log = PyCronLogger()
        self.log.debug("SvcDoRun")
        import servicemanager
        try:
            self.read_configuration()
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            pass
        except ValueError:
            servicemanager.LogMsg(servicemanager.EVENTLOG_ERROR_TYPE,
                    servicemanager.PYS_SERVICE_STARTING,
                    (self._svc_name_,
                     "\n- invalid value in configuration file (ValueError)"))
            return

        # Start the thread running the server.
        thread = threading.Thread(target=self.ServerThread)
        thread.start()

        extra = " as user '%s'" % win32api.GetUserName()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, extra))
        try:
            # Thread running - wait for the stopping event.
            self.event_stopping.wait()
            # Either user requested stop, or thread done - wait for it
            # to actually stop, but reporting we are still alive.
            # Wait up to 60 seconds for shutdown before giving up and
            # exiting uncleanly - we wait for current proxy connections
            # to close, but you have to draw the line somewhere.
            for i in range(60):
                self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
                self.event_stopped.wait(1)
                if self.event_stopped.isSet():
                    break
                self.log.debug("The service is still shutting down...")
            else:
                # eeek - we timed out - give up in disgust.
                self.log.debug("The worker failed to stop - aborting it anyway")
        except KeyboardInterrupt:
            pass

        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STOPPED,
                              (self._svc_name_, ""))

    def read_configuration(self):
        self.log.debug("read_configuration")
        config = ConfigParser.ConfigParser()
        config.read(SETTINGS_FILENAME)
        self.old_dow_compatibility = config.getboolean("pycron",
                                                       "old_dow_compatibility")
        self.crontab_filename = config.get("pycron", "crontab_filename")

    def _time_to_datetime(self, t):
        if t is None:
            return datetime.datetime(*time.localtime()[:7])
        else:
            return datetime.datetime(*time.localtime(t)[:7])

    def _check_missed_tasks(self, shutdown, startup, old_dow_compatibility):
        self.log.debug("_check_missed_tasks")
        local_shutdown = self._time_to_datetime(shutdown)
        local_startup = self._time_to_datetime(startup)
        try:
            cfile = Cronfile(os.path.abspath(os.path.join(prgpath,
                             self.crontab_filename)))
            for line in cfile.lines:
                for i in range(line.missed_tasks(local_shutdown, local_startup,
                                                   old_dow_compatibility)):
                    line.execute(missed=True)
        except InvalidLineException, e:
            self.log.error("error in file '%s' line no: %s"
                      % (self.crontab_filename, e.value))

    def ServerThread(self):
        self.log.debug("ServerThread")
        try:
            try:
                self.pycron_start()
            except SystemExit:
                # user requested shutdown
                self.log.debug(self._svc_name_ + \
                    "%s service shutting down due to user request")
            except:
                # Otherwise an error we should log.
                ob = cStringIO.StringIO()
                traceback.print_exc(file=ob)

                message = "The " + self._svc_name_ + " failed with an " \
                          "unexpected error\r\n\r\n" + ob.getvalue()

                self.log.error(message)
                # Log an error event to the event log.
                import servicemanager
                servicemanager.LogErrorMsg(message)
        finally:
            self.event_stopping.set()
            self.event_stopped.set()

    def pycron_start(self):
        self.log.debug("pycron_start")
        lastchecked = None
        cronstartup = None
        self.running = True
        while self.running:
            current_time = time.time()
            if cronstartup is None:
                cronstartup = current_time
                self.cfg_parser.save_startup(current_time)
                last_shutdown = self.cfg_parser.read_config_value("shutdown")
                if last_shutdown < current_time:
                    self._check_missed_tasks(last_shutdown, current_time,
                                             self.old_dow_compatibility)
            current_local_time = time.localtime(current_time)
            if current_local_time[:5] != lastchecked:
                try:
                    lastchecked = current_local_time[:5]
                    cfile = Cronfile(os.path.abspath
                                     (os.path.join(prgpath,
                                                self.crontab_filename)))
                    self.log.debug("checking cfile")
                    for line in cfile.lines:
                        if line.checktime(self._time_to_datetime(current_time),
                                          self._time_to_datetime(cronstartup),
                                          self.old_dow_compatibility):
                            self.log.debug("before line.execute")
                            line.execute(missed=False)
                except InvalidLineException, e:
                    self.log.error("error in file '%s' line no: %s"
                              % (self.crontab_filename, e.value))
            time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        win32serviceutil.HandleCommandLine(Service)
    else:
        interactive = Service(None)
        interactive.pycron_start()
