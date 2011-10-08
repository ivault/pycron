@echo off
c:\python24\python.exe setup.py py2exe -q
copy c:\python24\msvcr71.dll dist