import json
import subprocess
import unoTable
import os

username = ""
password = ""
sQueryConfig= ""
FilterName = ""

def readConfig():
	global username, password, sQueryConfig
	jdata=open( os.path.dirname(os.path.realpath(__file__)) + '/config.json')
	jConfig = json.load(jdata)	
	username = jConfig['username']
	password = jConfig['password']
	sQueryConfig = " curl -u " + username + ":" + password + " " 


def getKey(issue):
	return issue['key']

def getSummary(issue):
	return issue['fields']['summary']

def getPatchLink(issue):
	return issue['fields']['customfield_10102']

def getBugzillaLink(issue):
	return issue['fields']['customfield_10100']

def getFilterName(data):
	return FilterName
def getEpicName(issue):
	return issue['fields']['customfield_10003']

def getIssueLinks(issue):
	links = []
	jsonLinks = issue['fields']['issuelinks']
	for jsonLink in jsonLinks:
		if "outwardIssue" in jsonLink:
		    links.append(jsonLink['outwardIssue']['key'])
		elif "inwardIssue" in jsonLink:
		    links.append(jsonLink['inwardIssue']['key'])
	return links

def getFilterData(filterId):
	global FilterName;
	sQuery = sQueryConfig + " https://synerzip.atlassian.net/rest/api/2/filter/" + filterId
	process = subprocess.Popen([sQuery], shell=True,stdout=subprocess.PIPE)
	out, err = process.communicate()
	jData = json.loads(out.decode("utf-8"))
	FilterName = jData['name']
	searchUrl = jData['searchUrl']
	#print searchUrl

	sQuery =  sQueryConfig + " '" + searchUrl + "'"
	process = subprocess.Popen([sQuery], shell=True,stdout=subprocess.PIPE)
	out, err = process.communicate()
	data = json.loads((out).decode("utf-8"))
	return data
   


readConfig()

LO = unoTable.PrintToWriter()


#DEV :: Code Patch Review Pending
filterData = getFilterData("11302")
LO.tableStyle("GREY")
LO.insertHeading( FilterName )
issueList = filterData['issues']
headers = ["Key","Summary","Bugzilla Link", "Gerrit Link"]
LO.initTable(len(issueList), len(headers), headers)
rowIndex = 2
for i in  range(0,len(issueList)):
	issue = issueList[i];
	dataList = [getKey(issue), getSummary(issue), getBugzillaLink(issue), getPatchLink(issue)]
	LO.insertTextInRow(rowIndex, dataList)
	rowIndex = rowIndex + 1




#DEV :: Open and Reopened
filterData = getFilterData("11407")
LO.tableStyle("RED")
LO.insertHeading( FilterName )
issueList = filterData['issues']
headers = ["Epic/Theme","Key","Summary"]
LO.initTable(len(issueList),len(headers), headers)
rowIndex = 2
for i in  range(0,len(issueList)):
	issue = issueList[i];
	dataList = [getEpicName(issue), getKey(issue), getSummary(issue)]
	LO.insertTextInRow(rowIndex, dataList)
	rowIndex = rowIndex + 1


#DEV :: Code Patches Merged 11301 GREEN
filterData = getFilterData("11301")
LO.tableStyle("GREEN")
LO.insertHeading( FilterName )
issueList = filterData['issues']
headers = ["Key","Summary"]
LO.initTable(len(issueList),len(headers), headers)
rowIndex = 2
for i in  range(0,len(issueList)):
	issue = issueList[i];
	dataList = [getKey(issue), getSummary(issue)]
	LO.insertTextInRow(rowIndex, dataList)
	rowIndex = rowIndex + 1



