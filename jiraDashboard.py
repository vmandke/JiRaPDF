import accessJiraData


#DEV :: Code Patches Merged 11301 GREEN
filterId = "11301"
headers = ["Priority", "Key","Summary"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Code Patch Review Pending
filterId = "11302"
headers = ["Priority","Key","Summary","Bugzilla Link", "Gerrit Link"]
tableStyleColor = "GREY"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Code Patch Review Comments 11412 ORANGE
filterId = "11412"
headers = ["Priority","Key","Summary","Bugzilla Link", "Gerrit Link"]
tableStyleColor = "ORANGE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)

#DEV :: Fixed 11402 GREEN
filterId = "11402"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)

#DEV :: Fixed and Closed GREEN 11403
filterId = "11403"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)

#QA :: Sprint Tasks GREY 11408
filterId = "11408"
headers = ["Priority","Key","Summary", "Status", "Resolution", "Assignee"]
tableStyleColor = "GREY"
accessJiraData.processFilter(filterId, headers, tableStyleColor)

#DEV :: Unassigned 11208 PURPLE
filterId = "11208"
headers = ["Priority", "Epic/Theme","Key","Summary", "Status"]
tableStyleColor = "PURPLE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Open and Reopened
filterId = "11407"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "RED"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: In Progress 11406 ORANGE
filterId = "11406"
headers = ["Priority", "Epic/Theme","Key","Summary"]
tableStyleColor = "ORANGE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#Visual Roundtrip Comparison Reports PURPLE 11409
filterId = "11409"
headers = ["Key","Summary", "DocumentLink"]
tableStyleColor = "PURPLE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#Visual Comparison Improvements PURPLE 11415
filterId = "11415"
headers = ["Key", "Summary", "Status"]
tableStyleColor = "PURPLE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Split ORANGE 11303
filterId = "11303"
headers = ["Key", "Links"]
tableStyleColor = "ORANGE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Duplicates GREEN  11304
filterId = "11304"
headers = ["Key", "Links"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Non Reproducible 11404 GREEN
filterId = "11404"
headers = ["Key"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#DEV :: Won't Fix GREEN 11405
filterId = "11405"
headers = ["Key"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)



#QA :: New Defects RED 11411
filterId = "11411"
headers = ["Priority", "Key","Summary"]
tableStyleColor = "RED"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#QA :: Verified and Closed  GREEN  11410
filterId = "11410"
headers = ["Priority", "Key","Summary"]
tableStyleColor = "GREEN"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#QA :: Verification Failed ORANGE 11414
filterId = "11414"
headers = ["Priority", "Key","Summary"]
tableStyleColor = "ORANGE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#FET Execution Reports  BLUE 11413
filterId = "11413"
headers = ["Key","Summary", "DocumentLink"]
tableStyleColor = "BLUE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


#FET Improvements BLUE 11416
filterId = "11416"
headers = ["Key","Summary", "DocumentLink"]
tableStyleColor = "BLUE"
accessJiraData.processFilter(filterId, headers, tableStyleColor)


