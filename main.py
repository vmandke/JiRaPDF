import time
import os
import subprocess


sQuery = "/opt/libreoffice4.1/program/soffice --writer  \"--accept=socket,host=localhost,port=2002;urp;\""
sJiraCmd = "/opt/libreoffice4.1/program/python /home/vinaya/JIRA-pdf/jiraDashboard.py"
proc = subprocess.Popen([sQuery],shell=True,stdout=subprocess.PIPE)
time.sleep(10)
proc = subprocess.Popen([sJiraCmd],shell=True)
