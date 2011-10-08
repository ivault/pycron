; This file is part of PyCron.
;
; PyCron is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 3 of the License, or
; (at your option) any later version.
;
; PyCron is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; You should have received a copy of the GNU General Public License
; along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


#define MainPath "dist\"
#define AppVersion GetFileVersion(MainPath + "pycron.exe")

[Files]
Source: {#MainPath}pyCronEditor.exe; DestDir: {app}
Source: {#MainPath}pycron.exe; DestDir: {app}
Source: {#MainPath}pycron_console.exe; DestDir: {app}
Source: about.html; DestDir: {app}
Source: {#MainPath}shared.zip; DestDir: {app}
Source: {#MainPath}win32api.pyd; DestDir: {app}
Source: {#MainPath}win32evtlog.pyd; DestDir: {app}
Source: {#MainPath}win32service.pyd; DestDir: {app}
Source: crontab.txt.sample; DestDir: {app}
Source: {#MainPath}win32file.pyd; DestDir: {app}
Source: a little testscript.cmd; DestDir: {app}
Source: test.py; DestDir: {app}
Source: {#MainPath}_html.pyd; DestDir: {app}
Source: {#MainPath}_misc_.pyd; DestDir: {app}
Source: {#MainPath}_controls_.pyd; DestDir: {app}
Source: {#MainPath}_windows_.pyd; DestDir: {app}
Source: {#MainPath}_gdi_.pyd; DestDir: {app}
Source: {#MainPath}_core_.pyd; DestDir: {app}
Source: {#MainPath}servicemanager.pyd; DestDir: {app}
Source: {#MainPath}wxbase271uh_vc.dll; DestDir: {app}
Source: {#MainPath}wxmsw271uh_html_vc.dll; DestDir: {app}
Source: {#MainPath}wxmsw271uh_adv_vc.dll; DestDir: {app}
Source: {#MainPath}wxmsw271uh_core_vc.dll; DestDir: {app}
Source: {#MainPath}wxbase271uh_net_vc.dll; DestDir: {app}
Source: readme.txt; DestDir: {app}; Flags: isreadme
Source: pyCronEditor.exe.manifest; DestDir: {app}
Source: pycron.cfg.sample; DestDir: {app}
Source: changes.txt; DestDir: {app}
;only for python 2.3:
;Source: {#MainPath}_subprocess.pyd; DestDir: {app}
;Source: {#MainPath}python23.dll; DestDir: {app}
;Source: {#MainPath}pywintypes23.dll; DestDir: {app}
;Source: {#MainPath}datetime.pyd; DestDir: {app}
;Source: {#MainPath}w9xpopen.exe; DestDir: {app}
;Source: {#MainPath}_csv.pyd; DestDir: {app}
;Source: {#MainPath}_sre.pyd; DestDir: {app}
;;Source: {#MainPath}_winreg.pyd; DestDir: {app}
;only for python 2.4:
Source: {#MainPath}msvcr71.dll; DestDir: {app}
Source: {#MainPath}python24.dll; DestDir: {app}
Source: {#MainPath}pywintypes24.dll; DestDir: {app}
[Run]
Filename: {app}\pycron.exe; Parameters: -install -auto -interactive; WorkingDir: {app}; Description: Install as a service; Flags: postinstall; MinVersion: 0,4.0.1381
[UninstallRun]
Filename: {app}\pycron.exe; Parameters: -remove; WorkingDir: {app}
[Setup]
MinVersion=0,4.0.1381
AppCopyright=© 2005 Gerhard Kalab
AppName=Python Cron Service
AppVerName=pycron {#AppVersion}
PrivilegesRequired=admin
DefaultDirName={pf}\pycron\
AllowRootDirectory=true
DisableReadyPage=false
SolidCompression=true
Compression=lzma/ultra
DefaultGroupName=pycron
OutputBaseFilename=pycron-{#AppVersion}
;AppID={220505AD-018F-4430-8AEC-46F92702DAD1}
ShowLanguageDialog=yes
AppMutex=pycron.exe
InternalCompressLevel=ultra
InfoBeforeFile=update.txt

[_ISTool]
;Use7zip=true
UseAbsolutePaths=false
[Icons]
Name: {group}\crontab.txt Editor; Filename: {app}\pyCronEditor.exe; WorkingDir: {app}; Comment: crontab.txt Editor; IconIndex: 0
Name: {group}\{cm:UninstallProgram, Python Cron Service}; Filename: {uninstallexe}
