Purpose
-------

PyCron scans a file (crontab.txt) every minute and checks every line if the
specified time/date information matches the current time/date. If they are equal,
the command line specified will be executed. A log file (pycron.log) with the
executed commands is written to the current directory.


PyCron installation instructions
--------------------------------

Please go to control panel - services to adjust the settings for the
"Python Cron Service".

If you are a new user please rename the file crontab.txt.sample to crontab.txt and
change the file to your needs.

You can also use a graphical editor (pyCronEditor) to edit crontab entries.


How to use it
-------------

A good introductory article about pycron can be found at
http://www.bigbluehost.com/article4.html
["This article will discuss using a Cron type system, as used on Unix and Linux
systems, to bring the flexibility, scalability and a need for more out of a task
automation tool, to the Win32 environment."]


The crontab.txt file
--------------------

See the included file crontab.txt.sample for examples and the structure of
crontab entries.


Configuration
-------------

There is a sample configuration file "pycron.cfg.sample" in the program directory.
Rename this file to "pycron.cfg" and change it to your needs:

old_dow_compatibility = 1               ==> change day of week back to python style
                                            (0=Monday, ..., 6=Sunday)
crontab_filename = crontab.txt          ==> specify any other file
log_filename = pycron.log               ==> specify any other file