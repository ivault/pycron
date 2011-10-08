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
import datetime
import os
import sys

sys.path.append("..")

import pycron

class CronlineTestCase(unittest.TestCase):

    def check_parameter_with_and(self):
        """ parameter with '&' """
        line = '* * * * * "C:\\Program Files\\Mozilla Firefox\\firefox.exe" http://something.com:8000/admin.cgi?pass=password&mode=updinfo&song=something'
        cronline = pycron.Cronline(line, 1)
        self.assertEquals(cronline.command, "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.assertEquals(cronline.parameters, ["http://something.com:8000/admin.cgi?pass=password&mode=updinfo&song=something"])

    def check_longfilename(self):
        """ long file name with "..." """
        line = '* * * * * "this is a long line" foo bar'
        cronline = pycron.Cronline(line, 1)
        assert cronline.command == "this is a long line"
        assert cronline.parameters == ["foo", "bar"]
        line = '* * * * * "this is a long line" abc def "foo bar"'
        cronline = pycron.Cronline(line, 1)
        assert cronline.command == "this is a long line"
        assert cronline.parameters == ["abc", "def", '"foo bar"']
        line = '* * * * * command "this is a long line" foo bar'
        cronline = pycron.Cronline(line, 1)
        assert cronline.command == "command"
        assert cronline.parameters == ['"this is a long line"', "foo", "bar"]
        line = '* * * * * command'
        cronline = pycron.Cronline(line, 1)
        assert cronline.command == "command"
        assert cronline.parameters is None

    def check_missed_task_parser(self):
        """ command with ! or * """
        line = '* * * * * !"a command" "123"'
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.command, "a command")
        self.assertEqual(cronline.parameters, ["123"])
        line = '* * * * * *"a command" "123"'
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.command, "a command")
        self.assertEqual(cronline.parameters, ["123"])
        line = '* * * * * !acommand "123"'
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.command, "acommand")
        self.assertEqual(cronline.parameters, ["123"])
        line = '* * * * * *acommand "123"'
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.command, "acommand")
        self.assertEqual(cronline.parameters, ["123"])

    def check_lines(self):
        """ lines with different matching symbols """
        d = datetime.datetime(2003, 10, 25, 15, 35) # Saturday
        line = "* * * * * xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "*/5 * * * * every 5 minutes"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "*/4 * * * * every 4 minutes"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), False)
        line = "*/5 15 * * * xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "0-59/5 */3 * * * every 5 minutes, every 3 hours"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "0-59/5 */4 * * * every 5 minutes, every 4 hours"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), False)
        line = "1,2,3,4-7,9,10-19/2,20-59/2 * * * * xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), False)
        line = "1,2,3,4-7,9,10-19/2,20-59/3 * * * * xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "* * * * 6 xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        line = "* * * * 5 xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), False)
        d = datetime.datetime(2003, 10, 26, 15, 35) # Sunday
        line = "* * * * 0 xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        # XXX: this should work too:
        #line = "* * * * 7 xxx" # sunday, too
        #cronline = pycron.Cronline(line, 1)
        #self.assertEqual(cronline.checktime(d, d), True)
        d = datetime.datetime(2003, 10, 27, 15, 35) # Monday
        line = "* * * * 1 xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)

    def check_spaces(self):
        d = datetime.datetime(2003, 10, 25, 15, 35) # Saturday
        line = "* *       * *      6 xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)

    def check_exceptions(self):
        """ wrong lines - test exceptions """
        d = datetime.datetime(2003, 10, 25, 15, 35)
        line = "0-60 * * * * every minute, wrong format"
        cronline = pycron.Cronline(line, 1)
        self.assertRaises(pycron.InvalidLineException, cronline.checktime, d, d)
        line = "* 24 * * * wrong format"
        cronline = pycron.Cronline(line, 1)
        self.assertRaises(pycron.InvalidLineException, cronline.checktime, d, d)
        line = "* * * * 7 wrong dow"
        cronline = pycron.Cronline(line, 1)
        self.assertRaises(pycron.InvalidLineException, cronline.checktime, d, d)

    def check_startuptime(self):
        d = datetime.datetime(2003, 10, 25, 15, 3)
        d2 = datetime.datetime(2003, 10, 26, 15, 4)
        line = "? ? ? ? ? time of startup"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        self.assertEqual(cronline.checktime(d, d2), False)
        line = "* ? * ? ? time of startup"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        self.assertEqual(cronline.checktime(d, d2), False)
        line = "* ? * ? * time of startup"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d2), True)
        line = "*/2 ? * ? * time of startup"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d2), False)
        line = "*/3 ? * ? * time of startup"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d2), True)
        line = "* 22-2 * * * xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertRaises(pycron.InvalidLineException, cronline.checktime, d, d)

    def check_env_vars(self):
        d = datetime.datetime(2003, 10, 25, 22, 35)
        os.environ["TEST1"] = "this is environment variable no 1"
        os.environ["TEST2"] = "env_variable_2"
        line = "* 22-2 * * * %TEST1%\\%TEST2% %TEST2% %TEST1% %NOTFOUND%"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.command, "this is environment variable no 1\\env_variable_2")
        assert "this is environment variable no 1" in cronline.parameters
        assert "env_variable_2" in cronline.parameters
        assert "%NOTFOUND%" in cronline.parameters
        self.assertEqual(len(cronline.parameters), 3)

    def check_alphanumeric_values(self):
        d = datetime.datetime(2004, 11, 24, 22, 35)
        line = "* * * Oct-December Wednesday xxx"
        cronline = pycron.Cronline(line, 1)
        self.assertEqual(cronline.checktime(d, d), True)
        self.assertEqual(pycron.replace_alphanumerics("Septem"), 9)
        self.assertRaises(ValueError, pycron.replace_alphanumerics, "Sepptem")
        self.assertEqual(pycron.replace_alphanumerics("Sunday"), 0)
        self.assertEqual(pycron.replace_alphanumerics("Monday"), 1)
        self.assertEqual(pycron.replace_alphanumerics("Saturday"), 6)
        self.assertEqual(pycron.replace_alphanumerics("Fri"), 5)

    def check_parser_ranges(self):
        value = "1-3,5-6"
        for weekday in range(7):
            date = datetime.datetime(2005, 02, 27)
            date += datetime.timedelta(weekday)
            matcher = pycron.DayOfWeekMatcher(timestr=value, lineno=-1, old_dow_compatibility=False)
            if weekday in (1, 2, 3, 5, 6):
                self.failUnless(matcher.matches(date, date-datetime.timedelta(-1)))
            else:
                self.failIf(matcher.matches(date, date-datetime.timedelta(-1)))

    def check_missed_task(self):
        startup = datetime.datetime(2004, 11, 24, 22, 45)
        line = "*/15 * * Oct-December wed *missed tasks"
        cronline = pycron.Cronline(line, 1)
        shutdown = datetime.datetime(2004, 11, 24, 21, 30)
        self.assertEqual(cronline.missed_tasks(shutdown, startup, False), 4)

    def check_missed_task2(self):
        startup = datetime.datetime(2004, 11, 24, 22, 45)
        line = "*/15 * * Oct-December wed !'missed tasks'"
        cronline = pycron.Cronline(line, 1)
        shutdown = datetime.datetime(2004, 11, 24, 21, 30)
        self.assertEqual(cronline.missed_tasks(shutdown, startup, False), 1)

    def check_missed_task3(self):
        startup = datetime.datetime(2006, 01, 15, 9, 0)
        line = "0 2 * * * !'missed task'"
        cronline = pycron.Cronline(line, 1)
        shutdown = datetime.datetime(2006, 01, 15, 10, 0)
        self.assertEqual(cronline.missed_tasks(shutdown, startup, False), 0)

    def check_missed_task_questionmark(self):
        startup = datetime.datetime(2004, 11, 24, 22, 45)
        line = "? ? * Oct-December wed *missed tasks - should not work with question marks"
        cronline = pycron.Cronline(line, 1)
        shutdown = datetime.datetime(2004, 11, 24, 21, 30)
        self.assertEqual(cronline.missed_tasks(shutdown, startup, False), 0)

    def check_no_missed_task(self):
        startup = datetime.datetime(2004, 11, 24, 21, 45)
        line = "*/15 * * Oct-December Wednesday !no missed tasks"
        cronline = pycron.Cronline(line, 1)
        shutdown = datetime.datetime(2004, 11, 24, 21, 30)
        self.assertEqual(cronline.missed_tasks(shutdown, startup, False), 0)

    def check_valrange(self):
        """ MissedTaskParser.valrange """
        parser = pycron.MissedTaskParser(lineno = -1)
        self.assertEqual(parser.valrange(10, 2, "*", 1, 12, ismonth=True),
                         [{0: [10, 11, 12], 1: [1, 2]}])
        self.assertEqual(parser.valrange(10, 12, "*", 1, 12, ismonth=True),
                         [{0: [10, 11, 12]}])
        self.assertEqual(parser.valrange(10, 12, "*", 1, 12),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(parser.valrange(10, 12, "*/2", 1, 12),
                         [1, 3, 5, 7, 9, 11])
        self.assertEqual(parser.valrange(10, 12, "2,*/2", 1, 12),
                         [2, 1, 3, 5, 7, 9, 11])
        self.assertEqual(parser.valrange(9, 12, "*/2", 1, 12, ismonth=True),
                         [{0: [9, 11]}])
        self.assertEqual(parser.valrange(10, 2, "*/2", 1, 12, ismonth=True),
                         [{0: [11], 1: [1]}])
        self.assertEqual(parser.valrange(10, 2, "5,6-12/2", 1, 12),
                         [5, 6, 8, 10, 12])
        self.assertEqual(parser.valrange(2, 10, "5,6-12/2", 1, 12, ismonth=True),
                         [{0: [5]}, {0: [6, 8, 10]}])
        self.assertEqual(parser.valrange(10, 2, "Jan-Nov/2", 1, 12, ismonth=True),
                         [{0: [11], 1: [1]}])
        self.assertEqual(parser.valrange(10, 2, "11,1,2,3", 1, 12),
                         [11, 1, 2, 3])
        self.assertEqual(parser.valrange(10, 2, "Nov,Jan,Jan-Nov/2", 1, 12, ismonth=True),
                         [{0: [11], 1: []}, {0: [], 1: [1]}, {0: [11], 1: [1]}])


def makeTestSuite():
    return unittest.makeSuite(CronlineTestCase, "check_")

def suite():
    return makeTestSuite()

if __name__ == "__main__":
    unittest.main(defaultTest = "suite")
