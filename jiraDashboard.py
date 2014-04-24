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

def getAssignee(issue):
	return issue['fields']['assignee']['displayName']

def getResolution(issue):
	return "Unresolved" if (issue['fields']['resolution'] is None) \
	                    else issue['fields']['resolution']['name']

def getFilterName(data):
	return FilterName

def getEpicName(issue):
	return issue['fields']['customfield_10003']

def getStatus(issue):
	return issue['fields']['status']['name']

def getPriority(issue):
	return issue['fields']['priority']['name']

def getIssueLinks(issue):
	links = []
	jsonLinks = issue['fields']['issuelinks']
	for jsonLink in jsonLinks:
		if "outwardIssue" in jsonLink:
		    links.append(jsonLink['outwardIssue']['key'])
		elif "inwardIssue" in jsonLink:
		    links.append(jsonLink['inwardIssue']['key'])
	return links

def getDataListFromHeaders(issue,headers):
	dataList = []
	for header in headers:
		if header == "Key":
			dataList.append(getKey(issue))
		elif header == "Summary":
			dataList.append(getSummary(issue))
		elif header == "Bugzilla Link":
			dataList.append(getBugzillaLink(issue))
		elif header == "Gerrit Link":
			dataList.append(getPatchLink(issue))
		elif header == "Epic/Theme":
			dataList.append(getEpicName(issue))
		elif header == "Links":
			dataList.append(getIssueLinks(issue))
		elif header == "Status":
			dataList.append(getStatus(issue))
		elif header == "Priority":
			dataList.append(getPriority(issue))
		elif header == "Assignee":
			dataList.append(getAssignee(issue))
		elif header == "Resolution":
			dataList.append(getResolution(issue))
	return dataList

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
   
def processFilter(filterId, headers, tableStyleColor):
	filterData = getFilterData(filterId)
	LO.tableStyle(tableStyleColor)
	LO.insertHeading( FilterName, "Heading 3" )
	issueList = filterData['issues']
	LO.initTable(len(issueList), len(headers), headers)
	rowIndex = 2
	if (len(issueList) == 0):
		LO.insertHeading( "No matching issues found.", "Standard" )
	else:
		for i in  range(0,len(issueList)):
			issue = issueList[i];
			dataList = getDataListFromHeaders(issue,headers)
			LO.insertTextInRow(rowIndex, dataList)
			rowIndex = rowIndex + 1



readConfig()

LO = unoTable.PrintToWriter()



#DEV :: Code Patches Merged 11301 GREEN
filterId = "11301"
headers = ["Priority", "Key","Summary"]
tableStyleColor = "GREEN"
processFilter(filterId, headers, tableStyleColor)


#DEV :: Code Patch Review Pending
filterId = "11302"
headers = ["Priority","Key","Summary","Bugzilla Link", "Gerrit Link"]
tableStyleColor = "GREY"
processFilter(filterId, headers, tableStyleColor)


#DEV :: Code Patch Review Comments 11412 ORANGE
filterId = "11412"
headers = ["Priority","Key","Summary","Bugzilla Link", "Gerrit Link"]
tableStyleColor = "ORANGE"
processFilter(filterId, headers, tableStyleColor)

#DEV :: Fixed 11402 GREEN
filterId = "11402"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "GREEN"
processFilter(filterId, headers, tableStyleColor)

#DEV :: Fixed and Closed GREEN 11403
filterId = "11403"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "GREEN"
processFilter(filterId, headers, tableStyleColor)

#DEV :: Unassigned 11208 PURPLE
filterId = "11208"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "PURPLE"
processFilter(filterId, headers, tableStyleColor)


#DEV :: Open and Reopened
filterId = "11407"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "RED"
processFilter(filterId, headers, tableStyleColor)


#DEV :: In Progress 11406 ORANGE
filterId = "11406"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "ORANGE"
processFilter(filterId, headers, tableStyleColor)


#DEV :: Non Reproducible 11404 GREEN
filterId = "11404"
headers = ["Key"]
tableStyleColor = "GREEN"
processFilter(filterId, headers, tableStyleColor)



