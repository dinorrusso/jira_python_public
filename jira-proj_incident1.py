
"""
This program is a test program to exercise the Python Jira module
A test Jira instance was set up with a service desk and a 
project.  Included are a couple of incidents in different states.

"""
from jira import JIRA

# remove to remote file - for testing only
# this is not good practice embedding auth info
# replace values to use
user = 'youremailid@whatever.com'
apikey = 'yourapikeygoeshere'
server = "https://yourserver.atlassian.net"
###########################################

# configure connection options dictionary
options = {
    'server': server
}

# basic connection
jira = JIRA(options, basic_auth=(user, apikey))


# print all of the project keys as an example
print('\n\n\n----------------- All Project Keys -----------')
for project in jira.projects():
    print(project.key)


# Getting all the incidents in a specific project
proj_issues = jira.search_issues(
    'project=yourprojectid')

# OUTPUT

print('******** All Issues in Service Desk ********')

for each_issue in proj_issues:
    issue = jira.issue(each_issue)
    print('------------------------------------------')
    print('----------------  ' + str(issue) + '  ------------------')
    print('------------------------------------------')
    print('Summary: ' + issue.fields.summary)
    print('Description: ' + issue.fields.description)
    print('Status: ' + issue.fields.status.name)
    print('Comments: ')
    comment_list = jira.comments(issue)
    # comment_list is a list that might be empty

    # print(comment_list)  # simple dump for debug purposes
    # this prints all the comments (internal and customer)
    for comment_id in comment_list:
        print('--------------- Comment ID: ' +
              str(comment_id) + ' ---------------')
        #print('comment id=' + str(comment_id))
        print('public = ' + str(jira.comment(issue, comment_id).jsdPublic))
        print(jira.comment(issue, comment_id).body)
    print('------------------------------------------')
