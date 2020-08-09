"""
This is a test of using the Python Requests Module
to make a REST API call to Jira.  

This  gets the comments for a given issue
No error checking

It then gets the count of comments and iterates 
through the response getting values of interest
example:
Comment ID: 10002
Comment Text: Do this then that and it will be fine.
Is Public: True

NOTE: you must change values below
"""
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

user = 'youremail.com'
apikey = 'yourapikey'
server = "https://your_server.atlassian.net"

# TS-1 is a sample Incident id, comment is field name
api_url_body = '/rest/servicedeskapi/request/TS-1/comment'

response = requests.get(
    server + api_url_body, auth=(user, apikey))
#print('--------------------------  api response----------------------------------\n')
# print(response.json())
response_dictionary = response.json()
print('--------------------------  Decoding Response-------------------------------\n')

print('Number of comments in TS1: ' + str(response_dictionary['size']))
print('---------------')
for i in range(response_dictionary['size']):
    print('Comment ID: ' + response_dictionary['values'][i]['id'])
    print('Comment Text: ' + response_dictionary['values'][i]['body'])
    print('Is Public: ' + str(response_dictionary['values'][i]['public']))
    print('---------------')
